import numpy as np
import os
import glob
import re

import networkx as nx
from pyvis.network import Network
from skimage.color import rgb2lab, lab2rgb
from matplotlib.colors import to_rgb, to_hex

def interpolate_colors(nodes):
    node_colors_rgb = [to_rgb(node.color) for node in nodes]
    node_colors_lab = [rgb2lab([[color]])[0][0] for color in node_colors_rgb]
    avg_color_lab = np.mean(node_colors_lab, axis=0)
    avg_color_rgb = lab2rgb([[avg_color_lab]])[0][0]
    return to_hex(avg_color_rgb)



class Node:
    def __init__(self, name, base_radius=0, parents=[],
                 color=None, type='document', description="",
                 link = None):
        self.name = name
        self.base_area = base_radius**2
        self.parents = parents
        if color is None:
            if len(parents) > 0:
                self.color = interpolate_colors(self.parents)
            else:
                raise ValueError("Color must be specified if there are no parents.")
        else:
            self.color = color
        self.type = type
        self.description = description
        self.link = link
        self.highlight = False        
        self.children = []
        for parent in self.parents:
            parent.add_child(self)
            
    def add_child(self, child):
        self.children.append(child)

    def compute_area(self):
        descendants = self._collect_unique_descendants()
        return sum(node.base_area for node in descendants)
    
    def _collect_unique_descendants(self):
        descendants = set()
        stack = [self]
        while stack:
            node = stack.pop()
            descendants.add(node)
            stack.extend(node.children)
        return descendants

class KnowledgeMap:
    def __init__(self):
        self.node_dict = {}
        
    def add_node(self, name, base_radius=0, parent_names=[], color=None,
                type='document', description="", link=None):
        parents = [self.node_dict[parent] for parent in parent_names]
        self.node_dict[name] = Node(name,
                            base_radius=base_radius,
                            parents=parents,
                            color=color,
                            type=type,
                            description=description,
                            link=link)

    def render(self):
        G = nx.Graph()
        G.add_nodes_from(self.node_dict.keys())
        
        net = Network(
            notebook=True,
            bgcolor="#000000",
            font_color="white",
            width="100%",    # Set to full width
            height="100vh"   # Set to full height of the viewport
        )
        #net = Network(notebook=True, bgcolor="#000000", font_color="white")        
        for g_node in G.nodes:
            node = self.node_dict[g_node]
            label = f"“{node.name}”" if node.type in ['document', 'book', 'class', 'paper', 'post', 'chapter'] else node.name
            
            adjusted_radius = np.sqrt(node.compute_area()) * 1
            
            page_url = None
            if node.link:
                if node.link == "auto":
                    pluralized_type = node.type + 's' if node.type not in ['class'] else node.type + 'es'
                    hyphenated_name = re.sub(r'[-\s]+', '-', node.name).strip('-')
                    file_location = os.path.join("Notes", pluralized_type, hyphenated_name + ".md")
                    page_url = f"https://maswang32.github.io/knowledgemap/notes/{pluralized_type}/{hyphenated_name}/"

                    if not os.path.exists(file_location):
                        raise FileNotFoundError(f"File Not Found:\t{file_location}")
                else:
                    file_location = node.link
                              
                with open(file_location, 'r') as file:
                    file_text = file.read()
                    
                if node.description:
                    title = node.description + "\n" + file_text
                else:
                    title = file_text
            else:
                title = node.description
            
            node_attrs = {
                "label": label,
                "title": title,
                "size": max(adjusted_radius, 5),
                "mass": adjusted_radius**2 / 100,
                "fixed": False
            }
            
            if not node.link:
                node_attrs["color"] = node.color
            else:
                node_attrs["color"] = {
                    "background": node.color,
                    "border": "white",
                    "borderWidth" : 1,
                }
                node_attrs["href"] = page_url
            net.add_node(g_node, **node_attrs)

        # Add edges
        for node in self.node_dict.values():
            for parent in node.parents:
                net.add_edge(
                    node.name,
                    parent.name,
                    width = 4,
                    color=parent.color,
                    arrows="to"
                )

        # Configure physics options as a JavaScript string
        options_string = """
        {
            "nodes": {
                "borderWidth": 1,
                "borderWidthSelected": 3,
                "chosen": true,
                "shape": "dot",
                "font": {
                    "size": 20,
                    "color": "white"
                }
            },
            "edges": {
                "color": {
                    "inherit": true
                },
                "smooth": false
            },
            "physics": {
                "enabled": true,
                "solver": "hierarchicalRepulsion",
                "hierarchicalRepulsion": {
                    "nodeDistance": 150,
                    "centralGravity": 0.01,
                    "springLength": 150,
                    "springConstant": 0.001,
                    "damping": 0.5
                },
                "stabilization": {
                    "enabled": true,
                    "iterations": 2000,
                    "fit": true
                },
                "direction": "UD",
                "minVelocity": 0.75,
                "maxVelocity": 30
            },
            "interaction": {
            "zoomView": true,
            "dragView": true,
            "zoomSpeed": 0.5,
            "mouseWheel": true
            }
        }
        """

        #with open("template.html") as f:
        #    custom_template = f.read()

        # 2) Tell PyVis to use that template
        #net.set_template(custom_template)

        net.set_options(options_string)
        
        net.on('click', """
        function(params) {
            if (params.nodes.length > 0) {
                var nodeId = params.nodes[0];
                var node = this.body.nodes[nodeId];
                if (node.options.url) {
                    window.open(node.options.url, '_blank');
                }
            }
        }
        """)
        net.write_html("index.html")




            

if __name__=="__main__":
    M = KnowledgeMap()


    # radius 7 = one paper
    # radius 10 = UDL Chapter, Chain Rule, Gradients, Adam, UDL 
    # Math
    M.add_node("Math", type='concept', color="#C41E3A")
    M.add_node("Statistics", type='concept',  parent_names=["Math"], color='#FF6F20') #FFBF00
    M.add_node("Information Theory", type='concept', parent_names=["Math"])
    M.add_node("Linear Algebra", type='concept',  parent_names=["Math"])
    M.add_node("Calculus", type='concept',  parent_names=["Math"])
    M.add_node("Optimization", type='concept', parent_names=["Statistics"])
    
    M.add_node("Momentum, RMSProp, Adam", type='concept', parent_names=["Optimization"], base_radius=10, link='auto')
    M.add_node("Gradients", type='concept',  parent_names=["Calculus", "Linear Algebra"], base_radius=10, link="auto")
    M.add_node("Chain Rule", type='concept',  parent_names=["Gradients"], base_radius=10, link="auto")
    M.add_node("Infinitesimals", type='concept',  parent_names=["Calculus"], base_radius=5, link="auto")


    M.add_node("Functions", type='concept',  parent_names=["Math"], base_radius=1, link="auto")
    
    M.add_node("A Brief Introduction To Information", type='post', parent_names=["Information Theory"], link="auto", base_radius=2)

    M.add_node("Deep Learning Chapter 3", type='chapter', parent_names=["Information Theory"])
    M.add_node("KL Divergence", type='concept', parent_names=["Information Theory"], base_radius=5, link="auto")
    M.add_node("Six Interpretations of KL Divergence", type='post', parent_names=["KL Divergence"], base_radius=5, link="auto")
    M.add_node("Entropy", type='concept', parent_names=["Deep Learning Chapter 3"], base_radius=5, link="auto")
    M.add_node("Cross Entropy", type='concept', parent_names=["Deep Learning Chapter 3"], base_radius=5, link="auto")

    M.add_node("Info Theory Basics", type='concept', parent_names=["Deep Learning Chapter 3"], base_radius=5  , link="auto")
    M.add_node("Random-Variables-and-Probability-Distributions", type='concept', parent_names=["Statistics"], base_radius=10, link='auto')
    M.add_node("Bayes", type='concept', parent_names=["Statistics"], base_radius=10, link='auto')
    M.add_node("Conditional Independence", type='concept', parent_names=["Statistics"], base_radius=5, link='auto')


    # Deep Learning
    M.add_node("Deep Learning", type='concept', color="#0000FF")
    
    # Software
    M.add_node("Software", type='concept', color="#212129")
    M.add_node("PyTorch", type='software', parent_names=["Software", "Deep Learning"], base_radius=10, link='auto')


    # Activation Functions
    M.add_node("Activation Functions", type='concept', parent_names=["Deep Learning"])
    M.add_node("Pocketed Activations", type='concept', parent_names=["Activation Functions"], base_radius=2, link='auto')
    M.add_node("Gated Activations", type='concept', parent_names=["Activation Functions"], base_radius=2, link='auto')


    # UDL Textbook
    M.add_node("Understanding Deep Learning", type='book', parent_names=["Deep Learning"])
    M.add_node("MLP Interpretation - UDL", type='chapter', parent_names=["Understanding Deep Learning"], base_radius=10, description="Last Recall: 10/24/24", link="auto")
    M.add_node("Loss Functions - UDL", type='chapter', parent_names=["Understanding Deep Learning"], base_radius=10, link="auto")

    # Generative Modeling FFBF00
    M.add_node("Generative Modeling", type='concept', color="#FFD900", parent_names=["Deep Learning"]) #FFA500
    M.add_node("VAEs - UDL", type='chapter', parent_names=["Understanding Deep Learning", "Generative Modeling"], base_radius=10, link='auto')
    M.add_node("ELBO", type='concept', parent_names=["Optimization", "VAEs - UDL"], base_radius=4, link='auto')
    M.add_node("Jensens Inequality", type='concept', parent_names=["ELBO"], base_radius=4, link='auto')
    M.add_node("Optimization - UDL", type='chapter', parent_names=["Understanding Deep Learning", "Optimization"], base_radius=10, link="auto")

    M.add_node("Diffusion Models", type='concept', parent_names=["Generative Modeling"])
    M.add_node("DDPM - UDL", type='chapter', parent_names=["Understanding Deep Learning", "Diffusion Models"], base_radius=10, link='auto')
    M.add_node("DDPM - Math", type='chapter', parent_names=["DDPM - UDL"], base_radius=10, link='auto')
    M.add_node("DDPM - Reparametrization", type='chapter', parent_names=["DDPM - UDL"], base_radius=10, link='auto')

    M.add_node("Understanding Diffusion Models: A Unified Perspective", type='post', parent_names=["Diffusion Models"], base_radius=20, description="Last Recall: 7/14/24")

    M.add_node("Score Based Generative Models", type='post', parent_names=["Diffusion Models"], base_radius=10)

    M.add_node("Generative Modeling Using SDEs", type='post', parent_names=["Score Based Generative Models"], base_radius=10)
    
    M.add_node("Wiener Process", type='concept',  parent_names=["Calculus", "Statistics", "Generative Modeling Using SDEs"], base_radius=5, link="auto")



    # Audio
    M.add_node("Audio", type='concept', color="#3FFF57")
    M.add_node("DiffWave", type='paper', parent_names=["Audio", "Diffusion Models"], base_radius=7, link='auto')
    M.add_node("DAC", type='paper', parent_names=["Audio"], base_radius=7, link='auto')


    # Vision
    M.add_node("Vision", type='concept', color="#79443B")
    M.add_node("VAR", type='paper', parent_names=["Vision", "Generative Modeling"], base_radius=7, link='auto')
    M.add_node("Gaussian Splatting", type='paper', parent_names=["Vision"], base_radius=7, link='auto')


    # Language Modeling
    M.add_node("Language Modeling", type='concept', parent_names=["Deep Learning"], color="#00FF00")
    M.add_node("Language Modeling from Scratch", type='class', parent_names=["Language Modeling"], description="Last Recall: 6/14/24", link="auto")
    M.add_node("Transformers", type='concept', parent_names=["Language Modeling from Scratch"], description="Last Recall: 6/14/24", link="auto", base_radius=10)


    # Papers
    M.add_node("Interpretability", type='concept', parent_names=["Deep Learning"])
    M.add_node("Concept Activation Vectors", type='paper', parent_names=["Interpretability"], base_radius=7, link="auto")


    # Fine Tuning
    M.add_node("Fine Tuning", type='concept', parent_names=["Deep Learning"], link="auto")

    # Signal Processing
    M.add_node("Signal Processing", type='concept',color="#a8326f")
    M.add_node("DDSP", type='concept',  parent_names=["Signal Processing", "Deep Learning"], base_radius=7)
    M.add_node("PQMF", type='concept',  parent_names=["Signal Processing"], base_radius=7, link="auto")
    M.add_node("Downsampling and Stretching", type='concept',  parent_names=["Signal Processing"], base_radius=7, link="auto")
    M.add_node("Convolution", type='concept',  parent_names=["Signal Processing"], base_radius=7, link="auto")
    M.add_node("Transpose Convolution", type='concept',  parent_names=["Signal Processing"], base_radius=7, link="auto")
    
    # RL
    M.add_node("Reinforcement Learning", type='concept', color="#808080")
    M.add_node("ReaLChords", type='paper', parent_names=["Reinforcement Learning"], base_radius=7, description="Last Recall: 9/25/24")
    M.add_node("CS 285", type='class',  parent_names=["Reinforcement Learning"], base_radius=10, description="Last Recall: 9/25/24")
    M.render()
    
    
    list_of_notes_documents = [os.path.splitext(os.path.basename(path))[0] for path in glob.glob("Notes/*/*.md")]
    simplified_keys = [re.sub(r'[-\s]+', '-', name).strip('-') for name in list(M.node_dict.keys())]
    unassigned_notes = [name for name in list_of_notes_documents if name not in simplified_keys]    
    print("Unassigned Notes")
    print(unassigned_notes)
    


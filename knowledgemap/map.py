import numpy as np
import os
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
    def __init__(self, name, base_size=0, parents=[],
                 color=None, type='document', description="",
                 link = "", review_flag=False):
        self.name = name
        self.base_size = base_size
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
        self.review_flag = review_flag        
        self.children = []
        for parent in self.parents:
            parent.add_child(self)
            
    def add_child(self, child):
        self.children.append(child)
    
    
    def compute_size(self):
        descendants = self._collect_unique_descendants()
        return sum(node.base_size for node in descendants)
    
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
        
    def add_node(self, name, base_size=0, parent_names=[], color=None,
                type='document', description="", link="", review_flag=False):
        parents = [self.node_dict[parent] for parent in parent_names]
        self.node_dict[name] = Node(name,
                            base_size=base_size,
                            parents=parents,
                            color=color,
                            type=type,
                            description=description,
                            link=link,
                            review_flag=review_flag)

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
            label = f"“{node.name}”" if node.type in ['document', 'book', 'class', 'paper', 'blog post', 'chapter'] else node.name
            
            adjusted_size = node.compute_size() * 1
            
            if node.link:
                if node.link == "auto":
                    pluralized_type = node.type + 's' if node.type not in ['class'] else node.type + 'es'
                    file_location = os.path.join("Notes", pluralized_type, node.name + ".notes")
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
                "size": max(adjusted_size, 5),
                "mass": adjusted_size / 100,
                "fixed": False
            }
            
            if not node.review_flag:
                node_attrs["color"] = node.color
            else:
                node_attrs["color"] = {
                    "background": node.color,
                    "border": "white",
                }
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
                "borderWidth": 2,
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
        
        net.set_options(options_string)
        net.write_html("index.html")




            

if __name__=="__main__":
    M = KnowledgeMap()


    # size 7 = size of a paper
    # Math
    M.add_node("Math", type='concept', color="#C41E3A")
    M.add_node("Statistics", type='concept',  parent_names=["Math"])
    M.add_node("Information Theory", type='concept', parent_names=["Math"])
    M.add_node("Linear Algebra", type='concept',  parent_names=["Math"])
    M.add_node("Calculus", type='concept',  parent_names=["Math"])
    M.add_node("Optimization", type='concept', parent_names=["Statistics"])
    
    M.add_node("Momentum, RMSProp, Adam", type='concept', parent_names=["Optimization"], base_size=10, link='auto')
    M.add_node("Gradients", type='concept',  parent_names=["Linear Algebra", "Calculus"], base_size=10, link="auto")
    M.add_node("Chain Rule", type='concept',  parent_names=["Gradients"], base_size=10, link="auto")
    M.add_node("Functions", type='concept',  parent_names=["Math"], base_size=1, link="auto")
    
    M.add_node("A Brief Introduction To Information", type='blog post', parent_names=["Information Theory"], link="auto", base_size=2)

    M.add_node("Deep Learning Chapter 3", type='chapter', parent_names=["Information Theory"])
    M.add_node("KL Divergence", type='concept', parent_names=["Deep Learning Chapter 3"], base_size=5, link="auto")
    M.add_node("Entropy", type='concept', parent_names=["Deep Learning Chapter 3"], base_size=5, link="auto")
    M.add_node("Info Theory Basics", type='concept', parent_names=["Deep Learning Chapter 3"], base_size=5  , link="auto")






    # Deep Learning
    M.add_node("Deep Learning", type='concept', color="#0000FF")

    
    # UDL Textbook
    M.add_node("Understanding Deep Learning", type='book', parent_names=["Deep Learning"])
    M.add_node("MLP Interpretation - UDL", type='chapter', parent_names=["Understanding Deep Learning"], base_size=10, description="Last Recall: 10/24/24", link="auto")
    
    
    
    M.add_node("Loss Functions - UDL", type='chapter', parent_names=["Understanding Deep Learning"], base_size=10, link="auto")
    M.add_node("Optimization - UDL", type='chapter', parent_names=["Understanding Deep Learning", "Optimization"], base_size=10, link="auto")
    
    
    # Diffusion
    M.add_node("Diffusion Models", type='concept', parent_names=["Deep Learning"])
    M.add_node("Understanding Diffusion Models: A Unified Perspective", type='blog post', parent_names=["Diffusion Models"], base_size=20, description="Last Recall: 7/14/24", review_flag=True)


    # Language Modeling
    M.add_node("Language Modeling", type='concept', parent_names=["Deep Learning"], color="#00FF00")
    M.add_node("Language Modeling from Scratch", type='class', parent_names=["Language Modeling"], description="Last Recall: 6/14/24", link="auto")
    M.add_node("Transformers", type='concept', parent_names=["Language Modeling from Scratch"], description="Last Recall: 6/14/24", link="auto", base_size=10)


    # Papers
    M.add_node("Interpretability", type='concept', parent_names=["Deep Learning"])
    M.add_node("Concept Activation Vectors", type='paper', parent_names=["Interpretability"], base_size=7, link="auto")


    # Fine Tuning
    M.add_node("Fine Tuning", type='concept', parent_names=["Deep Learning"], link="auto")

    # Signal Processing
    M.add_node("Signal Processing", type='concept',color="#a8326f")
    M.add_node("DDSP", type='concept',  parent_names=["Signal Processing", "Deep Learning"], base_size=7)



    
    
    
    # RL 
    M.add_node("Reinforcement Learning", type='concept', color="#808080")
    M.add_node("ReaLChords", type='paper', parent_names=["Reinforcement Learning"], base_size=7, description="Last Recall: 9/25/24")
    M.add_node("CS 285", type='class',  parent_names=["Reinforcement Learning"], base_size=10, description="Last Recall: 9/25/24")










    M.render()
    


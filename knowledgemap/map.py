"""
Everything in this Python file has been humanized!
The only part that was pasted is shown in the comments, but I believe this was already humanized.
In addition, options_string and custom_script could be better interpreted.
"""

import os
import glob
import numpy as np
from pyvis.network import Network
from skimage.color import rgb2lab, lab2rgb
from matplotlib.colors import to_rgb, to_hex

def interpolate_colors(nodes):
    node_colors_rgb = [to_rgb(node.color) for node in nodes]
    node_colors_lab = rgb2lab(node_colors_rgb)
    avg_color_lab = np.mean(node_colors_lab, axis=0)
    avg_color_rgb = lab2rgb(avg_color_lab)
    return to_hex(avg_color_rgb)

class Node:
    def __init__(
        self,
        name,
        base_radius,
        parents,
        color,
    ):
        self.name = name
        self.base_area = base_radius**2
        self.parents = parents
        
        if color is None:
            if len(parents) > 0:
                self.color = interpolate_colors(self.parents)
            else:
                raise ValueError("Must specify node color if no parents")
        else:
            self.color = color
        
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
    
    def add_node(
        self,
        name,
        base_radius=0,
        parent_names=[],
        color=None,
    ):
        parents = [self.node_dict[parent] for parent in parent_names]
        
        self.node_dict[name] = Node(
            name=name,
            base_radius=base_radius,
            parents=parents,
            color=color,
        )
    
    def render(self):
        net = Network(
            bgcolor = "#000000",
            font_color="white",
            width="100%",
            height="100vh",
        )
        
        for node in self.node_dict.values():
            radius = np.sqrt(node.compute_area())
            
            # Link node to url
            # Get Node Text
            hyphenated_name = node.name.replace(" ", "-")
            file_location = os.path.join("notes", hyphenated_name + ".md")
            
            if os.path.exists(file_location):
                page_url = f"https://maswang32.github.io/knowledgemap/{file_location[:-3]}/"
                
                with open(file_location, "r") as f:
                    node_text = f.read()
            else:
                node_text = ""
                
            
            node_attrs = {
                "label" : node.name,
                "title" : node_text,
                "size" : radius,
                "mass" : radius**2 / 100,
            }
            
            if len(node_text) == 0:
                node_attrs["color"] = node.color
            else:
                node_attrs["color"] = {
                    "background" : node.color,
                    "border" : "white",
                    "borderWidth" : 1,
                }
                node_attrs["href"] = page_url
                assert node.base_area > 0, f"Node {node.name} with notes must have positive size"
            net.add_node(node.name, **node_attrs)
        
        for node in self.node_dict.values():
            for parent in node.parents:
                net.add_edge(
                    node.name,
                    parent.name,
                    width=4,
                    color=parent.color,
                    arrows="to",
                )
        
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
                "smooth": false
            },
            "physics": {
                "enabled": true,
                "solver": "hierarchicalRepulsion",
                "hierarchicalRepulsion": {
                    "nodeDistance": 150,
                    "centralGravity": 0.01,
                    "springLength": 150,
                    "springConstant": 0.0007,
                    "damping": 0.5
                },
                "stabilization": {
                    "enabled": true,
                    "iterations": 2000,
                    "fit": true
                }
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
            





if __name__ == "__main__":   
    M = KnowledgeMap()
    
    
    ### Pasted in from previous
    # Radius 7 = One Paper
    # Radius 10 = One textbook chapter (UDL)
    
    # Math
    M.add_node(
        "Math",
        color="#C41E3A",
    )
    M.add_node(
        "Linear Algebra",
        base_radius=0,
        parent_names=["Math"],
    )
    M.add_node(
        "Calculus",
        base_radius=0,
        parent_names=["Math"],
    )
    M.add_node(
        "Gradients",
        base_radius=10,
        parent_names=["Calculus", "Linear Algebra"],
    )
    M.add_node(
        "Chain Rule",
        base_radius=10,
        parent_names=["Gradients"],
    )
    M.add_node(
        "Infinitesimals",
        base_radius=5,
        parent_names=["Calculus"],
    )
    M.add_node(
        "Functions",
        base_radius=5,
        parent_names=["Math"],
    )
    M.add_node(
        "Group Theory",
        base_radius=5,
        parent_names=["Math"],
    )

    
    
    
    # Information Theory
    M.add_node(
        "Information Theory",
        base_radius=5,
        parent_names=["Math"],
    )
    M.add_node(
        "A Brief Introduction To Information",
        base_radius=5,
        parent_names=["Information Theory"],
    )
    M.add_node(
        "Deep Learning Chapter 3",
        base_radius=10,
        parent_names=["Information Theory"],
    )
    M.add_node(
        "KL Divergence",
        base_radius=5,
        parent_names=["Information Theory"],
    )
    M.add_node(
        "Six Interpretations of KL Divergence",
        parent_names=["KL Divergence"],
        base_radius=5,
    )
    M.add_node(
        "Entropy",
        parent_names=["Information Theory"],
        base_radius=5,
    )
    M.add_node(
        "Cross Entropy",
        parent_names=["Information Theory"],
        base_radius=5,
    )
    
    
    
    
    # Statistics
    M.add_node(
        "Statistics",
        base_radius=0,
        parent_names=["Math"],
        color="#FF6F20",
    )
    M.add_node(
        "Biased vs Unbiased Estimates",
        base_radius=3,
        parent_names=["Statistics"],
    )
    M.add_node(
        "Uniform Width Sampling",
        base_radius=1,
        parent_names=["Statistics"],
    )
    M.add_node(
        "Random Variables and Probability Distributions",
        parent_names=["Statistics"],
        base_radius=10,
    )
    M.add_node(
        "Bayes",
        parent_names=["Statistics"],
        base_radius=10,
    )
    M.add_node(
        "Conditional Independence",
        parent_names=["Statistics"],
        base_radius=5,
    )
    
    
    # Optimization
    M.add_node(
        "Optimization",
        base_radius=0,
        parent_names=["Statistics"],
    )
    M.add_node(
        "Momentum, RMSProp, Adam",
        base_radius=10,
        parent_names=["Optimization"],
    )

    
    # Traditional Statistical Learning
    M.add_node("Statistical Learning", parent_names=["Math", "Statistics"])
    M.add_node("Linear Classifiers", parent_names=["Statistical Learning"], base_radius=7)

    # Deep Learning
    M.add_node("Deep Learning", color="#0000FF")
    M.add_node("Backpropagation", parent_names=["Deep Learning", "Chain Rule"], base_radius=10)
    M.add_node(
        "Interpretability", parent_names=["Deep Learning"]
    )
    M.add_node(
        "Concept Activation Vectors",
        parent_names=["Interpretability"],
        base_radius=7,
    )

    # Fine Tuning
    M.add_node(
        "Fine Tuning",
        parent_names=["Deep Learning"],
        base_radius=5,
    )
    
    
    # Architecture
    M.add_node(
        "Architecture", parent_names=["Deep Learning"]
    )
    
    M.add_node(
        "Normalization",
        parent_names=["Architecture"],
        base_radius=7,
    )
    M.add_node(
        "Batchnorm",
        parent_names=["Normalization"],
        base_radius=3,
    )
    
    M.add_node(
        "Positional Encodings",
        parent_names=["Architecture"],
        base_radius=7,
    )

    # Activation Functions
    M.add_node(
        "Activation Functions", parent_names=["Architecture"]
    )
    M.add_node(
        "Pocketed Activations",
        parent_names=["Activation Functions"],
        base_radius=2,
    )
    M.add_node(
        "Gated Activations",
        parent_names=["Activation Functions"],
        base_radius=2,
    )
    
    

    # UDL Textbook
    M.add_node(
        "Understanding Deep Learning",
        parent_names=["Deep Learning"],
    )
    M.add_node(
        "MLP Interpretation - UDL",
        parent_names=["Understanding Deep Learning"],
        base_radius=10,
    )
    M.add_node(
        "Loss Functions - UDL",
        parent_names=["Understanding Deep Learning"],
        base_radius=10,
    )
    M.add_node(
        "Optimization - UDL",
        parent_names=["Understanding Deep Learning", "Optimization"],
        base_radius=10,
    )
    M.add_node(
        "Gradients and Initialization - UDL",
        parent_names=[
            "Understanding Deep Learning",
            "Optimization",
            "Chain Rule",
        ],
        base_radius=10,
    )


    # Generative Modeling
    M.add_node(
        "Generative Modeling",
        color="#FFD900",
        parent_names=["Deep Learning"],
    )
    
    # UDL Generative Modeling Chapters
    M.add_node(
        "VAEs - UDL",
        parent_names=["Understanding Deep Learning", "Generative Modeling"],
        base_radius=10,
    )
    M.add_node(
        "ELBO",
        parent_names=["Optimization", "VAEs - UDL"],
        base_radius=4,
    )
    M.add_node(
        "Jensens Inequality",
        parent_names=["ELBO"],
        base_radius=4,
    )
    
    
    M.add_node(
        "Energy Based Generative Models",
        parent_names=["Generative Modeling"],
        base_radius=7,
    )

    
    
    # Diffusion Models
    M.add_node(
        "Diffusion Models", parent_names=["Generative Modeling"]
    )
    M.add_node(
        "DDPM - UDL",
        parent_names=["Understanding Deep Learning", "Diffusion Models"],
        base_radius=10,
    )
    M.add_node(
        "DDPM - Math",
        parent_names=["DDPM - UDL"],
        base_radius=10,
    )
    M.add_node(
        "DDPM - Reparametrization",
        parent_names=["DDPM - UDL"],
        base_radius=10,
    )
    M.add_node(
        "DDPM - Noise Schedules",
        parent_names=["DDPM - UDL"],
        base_radius=7,
    )
    M.add_node(
        "Diffusion Best Practices",
        parent_names=["Diffusion Models"],
        base_radius=5,
    )
    M.add_node(
        "Diffusion Forcing",
        parent_names=["Diffusion Models"],
        base_radius=7,
    )
    M.add_node(
        "Diffusion Beats GANs",
        parent_names=["Diffusion Models"],
        base_radius=7,
    )
    M.add_node(
        "History Guidance",
        parent_names=["Diffusion Forcing"],
        base_radius=7,
    )
    M.add_node(
        "DiT",
        parent_names=["Diffusion Models"],
        base_radius=7,
    )
    M.add_node(
        "Edify Image",
        parent_names=["Diffusion Models"],
        base_radius=2,
    )
    M.add_node(
        "Understanding Diffusion Models: A Unified Perspective",
        parent_names=["Diffusion Models"],
        base_radius=20,
    )
    M.add_node(
        "Score Based Generative Models",
        parent_names=["Diffusion Models"],
        base_radius=10,
    )
    M.add_node(
        "Generative Modeling Using SDEs",
        parent_names=["Score Based Generative Models"],
        base_radius=10,
    )
    M.add_node(
        "Wiener Process",
        parent_names=[
            "Calculus",
            "Statistics",
            "Generative Modeling Using SDEs",
        ],
        base_radius=5,
    )
    M.add_node(
        "Classifier Free Guidance",
        parent_names=[
            "Diffusion Models",
        ],
        base_radius=5,
    )

    # Diffusion Model Papers
    M.add_node(
        "DDIM",
        parent_names=["Diffusion Models"],
        base_radius=7,
    )
    M.add_node(
        "Elucidated Diffusion Models",
        parent_names=["Diffusion Models"],
        base_radius=10,
    )
    
    
    # Training
    M.add_node(
        "Training",
        parent_names=["Deep Learning"],
        base_radius=10,
    )
    M.add_node(
        "A Recipe for Training Neural Networks",
        parent_names=["Training"],
        base_radius=7,
    )



    # Audio
    M.add_node("Audio", color="#3FFF57")
    M.add_node(
        "DiffWave",
        parent_names=["Audio", "Diffusion Models"],
        base_radius=7,
    )
    M.add_node(
        "DAC", parent_names=["Audio"], base_radius=7
    )

    # Vision
    M.add_node("Vision", color="#79443B")
    M.add_node(
        "VAR",
        parent_names=["Vision", "Generative Modeling"],
        base_radius=7,
    )
    M.add_node(
        "Gaussian Splatting",
        parent_names=["Vision"],
        base_radius=7,
    )
    
    # Advances in Computer Vision Class
    M.add_node(
        "Advances In Computer Vision",
        parent_names=["Vision"],
        base_radius=20,
    )
    M.add_node(
        "Image Formation",
        parent_names=["Advances In Computer Vision"],
        base_radius=5,
    )
    M.add_node(
        "Linear Image Processing",
        parent_names=["Advances In Computer Vision"],
        base_radius=5,
    )
    M.add_node(
        "Geometric Deep Learning",
        parent_names=["Vision", "Deep Learning"],
        base_radius=5,
    )

    # Deep Vision
    M.add_node(
        "CNNs",
        parent_names=["Vision", "Deep Learning"],
        base_radius=7,
    )
    M.add_node(
        "UNet",
        parent_names=["CNNs"],
        base_radius=7,
    )
    M.add_node(
        "PixelVAE",
        parent_names=["Generative Modeling", "Vision"],
        base_radius=7,
    )

    # Language Modeling
    M.add_node(
        "Language Modeling",
        parent_names=["Deep Learning"],
        color="#00FF00",
    )
    M.add_node(
        "Language Modeling from Scratch",
        parent_names=["Language Modeling"],
        base_radius=10,
    )
    M.add_node(
        "Transformers",
        parent_names=["Language Modeling"],
        base_radius=10,
    )
    M.add_node(
        "Encoder Decoder Transformers",
        parent_names=["Transformers"],
        base_radius=5,
    )

    
    # Software
    M.add_node("Software", color="#212129")
    
    
    M.add_node(
        "Filesystems",
        parent_names=["Software"],
        base_radius=1,
    )
    M.add_node(
        "Python",
        parent_names=["Software"],
        base_radius=1,
    )
    M.add_node(
        "Hydra",
        parent_names=["Python"],
        base_radius=2,
    )
    M.add_node(
        "Slurm",
        parent_names=["Software"],
        base_radius=2,
    )
    M.add_node(
        "Vector Operations",
        parent_names=["Software"],
    )
    M.add_node(
        "Einsum",
        parent_names=["Vector Operations"], base_radius=7,
    )
    
    # ML Systems
    M.add_node(
        "ML Systems",
        parent_names=["Software", "Deep Learning"],
        base_radius=0,
    )
    M.add_node(
        "Mixed Precision",
        parent_names=["ML Systems"],
        base_radius=7,
    )
    M.add_node(
        "Wandb",
        parent_names=["ML Systems"],
        base_radius=5,
    )
    M.add_node(
        "PyTorch",
        parent_names=["ML Systems", "Python"],
        base_radius=10,
    )
    M.add_node(
        "Lightning",
        parent_names=["PyTorch"],
        base_radius=5,
    )
    M.add_node(
        "Large Scale Deep Learning",
        parent_names=["ML Systems"],
        base_radius=7,
    )
    M.add_node(
        "Large Scale Deep Learning",
        parent_names=["ML Systems"],
        base_radius=5,
    )
    M.add_node(
        "Webdataset",
        parent_names=["Large Scale Deep Learning"],
        base_radius=5,
    )
    M.add_node(
        "Distributed Training",
        parent_names=["Large Scale Deep Learning", "Training"],
        base_radius=7,
    )


    # Signal Processing
    M.add_node("Signal Processing", color="#a8326f")
    M.add_node(
        "DDSP",
        parent_names=["Signal Processing", "Deep Learning"],
        base_radius=7,
    )
    M.add_node(
        "PQMF",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add_node(
        "Downsampling and Stretching",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add_node(
        "Convolution",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add_node(
        "Transpose Convolution",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add_node(
        "Discrete Fourier Transform",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add_node(
        "Fourier Dualities",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add_node(
        "Pink Frequency Profiles",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add_node(
        "1f Noise in Music and Speech",
        parent_names=["Pink Frequency Profiles"],
        base_radius=7,
    )

    # RL
    M.add_node("Reinforcement Learning", color="#808080")
    M.add_node(
        "ReaLChords",
        parent_names=["Reinforcement Learning"],
        base_radius=7,
    )
    M.add_node(
        "CS 285",
        parent_names=["Reinforcement Learning"],
        base_radius=10,
    )
    M.add_node(
        "Actor Critic",
        parent_names=["CS 285"],
        base_radius=7,
    )
    M.add_node(
        "Policy Gradient",
        parent_names=["CS 285"],
        base_radius=7,
    )
    
    M.add_node(
        "Generalized Advantage Estimation",
        parent_names=["Actor Critic"],
        base_radius=7,
    )
    M.add_node(
        "RLOO",
        parent_names=["Reinforcement Learning"],
        base_radius=7,
    )
    ### End Paste
    M.render()
    
    
    
    # Detect Unassigned Notes
    list_of_notes_documents = [
        os.path.basename(path)[:-3].replace("-", "").replace(" ", "") for path in glob.glob("notes/*.md")
    ]
    list_of_node_names = [
        name.replace("-", "").replace(" ", "") for name in M.node_dict.keys()
    ]
    
    unassigned_notes = [
        name for name in list_of_notes_documents if name not in list_of_node_names
    ]
    # if len(unassigned_notes) > 0:
    #    raise LookupError(f"Unassigned Notes: {unassigned_notes}")
    
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    
    # Add Node Linking
    custom_script = """
    <script type="text/javascript">
    document.addEventListener("DOMContentLoaded", function() {
        network.on('click', function(params) {
            if (params.nodes.length > 0) {
                var nodeId = params.nodes[0];
                var nodeData = network.body.data.nodes.get(nodeId);
                if (nodeData.href) {
                    window.open(nodeData.href, '_blank');
                }
            }
        });
    });
    </script>
    </body>
    """
    html = html.replace("</body>", custom_script)
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html)
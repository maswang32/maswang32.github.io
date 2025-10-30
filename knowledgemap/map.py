"""
Everything in this Python file has been humanized!
The only part that was pasted are the M.add section in main,
but I believe this was already humanized.
In addition, options_string and custom_script could be better interpreted.

To Do:
- Add all Notes
- Resize nodes
"""

import os
from glob import glob
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

    def add(
        self,
        name,
        base_radius=5,
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
            bgcolor="#000000",
            font_color="white",
            width="100%",
            height="100vh",
        )

        for node in self.node_dict.values():
            radius = np.sqrt(node.compute_area())

            # Link node to url
            # Get Node Text
            hyphenated_name = node.name.replace(" ", "-")

            file_locations = glob(os.path.join("notes", "*", hyphenated_name + ".md"))

            if len(file_locations) == 0:
                node_text = ""
            elif len(file_locations) == 1:
                file_location = file_locations[0]
                page_url = (
                    f"https://maswang32.github.io/knowledgemap/{file_location[:-3]}/"
                )
                with open(file_location, "r") as f:
                    node_text = f.read()
            else:
                raise ValueError(f"Duplicate Files Found: {file_locations}")

            node_attrs = {
                "label": node.name,
                "title": node_text,
                "size": radius,
                "mass": radius**2 / 100,
            }

            if len(node_text) == 0:
                node_attrs["color"] = node.color
            else:
                node_attrs["color"] = {
                    "background": node.color,
                    "border": "white",
                    "borderWidth": 1,
                }
                node_attrs["href"] = page_url
                assert node.base_area > 0, (
                    f"Node {node.name} with notes must have positive size"
                )
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
            "layout": {
                "clusterThreshold": 1000000
            },
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
                    "nodeDistance": 120,
                    "centralGravity": 0.01,
                    "springLength": 120,
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

    # region Math
    M.add("Math", color="#C41E3A")
    M.add("Functions", parent_names=["Math"])
    M.add("Group Theory", parent_names=["Math"])

    M.add("Linear Algebra", parent_names=["Math"])
    M.add("Eigenvalues", parent_names=["Linear Algebra"])

    M.add("Calculus", parent_names=["Math"])
    M.add("Infinitesimals", parent_names=["Calculus"])
    M.add("Gradients", parent_names=["Calculus", "Linear Algebra"])
    M.add("Gradients - UDL", parent_names=["Gradients"])
    M.add("Chain Rule", parent_names=["Gradients"])
    # endregion

    # region Information Theory
    M.add("Information Theory", parent_names=["Math"])
    M.add("A Brief Introduction To Information", parent_names=["Information Theory"])
    M.add("Deep Learning Chapter 3", parent_names=["Information Theory"])

    M.add("KL Divergence", parent_names=["Information Theory"])
    M.add("Six Interpretations of KL Divergence", parent_names=["KL Divergence"])

    M.add("Entropy", parent_names=["Information Theory"])
    M.add("Cross Entropy", parent_names=["Information Theory"])
    # endregion
    
    

    # region Statistics
    M.add("Statistics", parent_names=["Math"], color="#FF6F20")
    M.add("Biased vs Unbiased Estimates", parent_names=["Statistics"])
    M.add("Uniform Width Sampling", parent_names=["Statistics"])
    M.add("Random Variables and Probability Distributions", parent_names=["Statistics"])
    M.add("Bayes", parent_names=["Statistics"])
    M.add("Conditional Independence", parent_names=["Statistics"])
    M.add("Covariance", parent_names=["Statistics"])
    # endregion

    # region Optimization
    M.add("Optimization", parent_names=["Statistics"])
    M.add("Optimization - UDL", parent_names=["Optimization"])
    M.add("Momentum, RMSProp, Adam", parent_names=["Optimization"])
    # endregion

    # region Machine Learning
    M.add("Machine Learning", parent_names=["Statistics"])
    M.add("Linear Classifiers", parent_names=["Machine Learning"])
    M.add("K-Nearest Neighbors", parent_names=["Machine Learning"])
    M.add("K-Means", parent_names=["Machine Learning"])
    M.add(
        "Approximate Nearest Neighbors", parent_names=["K-Nearest Neighbors", "K-Means"]
    )
    # endregion

    # region Signal Processing
    M.add("Signal Processing", color="#a8326f")
    M.add("DDSP", parent_names=["Signal Processing"])
    M.add("PQMF", parent_names=["Signal Processing"])
    M.add("Downsampling and Stretching", parent_names=["Signal Processing"])
    M.add("Convolution", parent_names=["Signal Processing"])
    M.add("Transpose Convolution", parent_names=["Convolution"])
    # endregion

    # region Fourier
    M.add("Fourier Transform", parent_names=["Signal Processing"])
    M.add("Discrete Fourier Transform", parent_names=["Fourier Transform"])
    M.add("Fourier Dualities", parent_names=["Fourier Transform"])
    M.add("Pink Frequency Profiles", parent_names=["Fourier Transform"])
    M.add("1f Noise in Music and Speech", parent_names=["Pink Frequency Profiles"])
    # endregion


    # region Deep Learning
    M.add("Deep Learning", color="#0000FF")
    M.add("Initialization - UDL", parent_names=["Deep Learning"])
    M.add("Measuring Performance - UDL", parent_names=["Deep Learning"])
    # endregion

    # region Interpretability
    M.add("Interpretability", parent_names=["Deep Learning"])
    M.add("Concept Activation Vectors", parent_names=["Interpretability"])
    # endregion

    # region Deep Learning Theory
    M.add("Deep Learning Theory", parent_names=["Deep Learning"])
    M.add("Geometric Deep Learning", parent_names=["Deep Learning Theory"])
    M.add("Double Descent", parent_names=["Deep Learning Theory"])
    M.add("Generalization", parent_names=["Deep Learning Theory"])
    M.add("Bias-Variance Tradeoff", parent_names=["Deep Learning Theory"])
    # endregion

    # region Training
    M.add("Training", parent_names=["Deep Learning"])
    M.add("A Recipe for Training Neural Networks", parent_names=["Training"])
    M.add("Evolution Strategies", parent_names=["Training"])
    M.add("Backpropagation", parent_names=["Training", "Chain Rule"])
    M.add("Loss Functions", parent_names=["Training"])
    M.add("Loss Functions - UDL", parent_names=["Loss Functions"])
    # endregion

    # region Finetuning
    M.add("Fine Tuning", parent_names=["Deep Learning"])
    # endregion

    # region Architecture
    M.add("Architecture", parent_names=["Deep Learning"])
    M.add("Positional Encodings", parent_names=["Architecture"])
    M.add("Autoencoders", parent_names=["Architecture"])
    # endregion

    # region MLPs
    M.add("MLPs", parent_names=["Architecture"])
    M.add("MLP Interpretation - UDL", parent_names=["MLPs"])
    M.add("Approximation Theorem", parent_names=["MLPs"])
    # endregion

    # region CNNs
    M.add("CNNs", parent_names=["Architecture", "Convolution"])
    M.add("UNet", parent_names=["CNNs"])
    # endregion

    # region sequence models
    M.add("Sequence Models", parent_names=["Architecture"])
    M.add("LSTM", parent_names=["Sequence Models"])
    M.add("RNNs", parent_names=["Sequence Models"])
    # endregion

    # region transformers
    M.add("Transformers", parent_names=["Architecture"])
    M.add("Encoder Transformers", parent_names=["Transformers"])
    M.add("Decoder Transformers", parent_names=["Transformers"])
    M.add("KV-Caching", parent_names=["Decoder Transformers"])
    M.add(
        "Encoder Decoder Transformers",
        parent_names=["Decoder Transformers", "Encoder Transformers"],
    )
    # endregion

    # region activation functions
    M.add("Activation Functions", parent_names=["Architecture"])
    M.add("Pocketed Activations", parent_names=["Activation Functions"])
    M.add("Gated Activations", parent_names=["Activation Functions"])
    # endregion
    
    # region normalization
    M.add("Normalization", parent_names=["Architecture"])
    M.add("Batchnorm", parent_names=["Normalization"])
    M.add("GroupNorm", parent_names=["Normalization"])
    M.add("InstanceNorm", parent_names=["Normalization"])
    M.add("LayerNorm", parent_names=["Normalization"])
    M.add("RMSNorm", parent_names=["Normalization"])
    # endregion

    # region Generative models
    M.add("Generative Modeling", color="#FFD900", parent_names=["Deep Learning"])
    M.add("Energy Based Generative Models", parent_names=["Generative Modeling"])
    M.add("Next-Scale Prediction", parent_names=["Generative Modeling"])
    # endregion

    # region GANs
    M.add("GANs", parent_names=["Generative Modeling"])
    M.add("CLIP Plus GAN", parent_names=["GANs"])
    # endregion

    # region VAEs
    M.add("VAEs - UDL", parent_names=["Generative Modeling"])
    M.add("ELBO", parent_names=["VAEs - UDL"])
    M.add("Jensens Inequality", parent_names=["ELBO"])
    # endregion

    # region Diffusion
    M.add("Diffusion Models", parent_names=["Generative Modeling"])
    M.add("Diffusion Best Practices", parent_names=["Diffusion Models"])
    M.add("Denoising Autoencoder", parent_names=["Diffusion Models"])
    M.add("Classifier Free Guidance", parent_names=["Diffusion Models"])
    # endregion

    # region Diffusion Papers
    M.add("Elucidated Diffusion Models", parent_names=["Diffusion Models"])
    M.add("DiT", parent_names=["Diffusion Models"])
    M.add("DDIM", parent_names=["Diffusion Models"])
    M.add("Diffusion Beats GANs", parent_names=["Diffusion Models"])
    M.add("Edify Image", parent_names=["Diffusion Models"])
    M.add("Diffusion Forcing", parent_names=["Diffusion Models"])
    M.add("History Guidance", parent_names=["Diffusion Forcing"])
    # endregion

    # region Diffusion Posts
    M.add(
        "Understanding Diffusion Models: A Unified Perspective",
        parent_names=["Diffusion Models"],
    )
    M.add("Score-Based Generative Models", parent_names=["Diffusion Models"])
    M.add(
        "Generative Modeling Using SDEs", parent_names=["Score-Based Generative Models"]
    )
    M.add("Wiener Process", parent_names=["Generative Modeling Using SDEs"])
    # endregion

    # region DDPM
    M.add("DDPM - UDL", parent_names=["Diffusion Models"])
    M.add("DDPM - Math", parent_names=["DDPM - UDL"])
    M.add("DDPM - Reparametrization", parent_names=["DDPM - UDL"])
    M.add("DDPM - Noise Schedules", parent_names=["DDPM - UDL"])
    # endregion

    # region Representation Learning
    M.add("Representation Learning", parent_names=["Deep Learning"])
    M.add("Contrastive Learning", parent_names=["Representation Learning"])
    # endregion

    # region Audio
    M.add("Audio", color="#3FFF57")
    M.add("DiffWave", parent_names=["Audio"])
    M.add("DAC", parent_names=["Audio"])
    M.add("Next-Scale Audio Prediction", parent_names=["Audio", "Next-Scale Prediction"])
    # endregion

    # region Vision
    M.add("Vision", color="#79443B")
    M.add("PixelVAE", parent_names=["Vision", "Generative Modeling"])
    M.add("VAR", parent_names=["Vision", "Next-Scale Prediction"])
    # endregion

    # region 3D Reconstruction
    M.add("3D Reconstruction", parent_names=["Vision"])
    M.add("Gaussian Splatting", parent_names=["3D Reconstruction"])
    M.add("NeRF", parent_names=["3D Reconstruction"])
    # endregion

    # region Advances in Computer Vision
    M.add("Advances In Computer Vision", parent_names=["Vision"])
    M.add("Image Formation", parent_names=["Advances In Computer Vision"])
    M.add("Linear Image Processing", parent_names=["Advances In Computer Vision"])
    # endregion

    # region Language
    M.add("Language Modeling", color="#00FF00")
    M.add("LLMs", parent_names=["Language Modeling", "Deep Learning"])
    M.add("Byte-Pair Encoding", parent_names=["Language Modeling"])
    M.add("Language Modeling from Scratch", parent_names=["Language Modeling"])
    # endregion

    # region Reinforcement Learning
    M.add("Reinforcement Learning", color="#808080")
    M.add("ReaLChords", parent_names=["Reinforcement Learning"])
    M.add("RLOO", parent_names=["Reinforcement Learning"])
    M.add("Imitation Learning", parent_names=["Reinforcement Learning"])
    M.add("Policy Gradient", parent_names=["Reinforcement Learning"])
    M.add("Actor Critic", parent_names=["Reinforcement Learning"])
    M.add("Generalized Advantage Estimation", parent_names=["Actor Critic"])
    M.add("CS 285", parent_names=["Actor Critic", "Policy Gradient", "Deep Learning"])
    # endregion
    
    # region Computer Science
    M.add("Computer Science", color="#212129")
    M.add("Linked Lists", parent_names=["Computer Science"])
    # endregion


    # region Software
    M.add("Software", parent_names=["Computer Science"])
    M.add("Filesystems", parent_names=["Software"])
    M.add("Slurm", parent_names=["Software"])
    M.add("Python", parent_names=["Software"])
    M.add("Vector Operations", parent_names=["Python"])
    M.add("Einsum", parent_names=["Vector Operations"])
    M.add("Hydra", parent_names=["Python"])
    # endregion

    # region ML systems
    M.add("ML Systems", parent_names=["Computer Science", "Deep Learning"])
    M.add("Mixed Precision", parent_names=["ML Systems"])
    M.add("Large Scale Deep Learning", parent_names=["ML Systems"])
    M.add("Webdataset", parent_names=["Large Scale Deep Learning"])

    M.add("Wandb", parent_names=["ML Systems", "Software"])
    M.add("PyTorch", parent_names=["ML Systems", "Python"])
    M.add("Autograd", parent_names=["PyTorch"])
    M.add("Lightning", parent_names=["PyTorch"])
    M.add("Distributed Training", parent_names=["Large Scale Deep Learning"])
    # endregion

    M.render()

    # Detect Unassigned Notes
    list_of_notes_documents = [
        os.path.basename(path)[:-3].replace("-", "").replace(" ", "")
        for path in glob("notes/*/*.md")
    ]
    list_of_node_names = [
        name.replace("-", "").replace(" ", "") for name in M.node_dict.keys()
    ]

    unassigned_notes = [
        name for name in list_of_notes_documents if name not in list_of_node_names
    ]
    # if len(unassigned_notes) > 0:
    #     raise LookupError(f"Unassigned Notes: {unassigned_notes}")

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

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

    # Radius 7 = One Paper
    # Radius 10 = One textbook chapter (UDL)
    # region Math
    M.add(
        "Math",
        color="#C41E3A",
    )
    M.add(
        "Linear Algebra",
        base_radius=0,
        parent_names=["Math"],
    )
    M.add(
        "Eigenvalues",
        base_radius=3,
        parent_names=["Linear Algebra"],
    )
    M.add(
        "Calculus",
        base_radius=0,
        parent_names=["Math"],
    )
    M.add(
        "Gradients",
        base_radius=10,
        parent_names=["Calculus", "Linear Algebra"],
    )
    M.add(
        "Gradients - UDL",
        parent_names=[
            "Gradients",
        ],
        base_radius=5,
    )
    M.add(
        "Chain Rule",
        base_radius=10,
        parent_names=["Gradients"],
    )
    M.add(
        "Infinitesimals",
        base_radius=5,
        parent_names=["Calculus"],
    )
    M.add(
        "Functions",
        base_radius=5,
        parent_names=["Math"],
    )
    M.add(
        "Group Theory",
        base_radius=5,
        parent_names=["Math"],
    )
    # endregion

    # region Information Theory
    M.add(
        "Information Theory",
        base_radius=5,
        parent_names=["Math"],
    )
    M.add(
        "A Brief Introduction To Information",
        base_radius=5,
        parent_names=["Information Theory"],
    )
    M.add(
        "Deep Learning Chapter 3",
        base_radius=10,
        parent_names=["Information Theory"],
    )
    M.add(
        "KL Divergence",
        base_radius=5,
        parent_names=["Information Theory"],
    )
    M.add(
        "Six Interpretations of KL Divergence",
        parent_names=["KL Divergence"],
        base_radius=5,
    )
    M.add(
        "Entropy",
        parent_names=["Information Theory"],
        base_radius=5,
    )
    M.add(
        "Cross Entropy",
        parent_names=["Information Theory"],
        base_radius=5,
    )
    # endregion

    # region Statistics
    M.add(
        "Statistics",
        base_radius=0,
        parent_names=["Math"],
        color="#FF6F20",
    )
    M.add(
        "Biased vs Unbiased Estimates",
        base_radius=3,
        parent_names=["Statistics"],
    )
    M.add(
        "Uniform Width Sampling",
        base_radius=1,
        parent_names=["Statistics"],
    )
    M.add(
        "Random Variables and Probability Distributions",
        parent_names=["Statistics"],
        base_radius=10,
    )
    M.add(
        "Bayes",
        parent_names=["Statistics"],
        base_radius=10,
    )
    M.add(
        "Conditional Independence",
        parent_names=["Statistics"],
        base_radius=5,
    )
    M.add(
        "Covariance",
        parent_names=["Statistics"],
        base_radius=5,
    )
    # endregion

    # region Optimization
    M.add(
        "Optimization",
        base_radius=0,
        parent_names=["Statistics"],
    )
    M.add(
        "Momentum, RMSProp, Adam",
        base_radius=10,
        parent_names=["Optimization"],
    )
    M.add(
        "Optimization - UDL",
        parent_names=["Momentum, RMSProp, Adam"],
        base_radius=10,
    )
    # endregion

    # region Machine Learning
    M.add("Machine Learning", parent_names=["Statistics"])
    M.add("Linear Classifiers", parent_names=["Machine Learning"], base_radius=7)
    M.add("K-Nearest Neighbors", parent_names=["Machine Learning"], base_radius=7)
    M.add("K-means", parent_names=["Machine Learning"], base_radius=7)
    M.add(
        "Approximate Nearest Neighbors",
        parent_names=["K-Nearest Neighbors"],
        base_radius=7,
    )
    M.add("Bias-Variance Tradeoff", parent_names=["Machine Learning"], base_radius=7)
    # endregion

    # region Deep Learning
    M.add("Deep Learning", color="#0000FF")
    M.add("Initialization - UDL", parent_names=["Deep Learning"], base_radius=5)
    M.add("Measuring Performance - UDL", parent_names=["Deep Learning"], base_radius=5)
    # endregion

    # region Interpretability
    M.add("Interpretability", parent_names=["Deep Learning"])
    M.add(
        "Concept Activation Vectors", parent_names=["Interpretability"], base_radius=7
    )
    # endregion

    # region Deep Learning Theory
    M.add(
        "Deep Learning Theory",
        parent_names=["Deep Learning"],
        base_radius=5,
    )
    M.add(
        "Geometric Deep Learning",
        parent_names=["Deep Learning Theory"],
        base_radius=5,
    )
    M.add(
        "Double Descent",
        parent_names=["Deep Learning Theory"],
        base_radius=5,
    )
    M.add(
        "Generalization",
        parent_names=["Deep Learning Theory"],
        base_radius=5,
    )
    # endregion

    # region Training
    M.add(
        "Training",
        parent_names=["Deep Learning"],
        base_radius=10,
    )
    M.add(
        "Evolution Strategies",
        parent_names=["Training"],
        base_radius=10,
    )
    M.add(
        "Backpropagation",
        parent_names=["Training", "Chain Rule"],
        base_radius=10,
    )
    M.add(
        "Loss Functions",
        parent_names=["Training"],
        base_radius=1,
    )
    M.add(
        "Loss Functions - UDL",
        parent_names=["Loss Functions"],
        base_radius=10,
    )
    M.add(
        "A Recipe for Training Neural Networks",
        parent_names=["Training"],
        base_radius=7,
    )
    # endregion

    # region Finetuning
    M.add(
        "Fine Tuning",
        parent_names=["Deep Learning"],
        base_radius=5,
    )
    # endregion

    # region Architecture
    M.add("Architecture", parent_names=["Deep Learning"])
    M.add(
        "Positional Encodings",
        parent_names=["Architecture"],
        base_radius=7,
    )
    M.add(
        "Autoencoders",
        parent_names=["Architecture"],
        base_radius=7,
    )
    # endregion

    # region MLPs
    M.add(
        "MLPs",
        parent_names=["Architecture"],
        base_radius=0,
    )
    M.add(
        "MLP Interpretation - UDL",
        parent_names=["MLPs"],
        base_radius=10,
    )
    M.add(
        "Approximation Theorem",
        parent_names=["MLPs"],
        base_radius=3,
    )
    # endregion

    # region CNNs
    M.add(
        "CNNs",
        parent_names=["Deep Learning"],
        base_radius=7,
    )
    M.add(
        "UNet",
        parent_names=["CNNs"],
        base_radius=7,
    )
    # endregion

    # region sequence models
    M.add(
        "Sequence Models",
        parent_names=["Architecture"],
        base_radius=5,
    )
    M.add(
        "LSTM",
        parent_names=["Sequence Models"],
        base_radius=5,
    )
    M.add(
        "RNNs",
        parent_names=["Sequence Models"],
        base_radius=5,
    )
    # endregion

    # region transformers
    M.add(
        "Transformers",
        parent_names=["Architecture"],
        base_radius=10,
    )
    M.add(
        "Decoder Transformers",
        parent_names=["Transformers"],
        base_radius=5,
    )
    M.add(
        "Encoder Transformers",
        parent_names=["Transformers"],
        base_radius=5,
    )
    M.add(
        "Encoder Decoder Transformers",
        parent_names=["Decoder Transformers", "Encoder Transformers"],
        base_radius=5,
    )
    M.add(
        "KV-Caching",
        parent_names=["Decoder Transformers"],
        base_radius=5,
    )
    # endregion

    # region activation functions
    M.add("Activation Functions", parent_names=["Architecture"])
    M.add(
        "Pocketed Activations",
        parent_names=["Activation Functions"],
        base_radius=2,
    )
    M.add(
        "Gated Activations",
        parent_names=["Activation Functions"],
        base_radius=2,
    )
    # endregion

    # region Generative models
    M.add(
        "Generative Modeling",
        color="#FFD900",
        parent_names=["Deep Learning"],
    )
    M.add(
        "Energy Based Generative Models",
        parent_names=["Generative Modeling"],
        base_radius=7,
    )
    # endregion

    # region GANs
    M.add(
        "GANs",
        parent_names=["Generative Modeling"],
        base_radius=0,
    )
    M.add(
        "CLIP Plus GAN",
        parent_names=["GANs"],
        base_radius=10,
    )
    # endregion

    # region VAEs
    M.add(
        "VAEs - UDL",
        parent_names=["Generative Modeling"],
        base_radius=10,
    )
    M.add(
        "ELBO",
        parent_names=["VAEs - UDL"],
        base_radius=4,
    )
    M.add(
        "Jensens Inequality",
        parent_names=["ELBO"],
        base_radius=4,
    )
    # endregion

    # region Diffusion
    M.add("Diffusion Models", parent_names=["Generative Modeling"])
    M.add(
        "Diffusion Best Practices",
        parent_names=["Diffusion Models"],
        base_radius=5,
    )
    M.add(
        "Denoising Autoencoder",
        parent_names=["Diffusion Models"],
        base_radius=5,
    )
    M.add(
        "Classifier Free Guidance",
        parent_names=[
            "Diffusion Models",
        ],
        base_radius=5,
    )
    # endregion

    # region DDPM
    M.add(
        "DDPM - UDL",
        parent_names=["Diffusion Models"],
        base_radius=10,
    )
    M.add(
        "DDPM - Math",
        parent_names=["DDPM - UDL"],
        base_radius=10,
    )
    M.add(
        "DDPM - Reparametrization",
        parent_names=["DDPM - UDL"],
        base_radius=10,
    )
    M.add(
        "DDPM - Noise Schedules",
        parent_names=["DDPM - UDL"],
        base_radius=7,
    )
    # endregion

    # region Diffusion Papers
    M.add(
        "Diffusion Forcing",
        parent_names=["Diffusion Models"],
        base_radius=7,
    )
    M.add(
        "Diffusion Beats GANs",
        parent_names=["Diffusion Models"],
        base_radius=7,
    )
    M.add(
        "History Guidance",
        parent_names=["Diffusion Forcing"],
        base_radius=7,
    )
    M.add(
        "DiT",
        parent_names=["Diffusion Models"],
        base_radius=7,
    )
    M.add(
        "Edify Image",
        parent_names=["Diffusion Models"],
        base_radius=2,
    )
    # endregion

    # region Diffusion Posts
    M.add(
        "Understanding Diffusion Models: A Unified Perspective",
        parent_names=["Diffusion Models"],
        base_radius=20,
    )
    M.add(
        "Score Based Generative Models",
        parent_names=["Diffusion Models"],
        base_radius=10,
    )
    M.add(
        "Generative Modeling Using SDEs",
        parent_names=["Score Based Generative Models"],
        base_radius=10,
    )
    M.add(
        "Wiener Process",
        parent_names=[
            "Generative Modeling Using SDEs",
        ],
        base_radius=5,
    )
    M.add(
        "DDIM",
        parent_names=["Diffusion Models"],
        base_radius=7,
    )
    M.add(
        "Elucidated Diffusion Models",
        parent_names=["Diffusion Models"],
        base_radius=10,
    )
    # endregion

    # region Representation Learning
    M.add("Representation Learning", parent_names=["Deep Learning"], base_radius=3)
    M.add(
        "Contrastive Learning",
        parent_names=["Representation Learning"],
        base_radius=10,
    )
    # endregion

    # region Audio
    M.add("Audio", color="#3FFF57")
    M.add(
        "DiffWave",
        parent_names=["Audio", "Diffusion Models"],
        base_radius=7,
    )
    M.add("DAC", parent_names=["Audio"], base_radius=7)
    # endregion

    # region Vision
    M.add("Vision", color="#79443B")
    # endregion

    # region 3D Reconstruction
    M.add(
        "3D Reconstruction",
        parent_names=["Vision"],
        base_radius=7,
    )
    M.add(
        "Gaussian Splatting",
        parent_names=["3D Reconstruction"],
        base_radius=7,
    )
    M.add(
        "NeRF",
        parent_names=["3D Reconstruction"],
        base_radius=7,
    )
    # endregion

    # region Vision Papers
    M.add(
        "VAR",
        parent_names=["Vision", "Generative Modeling"],
        base_radius=7,
    )
    M.add(
        "PixelVAE",
        parent_names=["Generative Modeling", "Vision"],
        base_radius=7,
    )
    # endregion

    # region Advances in Computer Vision
    M.add(
        "Advances In Computer Vision",
        parent_names=["Vision"],
        base_radius=20,
    )
    M.add(
        "Image Formation",
        parent_names=["Advances In Computer Vision"],
        base_radius=5,
    )
    M.add(
        "Linear Image Processing",
        parent_names=["Advances In Computer Vision"],
        base_radius=5,
    )
    # endregion

    # region Language
    M.add(
        "Language Modeling",
        parent_names=["Deep Learning"],
        color="#00FF00",
    )
    M.add(
        "LLMs",
        parent_names=["Language Modeling"],
        base_radius=3,
    )
    M.add(
        "Byte-Pair Encoding",
        parent_names=["Language Modeling"],
        base_radius=3,
    )
    M.add(
        "Language Modeling from Scratch",
        parent_names=["Language Modeling"],
        base_radius=10,
    )
    # endregion

    # region Computer Science
    M.add("Computer Science", color="#212129")
    M.add(
        "Linked Lists",
        parent_names=["Computer Science"],
        base_radius=7,
    )

    M.add("Software", parent_names=["Computer Science"])

    M.add(
        "Filesystems",
        parent_names=["Software"],
        base_radius=1,
    )
    M.add(
        "Python",
        parent_names=["Software"],
        base_radius=1,
    )
    M.add(
        "Hydra",
        parent_names=["Python"],
        base_radius=2,
    )
    M.add(
        "PyTorch",
        parent_names=["Python"],
        base_radius=5,
    )
    M.add(
        "Autograd",
        parent_names=["PyTorch"],
        base_radius=5,
    )
    M.add(
        "Slurm",
        parent_names=["Software"],
        base_radius=2,
    )
    M.add(
        "Vector Operations",
        parent_names=["Software"],
    )
    M.add(
        "Einsum",
        parent_names=["Vector Operations"],
        base_radius=7,
    )

    # endregion

    # region Signal Processing
    M.add("Signal Processing", color="#a8326f")
    M.add(
        "DDSP",
        parent_names=["Signal Processing", "Deep Learning"],
        base_radius=7,
    )
    M.add(
        "PQMF",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add(
        "Downsampling and Stretching",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add(
        "Convolution",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add(
        "Transpose Convolution",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add(
        "Discrete Fourier Transform",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add(
        "Fourier Dualities",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add(
        "Pink Frequency Profiles",
        parent_names=["Signal Processing"],
        base_radius=7,
    )
    M.add(
        "1f Noise in Music and Speech",
        parent_names=["Pink Frequency Profiles"],
        base_radius=7,
    )
    # endregion

    # region ML systems
    M.add(
        "ML Systems",
        parent_names=["Software", "Deep Learning"],
        base_radius=0,
    )
    M.add(
        "Mixed Precision",
        parent_names=["ML Systems"],
        base_radius=7,
    )
    M.add(
        "Wandb",
        parent_names=["ML Systems"],
        base_radius=5,
    )
    M.add(
        "PyTorch",
        parent_names=["ML Systems", "Python"],
        base_radius=10,
    )
    M.add(
        "Lightning",
        parent_names=["PyTorch"],
        base_radius=5,
    )
    M.add(
        "Large Scale Deep Learning",
        parent_names=["ML Systems"],
        base_radius=7,
    )
    M.add(
        "Large Scale Deep Learning",
        parent_names=["ML Systems"],
        base_radius=5,
    )
    M.add(
        "Webdataset",
        parent_names=["Large Scale Deep Learning"],
        base_radius=5,
    )
    M.add(
        "Distributed Training",
        parent_names=["Large Scale Deep Learning", "Training"],
        base_radius=7,
    )
    # endregion

    # region Reinforcement Learning
    M.add("Reinforcement Learning", color="#808080")
    M.add(
        "Imitation Learning",
        parent_names=["Reinforcement Learning"],
        base_radius=7,
    )
    M.add(
        "ReaLChords",
        parent_names=["Reinforcement Learning"],
        base_radius=7,
    )
    M.add(
        "CS 285",
        parent_names=["Reinforcement Learning"],
        base_radius=10,
    )
    M.add(
        "Actor Critic",
        parent_names=["CS 285"],
        base_radius=7,
    )
    M.add(
        "Policy Gradient",
        parent_names=["CS 285"],
        base_radius=7,
    )

    M.add(
        "Generalized Advantage Estimation",
        parent_names=["Actor Critic"],
        base_radius=7,
    )
    M.add(
        "RLOO",
        parent_names=["Reinforcement Learning"],
        base_radius=7,
    )
    # endregion
    M.render()

    # region normalization
    M.add(
        "Normalization",
        parent_names=["Architecture"],
        base_radius=7,
    )
    M.add(
        "Batchnorm",
        parent_names=["Normalization"],
        base_radius=3,
    )
    M.add(
        "GroupNorm",
        parent_names=["Normalization"],
        base_radius=3,
    )
    M.add(
        "InstanceNorm",
        parent_names=["Normalization"],
        base_radius=3,
    )
    M.add(
        "LayerNorm",
        parent_names=["Normalization"],
        base_radius=3,
    )
    M.add(
        "RMSNorm",
        parent_names=["Normalization"],
        base_radius=3,
    )
    # endregion

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
    if len(unassigned_notes) > 0:
        raise LookupError(f"Unassigned Notes: {unassigned_notes}")

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

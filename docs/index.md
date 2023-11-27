---
layout: default
---

## Image Cropping under Design Constraints

<img src = "https://github.com/CyberAgentAILab/image_cropping_under_design_constraints/blob/main/example/abstract.jpg?raw=true" title = "proposed_method">



Takumi Nishiyasu<sup>1</sup>, Wataru Shimoda<sup>2</sup>, Yoichi Sato<sup>1</sup>  
<sup>1</sup>The University of Tokyo, <sup>2</sup> CyberAgent.Inc  

### Abstruct
Image cropping is essential in image editing for obtaining a compositionally enhanced image. In display media, image cropping is a prospective technique for automatically creating media content. However, image cropping for media contents is often required to satisfy various constraints, such as an aspect ratio and blank regions for placing texts or objects. We call this problem image cropping under design constraints. To achieve image cropping under design constraints, we propose a score function-based approach, which computes scores for cropped results whether aesthetically plausible and satisfies design constraints. We explore two derived approaches, a proposal-based approach, and a heatmap-based approach, and we construct a dataset for evaluating the performance of the proposed approaches on image cropping under design constraints. In experiments, we demonstrate that the proposed approaches outperform a baseline, and we observe that the proposal-based approach is better than the heatmap-based approach under the same computation cost, but the heatmap-based approach leads to better scores by increasing computation cost. The experimental results indicate that balancing aesthetically plausible regions and satisfying design constraints is not a trivial problem and requires sensitive balance, and both proposed approaches are reasonable alternatives.

### Overview of the proposed model
<img src = "https://github.com/CyberAgentAILab/image_cropping_under_design_constraints/blob/main/example/approach2.jpg?raw=true" title = "proposed_method">


### Results1: visual comparison
<img src = "https://github.com/CyberAgentAILab/image_cropping_under_design_constraints/blob/main/example/supplimental_comparison.jpg?raw=true" title = "result1">

### Results2: visual comparision under several design constraints
<img src = "https://github.com/CyberAgentAILab/image_cropping_under_design_constraints/blob/main/example/supplemental_fig_results2.jpg?raw=true" title = "result2">


### Application
<img src = "https://github.com/CyberAgentAILab/image_cropping_under_design_constraints/blob/main/example/application.jpg?raw=true" title = "application">

### Citation

```bibtex

```

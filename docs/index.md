---
layout: default
---

## Image Cropping under Design Constraints

![Concept](https://raw.githubusercontent.com/CyberAgentAILab/image_cropping_under_design_constraints/dev-nishiyasu/example/abstract.png)

Takumi Nishiyasu<sup>1</sup>, Wataru Shimoda<sup>2</sup>, Yoichi Sato<sup>1</sup>  
<sup>1</sup>The University of Tokyo, <sup>2</sup> CyberAgent.Inc  

### Abstruct
Image cropping is essential in image editing for obtaining a compositionally enhanced image. In display media, image cropping is a prospective technique for automatically creating media content. However, image cropping for media contents is often required to satisfy various constraints, such as an aspect ratio and blank regions for placing texts or objects. We call this problem image cropping under design constraints. To achieve image cropping under design constraints, we propose a score function-based approach, which computes scores for cropped results whether aesthetically plausible and satisfies design constraints. We explore two derived approaches, a proposal-based approach, and a heatmap-based approach, and we construct a dataset for evaluating the performance of the proposed approaches on image cropping under design constraints. In experiments, we demonstrate that the proposed approaches outperform a baseline, and we observe that the proposal-based approach is better than the heatmap-based approach under the same computation cost, but the heatmap-based approach leads to better scores by increasing computation cost. The experimental results indicate that balancing aesthetically plausible regions and satisfying design constraints is not a trivial problem and requires sensitive balance, and both proposed approaches are reasonable alternatives.

### Overview of the proposed model
![Concept](https://raw.githubusercontent.com/CyberAgentAILab/derendering-text/master/example/model.png)

### Optimization via differentiable text rendering
<div align = 'center'>
<img src = "https://raw.githubusercontent.com/CyberAgentAILab/derendering-text/master/example/sample.jpg" title = "inp" height = "350" >
<img src = "https://raw.githubusercontent.com/CyberAgentAILab/derendering-text/master/example/opt.gif" title = "opt" height = "350" >
</div>

### Text edit Demo
<div align = 'center'>
<img src = "https://raw.githubusercontent.com/CyberAgentAILab/derendering-text/master/example/edit0.gif" title = "edit0" height = "400" >
<img src = "https://raw.githubusercontent.com/CyberAgentAILab/derendering-text/master/example/edit1.gif" title = "edit1" height = "400" >
</div>

### Results1
<img src = "https://raw.githubusercontent.com/CyberAgentAILab/derendering-text/master/example/rec0.png" title = "edit0">

### Results2
<img src = "https://raw.githubusercontent.com/CyberAgentAILab/derendering-text/master/example/rec1.png" title = "edit1">

### Citation

```bibtex
@InProceedings{Shimoda_2021_ICCV,
    author    = {Shimoda, Wataru and Haraguchi, Daichi and Uchida, Seiichi and Yamaguchi, Kota},
    title     = {De-Rendering Stylized Texts},
    booktitle = {Proceedings of the IEEE/CVF International Conference on Computer Vision (ICCV)},
    month     = {October},
    year      = {2021},
    pages     = {1076-1085}
}
```

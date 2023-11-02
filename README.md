## Paper: Image Cropping under Design Constraints


Takumi Nishiyasu<sup>1</sup>, Wataru Shimoda<sup>2</sup>,  Yoichi Sato<sup>1</sup>  
<sup>1</sup>Tokyo University, <sup>2</sup> CyberAgent.Inc

Accepted to ACMMM Asia 2023.
[[Publication](https://arxiv.org/abs/2310.08892)]
[[Arxiv](https://arxiv.org/abs/2310.08892)]
[[project-page](https://cyberagentailab.github.io/image_cropping_under_design_constraints/)]

## Introduction
This repository contains the codes for ["Image Cropping under Design Constraints"](https://arxiv.org/abs/2310.08892).
### Concept
We propose to parse rendering parameters of stylized texts utilizing a neural net.
<img src = "example/abstract.png" title = "rec" >



## Installation

### Requirements
- Python >= 3.7
- Pytorch >= 1.8.1
- torchvision >= 0.9.1

```bash
pip install -r requirements.txt
```

### Evaluation data
- The evaluation dataset is in [here](/data/FLMS_blank_aspect.json) 
- Locate the json file in `data/FLMS_blank_aspect.json`



## Usage

### Test
- Download the pre-trained weight from this link
([weight](https://drive.google.com/file/d/1HBcfV0nfSluCWCHGgGerx7QNJZJpOv3h/view?usp=sharing)).  
- Locate the weight file in `weights/font100_unified.pth`.  

Example usage.
```bash
python test.py --imgfile=example/sample.jpg
```
Note
- imgfile option: path of an input image
- results would be generated in `res/`


## Todo
- [ ] Link of dataset
- [ ] Testing codes

## Reference
```bibtex

```

## Contact
This repository is maintained by Takumi Nishiyasu(nishiyasu-takumi[at]cyberagent.co.jp).

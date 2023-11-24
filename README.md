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

FLMS_blank_aspect.json
```
{
    "1011366896_Large-0-1_0158730158730158.png": {
      "image_name": "1011366896_Large.jpg",
      "aspect_ratio": "1.0158730158730158",
      "blank_space_index": 0,
      "blank_space": [
        0,
        0,
        512,
        384
      ],
      "blank_aspect_bbox": [
        0,
        0,
        756,
        768
      ]
    },
    "1011366896_Large-1-0_750816104461371.png": {...},
    
    ...

    "IMG_6266-4-0_6805708013172338.png": {
      "image_name": "IMG_6266.jpg",
      "aspect_ratio": "0.6805708013172338",
      "blank_space_index": 4,
      "blank_space": [
        0,
        170,
        128,
        682
      ],
      "blank_aspect_bbox": [
        0,
        77,
        911,
        697
      ]
    }
}
```

## Todo
- [ ] Link of dataset
- [ ] Testing codes

## Reference
```bibtex

```

## Contact
This repository is maintained by Takumi Nishiyasu(nishiyasu_takumi[at]cyberagent.co.jp).

## Paper: Image Cropping under Design Constraints

This repository contains the codes for ["Image Cropping under Design Constraints"](https://arxiv.org/abs/2310.08892).

Takumi Nishiyasu<sup>1</sup>, Wataru Shimoda<sup>2</sup>,  Yoichi Sato<sup>1</sup>  
<sup>1</sup>Tokyo University, <sup>2</sup> CyberAgent.Inc

Accepted to ACMMM Asia 2023.
[[Publication](https://arxiv.org/abs/2310.08892)]
[[Arxiv](https://arxiv.org/abs/2310.08892)]
[[project-page](https://cyberagentailab.github.io/image_cropping_under_design_constraints/)]


<img src = "example/abstract.png" title = "rec" >


## Evaluation data
- The evaluation dataset is in [here](/data/FLMS_blank_aspect.json) 
- Locate the json file in `data/FLMS_blank_aspect.json`


- FLMS_blank_aspect.json
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


## Test

- Test the performance of Heatmap-based approach (iter_size = 100) 

    ```bash
    python test.py 
    ```


- predictions.csv
    - image file name, predicted bounding box [x1,y1,x2,y2], ground truth bounding box [x1,y1,x2,y2], layout bounding box [x1,y1,x2,y2]
    ```
    1011366896_Large.jpg,"[[0, 0, 768, 768]]","[[0.0, 0.0, 756.0, 768.0]]","[[0.0, 0.0, 512.0, 384.0]]"

    1011366896_Large.jpg,"[[0, 0, 1024, 757]]","[[105.0, 0.0, 1024.0, 690.0]]","[[512.0, 0.0, 1024.0, 384.0]]"

    ...

    IMG_6266.jpg,"[[0, 96, 941, 736]]","[[0.0, 77.0, 911.0, 697.0]]","[[0.0, 170.0, 128.0, 682.0]]"
    ```

## Reference
```bibtex

```

## Contact
This repository is maintained by Takumi Nishiyasu(nishiyasu_takumi[at]cyberagent.co.jp).

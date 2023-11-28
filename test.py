import argparse
import numpy as np
import pandas as pd


def compute_iou(gt_crop, pre_crop):
    gt_crop = gt_crop[gt_crop[:, 0] >= 0]
    zero_array = np.zeros(gt_crop.shape[0])
    over_x1 = np.maximum(gt_crop[:, 0], pre_crop[:, 0])
    over_y1 = np.maximum(gt_crop[:, 1], pre_crop[:, 1])
    over_x2 = np.minimum(gt_crop[:, 2], pre_crop[:, 2])
    over_y2 = np.minimum(gt_crop[:, 3], pre_crop[:, 3])
    over_w = np.maximum(zero_array, over_x2 - over_x1)
    over_h = np.maximum(zero_array, over_y2 - over_y1)
    inter = over_w * over_h
    area1 = (gt_crop[:, 2] - gt_crop[:, 0]) * (gt_crop[:, 3] - gt_crop[:, 1])
    area2 = (pre_crop[:, 2] - pre_crop[:, 0]) * (pre_crop[:, 3] - pre_crop[:, 1])
    union = area1 + area2 - inter
    iou = inter / union

    iou_idx = np.argmax(iou)
    return iou[iou_idx]


def string_to_ndarray(string_input):
    list_input = eval(string_input)
    ndarray_output = np.array(list_input, dtype=int)
    return ndarray_output


def test(pred_file):
    df = pd.read_csv(pred_file, header=None)
    ious = []
    for _, row in df.iterrows():
        box1 = string_to_ndarray(row[1])
        box2 = string_to_ndarray(row[2])
        ious.append(compute_iou(box1, box2))
    print("IoUs:", np.mean(np.array(ious)))
    df["IoU"] = ious
    print(df.head())
    return ious


def main(args):
    test(pred_file=args.pred_file)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Test script")
    parser.add_argument(
        "--pred_file",
        required=False,
        default="data/predictions.csv",
        help="predictions of heatmap-based-approach",
        type=str,
    )
    args = parser.parse_args()
    main(args)

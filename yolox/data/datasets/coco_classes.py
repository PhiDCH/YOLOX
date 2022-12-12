#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

# COCO_CLASSES = (
#     "person",
#     "bicycle",
#     "car",
#     "motorcycle",
#     "airplane",
#     "bus",
#     "train",
#     "truck",
#     "boat",
#     "traffic light",
#     "fire hydrant",
#     "stop sign",
#     "parking meter",
#     "bench",
#     "bird",
#     "cat",
#     "dog",
#     "horse",
#     "sheep",
#     "cow",
#     "elephant",
#     "bear",
#     "zebra",
#     "giraffe",
#     "backpack",
#     "umbrella",
#     "handbag",
#     "tie",
#     "suitcase",
#     "frisbee",
#     "skis",
#     "snowboard",
#     "sports ball",
#     "kite",
#     "baseball bat",
#     "baseball glove",
#     "skateboard",
#     "surfboard",
#     "tennis racket",
#     "bottle",
#     "wine glass",
#     "cup",
#     "fork",
#     "knife",
#     "spoon",
#     "bowl",
#     "banana",
#     "apple",
#     "sandwich",
#     "orange",
#     "broccoli",
#     "carrot",
#     "hot dog",
#     "pizza",
#     "donut",
#     "cake",
#     "chair",
#     "couch",
#     "potted plant",
#     "bed",
#     "dining table",
#     "toilet",
#     "tv",
#     "laptop",
#     "mouse",
#     "remote",
#     "keyboard",
#     "cell phone",
#     "microwave",
#     "oven",
#     "toaster",
#     "sink",
#     "refrigerator",
#     "book",
#     "clock",
#     "vase",
#     "scissors",
#     "teddy bear",
#     "hair drier",
#     "toothbrush",
# )


from pycocotools.coco import COCO
coco = COCO("/home/robotic/Downloads/phidch_ws/src/bmw-lab/scripts/sordi-2022/data/SORDI/annotations/sordi-single-asserts-val100.json")
class_id = sorted(coco.getCatIds())
cats = coco.loadCats(coco.getCatIds())
cat_dict = {}
COCO_IDS = {}
for c in cats:
    cat_dict[c['id']] = c['name']
    COCO_IDS[c['name']] = c['id']
    
COCO_CLASSES = tuple([cat_dict[id] for id in class_id])

# print(COCO_IDS)

# COCO_CLASSES = ('stillage_close', 'stillage_open', 'l_klt_4147', 'l_klt_6147', 'l_klt_8210', 'locker', 'cabinet', 'cardboard_box', 'pallet', 'dolly', 'jack', 'spring_post', 'bicycle', 'forklift', 'str', 'exit_sign', 'fire_extinguisher')

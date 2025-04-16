import lmdb
import cv2
import numpy as np
import os
from PIL import Image
from io import BytesIO

env = lmdb.open("out_lmdb", readonly=True, lock=False)
with env.begin() as txn:
    n_samples = int(txn.get('num-samples'.encode()))
    for i in range(1, min(10, n_samples + 1)):
        index = f'{i:09d}'
        label_key = f'label-{index}'.encode()
        img_key = f'image-{index}'.encode()
        label = txn.get(label_key)
        img_bin = txn.get(img_key)

        if label:
            print(f"[{index}] → {label.decode('utf-8')}")
        else:
            print(f"[{index}] → (label missing!)")

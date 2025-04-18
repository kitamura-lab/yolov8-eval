# images/pose1.mp4の各フレームにおいて骨格を抽出し，ボーンを青色で動画に描画せよ．

import cv2
from ultralytics import YOLO
import torch
import sys

args = sys.argv

# video_path = "video/002b.mp4"
video_path = args[1]

model = YOLO("yolov8x-pose.pt")

# 骨格のリンク
links = [
    [5, 7],
    [6, 8],
    [7, 9],
    [8, 10],
    [11, 13],
    [12, 14],
    [13, 15],
    [14, 16],
    [5, 11],
    [6, 12],
    [5, 6],
    [11, 12],
]

cap = cv2.VideoCapture(video_path)

cnt = 0
while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model(frame)
        # print(results[0].orig_img)
        img = results[0].orig_img

        # print(len(results[0].keypoints.data))
        for data in results[0].keypoints.data:
            nodes = data[:, :2]
            if len(nodes) == 0:
                continue
            # print(nodes)
            # nodes = results[0].keypoints.data[0][:, :2]
            # print(nodes)

            for n1, n2 in links:
                # 誤認識のリンクを描画しない．
                if nodes[n1][0] * nodes[n1][1] * nodes[n2][0] * nodes[n2][1] == 0:
                    continue

                color = (255, 0, 255)
                cv2.line(
                    img,
                    # 2つの座標を整数化し，テンソルからリストにする．
                    nodes[n1].to(torch.int).tolist(),
                    nodes[n2].to(torch.int).tolist(),
                    color,
                    thickness=2,
                )

        cv2.imshow("", img)
        
        if cv2.waitKey(1) == 27:
            break
    else:
        break
    cnt = cnt + 1

cap.release()
cv2.destroyAllWindows()

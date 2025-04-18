# images/object1.mp4の各フレームにおいて人物領域を抽出し，動画に描画せよ．
import cv2
from ultralytics import YOLO
import sys

args = sys.argv

# video_path = "video/002c.MP4"
video_path = args[1]
# model = YOLO("yolov9e.pt")

model = YOLO("yolov8x.pt")

cap = cv2.VideoCapture(video_path)

cnt = 0
num = 0
while cap.isOpened():
    success, frame = cap.read()

    if success:
        results = model(frame)

        annotated_frame = results[0].orig_img
        boxes = results[0].boxes
        size = 0

        for box in boxes:
            x1 = int(box.data[0][0])
            y1 = int(box.data[0][1])
            x2 = int(box.data[0][2])
            y2 = int(box.data[0][3])
            id = int(box.data[0][5])
            if id == 0:
                cv2.rectangle(
                    annotated_frame,
                    (x1, y1),
                    (x2, y2),
                    (0, 0, 255),
                    thickness=3,
                )
        cv2.imshow("", annotated_frame)
        # print(len(boxes))
        cnt += len(boxes)
        num += 1

        if cv2.waitKey(1) == 27:
            break
    else:
        break

# print(cnt / num)

cap.release()
cv2.destroyAllWindows()

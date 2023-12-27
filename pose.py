import cv2
from ultralytics import YOLO


class Pose:
    def __init__(self, video_path):
        self.video_path = video_path
        # YOLOv8モデルをロード
        self.model = YOLO("yolov8x-pose.pt")

    def run(self):
        # ビデオファイルを開く
        cap = cv2.VideoCapture(self.video_path)

        # ビデオフレームをループする
        while cap.isOpened():
            # ビデオからフレームを読み込む
            success, frame = cap.read()

            if success:
                # フレームから骨格抽出
                results = self.model(frame)

                # フレームに結果を可視化
                annotated_frame = results[0].plot()

                # 注釈付きのフレームを表示
                cv2.imshow("", annotated_frame)

                # ESCが押されたらループから抜ける
                if cv2.waitKey(1) == 27:
                    break
            else:
                # ビデオの終わりに到達したらループから抜ける
                break

        # ビデオキャプチャオブジェクトを解放し、表示ウィンドウを閉じる
        cap.release()
        cv2.destroyAllWindows()

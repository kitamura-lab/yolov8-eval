import cv2
from ultralytics import YOLO
import time


class Pose:
    def eval(self):
        ut0 = time.time()

        # YOLOv8モデルをロード
        model = YOLO("yolov8x-pose.pt")

        # ビデオファイルを開く
        video_path = "single_short.mp4"
        cap = cv2.VideoCapture(video_path)

        # ビデオフレームをループする
        while cap.isOpened():
            # ビデオからフレームを読み込む
            success, frame = cap.read()

            if success:
                # フレームでYOLOv8トラッキングを実行し、フレーム間でトラックを永続化
                results = model(frame)

                # フレームに結果を可視化
                annotated_frame = results[0].plot()

                # 注釈付きのフレームを表示
                cv2.imshow("", annotated_frame)

                # 'q'が押されたらループから抜ける
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
            else:
                # ビデオの終わりに到達したらループから抜ける
                break

        # ビデオキャプチャオブジェクトを解放し、表示ウィンドウを閉じる
        cap.release()
        cv2.destroyAllWindows()

        ut1 = time.time()
        print("Time: {}".format(ut1 - ut0))  # 秒単位

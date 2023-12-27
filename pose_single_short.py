from pose import Pose
import time

video_path = "single_short.mp4"

start = time.time()

pose = Pose(video_path)
pose.run()

end = time.time()
print("Time: {}".format(end - start))  # 秒単位

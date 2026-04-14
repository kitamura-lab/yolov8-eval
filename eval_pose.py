from clock import Clock
from pose import Pose

# video_path = "single_short.mp4"
video_path = "single_long.mp4"

clock = Clock()
clock.start()

pose = Pose(video_path)
pose.run(True)

print("Time: {}".format(clock.stop()))  # 秒単位

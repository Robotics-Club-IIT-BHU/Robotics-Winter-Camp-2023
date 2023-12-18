import gym
import os
import cv2 as cv
import time as t
import pybullet as p
import pybullet_workshop_23

CAR_LOCATION = [3,0,1.5]
# BALL_LOCATION = [-3,0,1.5]
# HUMANOID_LOCATION = [6,7,1.5]
VISUAL_CAM_SETTINGS = dict({
    'cam_dist'       : 13,
    'cam_yaw'        : 0,
    'cam_pitch'      : -110,
    'cam_target_pos' : [0,4,0]
})

os.chdir(os.path.dirname(os.getcwd()))

env = gym.make('pybullet_workshop_23',
    arena = "default",
    car_location=CAR_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)

while True:
    img = env.get_image(cam_height=0, dims=[512,512])
    cv.imshow("img", img)
    k = cv.waitKey(1)
    if k==ord('q'):
        break
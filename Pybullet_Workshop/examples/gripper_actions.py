import gym
import os
import cv2 as cv
import time as t
import pybullet as p
import pybullet_workshop_23

CAR_LOCATION = [3,0,1.5]
BALL_LOCATION = [-3,0,1.5]
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
    ball_location=BALL_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)

env.open_grip()
env.move(vels=[[6,6],
               [6,6]])
t.sleep(3.5)
env.move(vels=[[0,0],
               [0,0]])
env.close_grip()
t.sleep(1)
env.move(vels=[[-2,-2],
               [-2,-2]])

t.sleep(2)
env.move(vels=[[0,0],
               [0,0]])
env.open_grip()
t.sleep(2)

env.close()

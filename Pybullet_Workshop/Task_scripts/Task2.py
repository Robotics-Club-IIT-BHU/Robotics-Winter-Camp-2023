## Library Imports :: ---
import gym
import os
import cv2
import time as t
import numpy as np
import pybullet_workshop_23


CAR_LOCATION = [3,0,1.5]

BALL_LOCATION = [-3,0,1.5]

HUMANOID_LOCATION = [6,7,1.5]

VISUAL_CAM_SETTINGS = dict({
    'cam_dist'       : 13,
    'cam_yaw'        : 0,
    'cam_pitch'      : -110,
    'cam_target_pos' : [0,4,0]
})

##########################################################
"""
Your Task is to grab the ball that is in front of the husky and then find the humanoid and shoot the ball.
Your code should be using opencv to autonomously grab the ball and shoot.
"""
##########################################################

os.chdir(os.path.dirname(os.getcwd()))
# Environment Setup ::---
env = gym.make('pybullet_workshop_23',
               arena="arena2",
               car_location=CAR_LOCATION,
               ball_location=BALL_LOCATION,
               humanoid_location=HUMANOID_LOCATION,
               visual_cam_settings=VISUAL_CAM_SETTINGS
               )

###################### Write your code from here ###########################
while True:
    img = env.get_image(cam_height=0, dims=[512,512])
    k = cv2.waitKey(100)
    if k == ord('q'):
        break
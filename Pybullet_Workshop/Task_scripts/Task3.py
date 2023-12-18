## Library Imports :: ---

## Library Imports :: ---
import gym
import os
import pybullet_workshop_23
import cv2

CAR_LOCATION = [-0.7,8.5,1.5]
# BALL_LOCATION = [4,5,1.5]
# HUMANOID_LOCATION = [-3,-4,1.3]
VISUAL_CAM_SETTINGS = dict({
    'cam_dist'       : 13,
    'cam_yaw'        : 0,
    'cam_pitch'      : -110,
    'cam_target_pos' : [0,4,0]
})

##########################################################
"""
Your task is to make husky follow the red line autonomously using opencv and PID control.
This is BONUS TASK.
"""
##########################################################



os.chdir(os.path.dirname(os.getcwd()))
# Environment Setup ::---

env = gym.make('pybullet_workshop_23',
    arena = "arena1",
    car_location=CAR_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)


###################### Write your code from here ###########################

while True:
    img = env.get_image(cam_height=0, dims=[512,512])
    k = cv2.waitKey(100)
    if k == ord('q'):
        break
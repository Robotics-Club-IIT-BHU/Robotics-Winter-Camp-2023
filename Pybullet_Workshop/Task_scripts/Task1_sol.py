## Library Imports :: ---
import gym
import os
import time as t
import pybullet as p
import pybullet_workshop_23

CAR_LOCATION = [2,3,1.5]
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
Your task is to use env.move() and p.getKeyboardEvents() to control the husky using the arrow keys
of you keyboard and make the husky stop when the spacebar is pressed (like games :D

"""
##########################################################

os.chdir(os.path.dirname(os.getcwd()))

#Environment Setup ::---
env = gym.make('pybullet_workshop_23',
    arena = "default",
    car_location=CAR_LOCATION,
    visual_cam_settings=VISUAL_CAM_SETTINGS
)


###################### Write your code from here ###########################

vel=[[0,0],
     [0,0]]
while True:
    p.stepSimulation()
    keys = p.getKeyboardEvents()


    if p.B3G_UP_ARROW in keys and keys[p.B3G_UP_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] += 0.3
            a[1] += 0.3
        env.move(vels=vel)

    elif p.B3G_LEFT_ARROW in keys and keys[p.B3G_LEFT_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] -= 0.1
            a[1] += 0.1
        env.move(vels=vel)

    elif p.B3G_DOWN_ARROW in keys and keys[p.B3G_DOWN_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] -= 0.4
            a[1] -= 0.4
        env.move(vels=vel)

    elif p.B3G_RIGHT_ARROW in keys and keys[p.B3G_RIGHT_ARROW] & p.KEY_IS_DOWN:
        for a in vel:
            a[0] += 0.1
            a[1] -= 0.1
        env.move(vels=vel)

    elif 32 in keys and keys[32] & p.KEY_IS_DOWN:
        vel = [[0, 0],
               [0, 0]]
        env.move(vels=vel)
    else:
        pass
    t.sleep(0.1)
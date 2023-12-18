import gym
import os
import time as t
import pybullet as p
import pybullet_workshop_23

os.chdir(os.path.dirname(os.getcwd()))

env = gym.make('pybullet_workshop_23',
    arena = "default",
    car_location=[2,0,1.5]
)

env.move(vels=[[2,2],
               [2,2]])
t.sleep(2)
env.move(vels=[[-2,2],
               [-2,2]])
t.sleep(2)
env.move(vels=[[-2,-2],
               [-2,-2]])
t.sleep(2)
env.close()
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


#### Functions :: ---
def wait(time=1):
    t.sleep(time)


def open():
    env.open_grip()


def stop(time=1):
    wait(time)
    env.move(vels=[[0, 0], [0, 0]])


def close():
    env.close_grip()


def shoot(hit=1000):
    env.shoot(hit)


def move(mode='f', speed=5):
    if mode.lower() == "f":
        mat = [[speed, speed], [speed, speed]]
    elif mode.lower() == "r":
        mat = [[speed, -speed], [speed, -speed]]
    else:
        print("Error Occurred , Unexpected mode in Move Function.")
        return "Error"
    env.move(vels=mat)


def isBall(cnt):
    area = cv2.contourArea(cnt) if cv2.contourArea(cnt) != 0 else 1
    x, y, w, h = cv2.boundingRect(cnt)
    return (True if (1.1 < w * h / area < 1.5) else False) if (0.85 < w / h < 1.2) else False


def MoveHold(cnt):
    x, y, w, h = cv2.boundingRect(cnt)
    x = x + w / 2
    if x > 330:
        move('r', (330 - x) / 30)
    elif x < 270:
        move('r', (270 - x) / 30)
    else:
        move('f', 10)
        area = cv2.contourArea(cnt)
        if area > 40000:
            global Holding
            stop(.2)
            close()
            stop(.25)
            Holding = True


def MoveShoot(cnt):
    if len(contours) != 1:
        x, y, w, h = cv2.boundingRect(cnt)
        x = x + w / 2
        if x > 301:
            move('r', (301 - x) / 30)
        elif x < 299:
            move('r', (299 - x) / 30)
        else:
            global End
            stop(.1)
            open()
            shoot()
            wait(2)
            End = True
    else:
        move('r')


def Findcontour(img, lowerRange, UpperRange):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lowerRange, UpperRange)
    res = cv2.bitwise_and(img, img, mask=mask)
    imgray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    return contours


"""Solution Goes here ..."""

## setup

open()
Holding = False
humanoid = False
End = False
move('r', 10)

### Loop

while True:
    img = env.get_image(cam_height=0, dims=[600, 600])
    img = cv2.flip(img, 5)
    # range of RED color in HSV
    lower_color = np.array([0, 50, 50], dtype=np.uint8)
    upper_color = np.array([10, 255, 255], dtype=np.uint8)
    #####
    contours = Findcontour(img, lower_color, upper_color)
    # cv2.drawContours(img,contours,-1,(0,255,0),2) ### uncomment to draw contours
    cv2.imshow("image",img)
    sorted(contours, key=cv2.contourArea)

    if contours:
        cnt = contours[-1]
        if not Holding:
            if isBall(cnt):
                MoveHold(cnt)
        elif End:
            break
        else:
            if humanoid:
                MoveShoot(cnt)
            elif len(contours) > 1:
                humanoid = True
            elif not humanoid:
                move('r')
    else:
        move('r')

    ### Contour detected Image
    # cv2.imshow('Contour Detection',img) ##Un-Comment to see image with detected Contour

    #### Termination Condition
    k = cv2.waitKey(1)
    if k == ord('q'):
        break
t.sleep(3)
cv2.destroyAllWindows()

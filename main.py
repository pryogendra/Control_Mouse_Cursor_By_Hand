from time import sleep
import cv2 as cv
import numpy as np
import pyautogui as pyg

def mouse_move(x, y):
    screen_w, screen_h = pyg.size()
    camera_w = capture.get(cv.CAP_PROP_FRAME_WIDTH)
    camera_h = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
    move_x = int((cx / camera_w) * screen_w)
    move_y = int((cy / camera_h) * screen_h)
    pyg.moveTo(move_x, move_y)


cx = cy = x = y = 0
capture = cv.VideoCapture(0)
capture.set(cv.CAP_PROP_FRAME_WIDTH, 20)
capture.set(cv.CAP_PROP_FRAME_HEIGHT, 20)
pyg.FAILSAFE = False
try:
    #Red
    lower_color_red = np.array([1, 120, 70])  #Red[0-10]
    upper_color_red = np.array([5, 255, 255])
    lower_color_yellow = np.array([25, 100, 70])  #Yellow[25-35]
    upper_color_yellow = np.array([30, 255, 255])
    #Green
    lower_color_green = np.array([35, 100, 70])  #Green[35-85]
    upper_color_green = np.array([45, 255, 255])

    while True:
        _, f = capture.read()
        frame = cv.flip(f, 1)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        mask_green = cv.inRange(hsv, lower_color_green, upper_color_green)
        mask_yellow = cv.inRange(hsv, lower_color_yellow, upper_color_yellow)
        mask_red = cv.inRange(hsv, lower_color_red, upper_color_red)
        contours_green, _ = cv.findContours(mask_green, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours_yellow, _ = cv.findContours(mask_yellow, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        contours_red, _ = cv.findContours(mask_red, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        point_yellow = []
        points = ['yellow', 'green', 'red']  #Store the points

        for g in contours_green:
            if cv.contourArea(g) > 100:
                moment = cv.moments(g)
                if moment['m00'] != 0:
                    x1 = int(moment["m10"] / moment["m00"])
                    y1 = int(moment["m01"] / moment["m00"])
                    cx = x1
                    cy = y1
                    cv.circle(frame, (cx, cy), 5, (0, 255, 0), -1)
                    points[1] = 'g'
        for r in contours_red:
            if cv.contourArea(r) > 100:
                points[2] = 'r'
                moment = cv.moments(r)
                if moment['m00'] != 0:
                    x1 = int(moment["m10"] / moment["m00"])
                    y1 = int(moment["m01"] / moment["m00"])
                    cx = x1
                    cy = y1
                    cv.circle(frame, (cx, cy), 5, (0, 0, 255), -1)
        for y in contours_yellow:
            if cv.contourArea(y) > 100:
                moment = cv.moments(y)
                if moment['m00'] != 0:
                    x1 = int(moment["m10"] / moment["m00"])
                    y1 = int(moment["m01"] / moment["m00"])
                    if x1 % 2 == 0 and y1 % 2 == 0:
                        cx = x1
                        cy = y1
                    point_yellow.append((cx, cy))
                    points[0] = 'y'
                    cv.circle(frame, (cx, cy), 5, (0, 255, 255), -1)

        if points[0] == 'y':
            mouse_move(point_yellow[0][0], point_yellow[0][1])
        if points[1] == 'g':
            if points[0] == 'y':
                pyg.click()
        if points[2] == 'r':
            if points[1] == 'g':
                pyg.scroll(3)
                sleep(0.2)
            else:
                pyg.scroll(-3)

        cv.imshow("Live Video", frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
except Exception as e:
    print(e)
    cv.destroyAllWindows()

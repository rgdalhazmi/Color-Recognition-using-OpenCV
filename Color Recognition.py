import cv2
import numpy as np

image = cv2.imread("apple.png")
image = cv2.resize(image, (600, 600))

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

lower_red1 = np.array([0, 120, 70])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 120, 70])
upper_red2 = np.array([180, 255, 255])

lower_green = np.array([40, 70, 70])
upper_green = np.array([80, 255, 255])

lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

red_mask = cv2.inRange(hsv, lower_red1, upper_red1) + cv2.inRange(hsv, lower_red2, upper_red2)
green_mask = cv2.inRange(hsv, lower_green, upper_green)
blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

if cv2.countNonZero(red_mask) > 500:
    text = "RED"
elif cv2.countNonZero(green_mask) > 500:
    text = "GREEN"
elif cv2.countNonZero(blue_mask) > 500:
    text = "BLUE"
else:
    text = "UNKNOWN"

print("Detected color:", text)

cv2.putText(image, text, (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (255, 255, 255), 4)
cv2.putText(image, text, (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX, 1,
            (0, 0, 0), 2)

cv2.imshow("Color Recognition", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
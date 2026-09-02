import cv2

img = cv2.imread("sample_frame.jpg")
points = []

def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))
        print(f"Point {len(points)}: ({x}, {y})")
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)
        cv2.imshow("Click 4 corners of queue region", img)

cv2.imshow("Click 4 corners of queue region", img)
cv2.setMouseCallback("Click 4 corners of queue region", click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\nFinal queue_region:")
print(points)
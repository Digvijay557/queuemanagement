import cv2
from ultralytics import solutions

cap = cv2.VideoCapture(0)
assert cap.isOpened(), "Error accessing camera"

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS)) or 20

video_writer = cv2.VideoWriter("queue_management_live.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# Your calibrated queue region
queue_region = [(49, 284), (620, 283), (624, 346), (53, 334)]

queuemanager = solutions.QueueManager(
    show=True,
    model="yolo26n.pt",
    region=queue_region,
)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Failed to grab frame from camera.")
        break

    results = queuemanager(im0)
    video_writer.write(results.plot_im)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()
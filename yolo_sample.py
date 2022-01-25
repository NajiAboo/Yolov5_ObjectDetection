from unittest import result
import torch
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
img = 'zidane.jpg'

results = model(img)
#print("result", results)
print(results.pandas().xyxy[0])
results.show()
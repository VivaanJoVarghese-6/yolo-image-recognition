from ultralytics import YOLO
from PIL import Image
 
# Load the pre-trained model (downloads on first run)
model = YOLO('yolov8n.pt')
 
# Run detection on your image
results = model('bus.jpg')
 
# Show and save results
for result in results:
    result.show()
    result.save(filename='bus1.jpg')
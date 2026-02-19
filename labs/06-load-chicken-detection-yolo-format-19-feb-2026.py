# On local machine
import fiftyone as fo

dataset = fo.Dataset("chicken-detection-yolo-format-19-feb-2026")

# Verify the data exists
print(f"Dataset has {len(dataset)} samples")
print(dataset)

session = fo.launch_app(dataset)  # (optional) port=XXXX

session.wait()
# On local machine
import fiftyone as fo
from fiftyone import ViewField as F

# Dataset name
name = "chicken-detection-dataset-yolo-format-19-feb-2026"

# Load existing dataset (do not delete, do not override)
dataset = fo.load_dataset(name)

# Verify the data exists
print(f"Dataset has {len(dataset)} samples")
print(dataset)

# Filter samples where possible_missing > 0
session = fo.launch_app(dataset)
session.view = dataset.match(F("possible_missing") > 0)
session.wait()

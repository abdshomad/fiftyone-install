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

# Filter labels in ground_truth field where mistakenness_loc > 0.85
session = fo.launch_app(dataset)
session.view = dataset.filter_labels("ground_truth", F("mistakenness_loc") > 0.85)
session.wait()

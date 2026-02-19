# On local machine
import fiftyone as fo
import fiftyone.brain as fob

# Dataset name
name = "chicken-detection-dataset-yolo-format-19-feb-2026"

# Load existing dataset (do not delete, do not override)
dataset = fo.load_dataset(name)

# Verify the data exists
print(f"Dataset has {len(dataset)} samples")
print(dataset)

# Compute mistakenness of annotations in `ground_truth` field using
# predictions from `predictions` field as point of reference
fob.compute_mistakenness(dataset, "yolo26n-best-14-feb-2026-predictions", label_field="ground_truth")

session = fo.launch_app(dataset)  # (optional) port=XXXX
session.wait()

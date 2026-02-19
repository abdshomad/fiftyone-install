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

# Sort by likelihood of mistake (most likely first)
mistake_view = dataset.sort_by("mistakenness", reverse=True)

# Print some information about the view
print(mistake_view)

# Launch app and show the samples we processed in rank order by the mistakenness
session = fo.launch_app(dataset)
session.view = mistake_view
session.wait()

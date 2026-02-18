import fiftyone as fo
import fiftyone.zoo as foz

dataset = foz.load_zoo_dataset("quickstart")

# Verify the data exists
print(f"Dataset has {len(dataset)} samples")
print(dataset)

session = fo.launch_app(dataset)
session.wait()
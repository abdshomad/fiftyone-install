MODEL_PATH = "chicken-detection-dataset-yolo-format-19-feb-2026/models/chicken-detection-model-v26n-best-14-feb-2026.pt"

# On local machine
import fiftyone as fo

# Path to the directory containing your YOLO dataset and data.yaml
dataset_dir = "chicken-detection-dataset-yolo-format-19-feb-2026"
name = "chicken-detection-dataset-yolo-format-19-feb-2026"

# Why do we need to delete the dataset if it exists?
# Because if the dataset exists, it will not be loaded correctly.
# We need to delete the dataset if it exists to reload with all splits.
# If the dataset does not exist, it will be created.
# If the dataset exists, it will be loaded correctly.
# Delete existing dataset if it exists (to reload with all splits)
try:
    fo.delete_dataset(name)
    print(f"Deleted existing dataset '{name}'")
except:
    pass  # Dataset doesn't exist, which is fine

# The splits to load
splits = ["train", "val"]

# Create the dataset as persistent with overwrite enabled
dataset = fo.Dataset(name, persistent=True, overwrite=True)

# Load each split and add to the dataset
for split in splits:
    print(f"Loading {split} split...")
    max_retries = 2
    retry_count = 0
    
    while retry_count < max_retries:
        try:
            dataset.add_dir(
                dataset_dir=dataset_dir,
                dataset_type=fo.types.YOLOv5Dataset,  # Use YOLOv5Dataset for v5 or v8
                split=split,
                tags=split,  # Tag samples with their split name for easy filtering
            )
            # Reload dataset reference to ensure state is fresh
            dataset.reload()
            print(f"Loaded {split} split. Total samples: {len(dataset)}")
            break  # Success, exit retry loop
        except (ValueError, Exception) as e:
            error_msg = str(e)
            # Handle case where dataset was deleted or state is corrupted
            if "is deleted" in error_msg or "does not exist" in error_msg.lower() or "Failed to update document" in error_msg:
                retry_count += 1
                if retry_count < max_retries:
                    print(f"Dataset state issue detected (attempt {retry_count}), reloading dataset...")
                    # Reload the dataset reference
                    try:
                        dataset = fo.load_dataset(name)
                    except:
                        # If reload fails, recreate (shouldn't happen but just in case)
                        dataset = fo.Dataset(name, persistent=True, overwrite=True)
                else:
                    raise
            else:
                # Different error, re-raise
                raise

# dataset = fo.Dataset("chicken-detection-dataset-yolo-format-19-feb-2026")

# Verify the data exists
print(f"Dataset has {len(dataset)} samples")
print(dataset)

# import fiftyone as fo
from ultralytics import YOLO

model = YOLO(MODEL_PATH)

dataset = fo.load_dataset("chicken-detection-dataset-yolo-format-19-feb-2026")
print(dataset)

dataset.apply_model(model, label_field="yolo26n-best-14-feb-2026-predictions")


session = fo.launch_app(dataset)  # (optional) port=XXXX
session.wait()
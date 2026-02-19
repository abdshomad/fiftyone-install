# On local machine
import fiftyone as fo

# Dataset name
name = "chicken-detection-dataset-yolo-format-19-feb-2026"

# Load existing dataset (do not delete, do not override)
dataset = fo.load_dataset(name)

# Verify the data exists
print(f"Dataset has {len(dataset)} samples")
print(dataset)

# Evaluate the predictions in the `predictions` field of our dataset
# with respect to the objects in the `ground_truth` field
results = dataset.evaluate_detections(
    "predictions",
    gt_field="ground_truth",
    eval_key="eval",
    compute_mAP=True,
)

# Get the 10 most common classes in the dataset
counts = dataset.count_values("ground_truth.detections.label")
classes_top10 = sorted(counts, key=counts.get, reverse=True)[:10]

# Print a classification report for the top-10 classes
results.print_report(classes=classes_top10)

# Print out the mAP score
print(f"mAP score: {results.mAP()}")

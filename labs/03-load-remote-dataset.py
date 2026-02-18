# On remote machine
import fiftyone as fo

dataset = fo.load_dataset(...)

session = fo.launch_app(dataset, remote=True)  # optional: port=XXXX
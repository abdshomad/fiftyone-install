# FiftyOne Install

# Using Conda 
conda create -n fo python=3.11
cd fiftyone
bash install.sh 
cd .. 
python labs/01-load-dataset.py          # OK
python labs/04-load-coco2017-dataset.py # OK
python labs/05-quickstart.py            # OK 

# Using uv (Still error)
Setup for [FiftyOne](https://github.com/voxel51/fiftyone) with a uv-managed Python environment and optional Git submodule.

## Prerequisites

- **[uv](https://docs.astral.sh/uv/)** — Python package and project manager (install from [astral.sh](https://docs.astral.sh/uv/getting-started/installation/))

## Quick start

### 1. Pin Python version (recommended: 3.11)

Stick to Python 3.11 for compatibility with FiftyOne and dependencies.

```bash
uv python pin 3.11
```

### 2. Create and use the virtual environment

```bash
uv venv --seed
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
uv sync
```

### 3. Add FiftyOne as a Git submodule (my preference)

To track the FiftyOne repo inside this project:

```bash
git submodule add https://github.com/voxel51/fiftyone.git
```

After cloning this repo (with submodules), run:

```bash
git submodule update --init --recursive
```

## Running Jupyter Notebook

Activate the venv, then start the notebook server:

```bash
source .venv/bin/activate
jupyter notebook --no-browser --port=5151
# Or with browser: jupyter notebook --port=5151
```

> **Note:** Do **not** use `uvx --with jupyter jupyter notebook ...`; run `jupyter` from the activated environment so it uses the project’s installed packages.

### Access from another machine (SSH tunnel)

On your **local machine**, create an SSH tunnel so you can open the notebook in your browser:

```bash
ssh -N -L 5151:localhost:5151 [<username>@]<hostname>
```

Example:

```bash
ssh -N -L 5151:localhost:5151 nvidia-user@103.215.13.55
```

Then open **http://localhost:5151** in your browser and paste the token shown in the terminal where Jupyter is running.

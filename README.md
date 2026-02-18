# FiftyOne Install

# Add FiftyOne as Git Sub Module 
git submodule add https://github.com/voxel51/fiftyone.git

# To update after cloning 
git submodule update --init --recursive

# Create uv venv (Require: uv : http: ... )
uv venv 
source .venv/bin/activate 
uv init
uv add fiftyone 
uv sync

Run Jupyter Notebook using uv 
DO NOT USE: uvx --with jupyter jupyter notebook --no-browser --port=5151
jupyter notebook --no-browser --port=5151

On our Local Machine, run: 
ssh -N -L 5151:localhost:5151 [<username>@]<hostname>
Example: ssh -N -L 5151:localhost:5151 nvidia-user@103.215.13.55 
Access to http://localhost:5151 
Copy paste the token 
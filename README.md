## Live ASL Fingerspelling Classifier

Classifies American Sign Language alphabet hand signs from a webcam in real time. 
Compare two pipelines: a raw-pixel CNN and a hand-landmark MLP (MediaPipe). 
(Optional) Special case to handle J and Z, as they need motion capture.

# Getting Started

### Prerequisites
- **Git:** check with `git --version`.
- **Python 3.14:** check with `python3 --version` (Windows: `py --version`). If you don't have it, install it from [python.org](https://www.python.org/downloads/) or with `brew install python@3.14` on Mac.

### 1. Clone the repo (first time only)
```bash
git clone https://github.com/ML-Rice/asl_fingerspelling_classifier.git
cd asl_fingerspelling_classifier
```
Run every command below from inside this `asl_fingerspelling_classifier/` folder, the root of the repo.

### 2. Create and activate a virtual environment (first time only)
The virtual environment (`.venv/`) keeps this project's packages separate from the rest of your computer. It is gitignored, so everyone creates their own.

**Mac / Linux**
```bash
python3.14 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
py -3.14 -m venv .venv
.venv\Scripts\Activate.ps1
```
If PowerShell blocks the script, run `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned` once and try again.

When the venv is active, your terminal prompt starts with `(.venv)`. **Activate it every time you open a new terminal to work on the project** (just the `source` / `Activate.ps1` line; you don't need to create it again).

### 3. Install the dependencies
```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```
The first install takes a few minutes because PyTorch is large. Then check that it worked:
```bash
python -c "import torch, cv2, mediapipe; print('torch', torch.__version__, '| ok')"
```
> **NVIDIA GPU users (Windows/Linux):** if `torch.cuda.is_available()` prints `False`, reinstall torch using the command from [pytorch.org/get-started](https://pytorch.org/get-started/locally/) for your CUDA version. Mac users get GPU acceleration through `mps` automatically.

### 4. Set up notebooks (first time only)
```bash
nbstripout --install
```
This strips cell outputs from notebooks when you commit them, which keeps diffs small and avoids merge conflicts. In VS Code or Jupyter, select the `.venv` Python as the notebook kernel. Start Jupyter with `jupyter lab`.

### 5. Download the data
```bash
python data/download_mnist.py
```
This saves Sign Language MNIST into `data/raw_data/`, which is gitignored. Never commit data files.

### Everyday Git workflow
Before you start working, get the latest changes from GitHub:
```bash
git switch main
git pull
```
If `requirements.txt` changed in what you pulled, run `pip install -r requirements.txt` again.

Do your work on your own branch, not on `main`:
```bash
git switch -c <your-name>/<short-task-name>     # e.g. maria/mnist-dataloader
# ...make changes...
git add <files you changed>
git commit -m "Short description of what you did"
git push -u origin <your-name>/<short-task-name>
```
Then open a Pull Request on GitHub for review. If `main` gets updated while you're still working, bring those changes into your branch:
```bash
git switch main && git pull
git switch <your-name>/<short-task-name>
git merge main
```

# Recommended Datasets:
- Sign Language MNIST (J and Z excluded)
- ASL Alphabet (Kaggle) (J and Z excluded)
- Webcam test set (For testing only. 10-20 images per letter recorded by the team: varied people/lightning/background.)

# Evaluation 
- Accuracy
- A 24x24 confusion matrix
- (Optional) Speed and size: FPS and latency per frame

# Project Layout
```
asl_fingerspelling_classifier/
├── asl/                      # importable package (pip install -e .)
│   ├── datasets/
│   │   ├── mnist.py          # Dataset + get_dataloaders(cfg)
│   │   ├── asl_alphabet.py   # (phase 2)
│   │   └── transforms.py     # train/eval transforms per dataset; get_transform(dataset, is_train) used by train/eval/webcam
│   ├── models/
│   │   ├── __init__.py       # registry: get_model(name, **kw)
│   │   ├── logistic.py
│   │   ├── mlp.py
│   │   ├── cnn_small.py
│   │   └── ...               # one architecture per file, one owner each
│   ├── training/
│   │   ├── train.py          # train_model(...) + CLI entrypoint --config
│   │   └── logging.py        # run dir creation, metrics.csv, plots
│   └── utils.py              # set_seed, get_device, count_params
├── configs/mnist/*.yaml
├── data/
│   ├── download_mnist.py
│   ├── raw_data/             # gitignored
│   └── splits/               # committed: fixed val indices
├── notebooks/
│   ├── eda/                  # eda_mnist_<name>.ipynb
│   └── analysis/compare_runs.ipynb   # builds leaderboard from runs/*/summary.json
├── runs/                     # one folder per run; *.pt gitignored
│   └── 20261014-1530_cnn_small_francisco/
│       ├── config.yaml  metrics.csv  summary.json
│       ├── curves.png   confusion_matrix.png
│       └── best.pt      last.pt
├── evaluate.py               # test set: accuracy, confusion matrix, latency, size
├── webcam.py                 # phase 3
├── pyproject.toml
└── requirements.txt
```

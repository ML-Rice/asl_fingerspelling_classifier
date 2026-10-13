## Live ASL Fingerspelling Classifier

Classifies American Sign Language alphabet hand signs from a webcam in real time. 
Compare two pipelines: a raw-pixel CNN and a hand-landmark MLP (MediaPipe). 
(Optional) Special case to handle J and Z, as they need motion capture.

# Getting Started (Google Colab)
You only need a Google account and a web browser. There is nothing to install.

### 1. Open the template
Click here: <a href="https://colab.research.google.com/github/ML-Rice/asl_fingerspelling_classifier/blob/main/mnist_template.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

Or, in [Colab](https://colab.research.google.com): **File → Open notebook → GitHub**, search for `ML-Rice/asl_fingerspelling_classifier`, and pick `mnist_template.ipynb`.

### 2. Save your own copy
1. **File → Save a copy in Drive.** Your copy opens in a new tab. Work in that tab, not the original.
2. Click the notebook title at the top left and rename it to `<yourname>_mnist.ipynb` (e.g. `maria_mnist.ipynb`).

Your copy is saved in your Google Drive, in the **Colab Notebooks** folder.

### 3. (Optional) Turn on the GPU
**Runtime → Change runtime type → T4 GPU → Save.**
MNIST trains fine without a GPU. We'll need one later for the ASL Alphabet dataset (200×200 images). Free GPU time is limited, so leave it off when you don't need it.

### 4. Work through the notebook
- Run a cell with **Shift + Enter**.
- **Every time you reopen the notebook, run the Setup cells first.** Colab forgets everything (variables, downloaded data, saved files) when your session ends. To catch up quickly, click into the cell you want to continue from and use **Runtime → Run before**.
- Work through Steps 1 to 6, one step per week.
- Stuck for more than ~30 minutes? Check the docs linked in that step, then search the error message, then ask your buddy, then ask the group chat.

### 5. Submit your notebook
1. **Runtime → Restart session and run all.** The notebook must run from top to bottom without errors.
2. **File → Download → Download .ipynb**.
3. On this repo's GitHub page: **Add file → Upload files**, drag in your `<yourname>_mnist.ipynb`, and click **Commit changes**.

To submit a newer version later, upload it again with the same filename and it replaces the old one. You need to be a collaborator on the repo to upload, so ask the project lead to add you.

# What's in this repo
- `mnist_template.ipynb`: the starter notebook. Don't edit it directly; save a copy (step 2 above).
- `data/download_mnist.py`: downloads the MNIST data, for running locally.
- `requirements.txt`: Python packages, for running locally.

<details>
<summary><b>Local setup</b> (not needed for Colab; used later for the live webcam demo)</summary>

Requires Git and Python 3.14.

```bash
git clone https://github.com/ML-Rice/asl_fingerspelling_classifier.git
cd asl_fingerspelling_classifier

# Create and activate a virtual environment
python3.14 -m venv .venv
source .venv/bin/activate          # Windows (PowerShell): .venv\Scripts\Activate.ps1

# Install packages and download the data
pip install -r requirements.txt
python data/download_mnist.py      # saves to data/raw_data/ (gitignored)
```
Activate the venv again every time you open a new terminal.

</details>

# Recommended Datasets:
- Sign Language MNIST (J and Z excluded)
- ASL Alphabet (Kaggle) (J and Z excluded)
- Webcam test set (For testing only. 10-20 images per letter recorded by the team: varied people/lightning/background.)

# Evaluation 
- Accuracy
- A 24x24 confusion matrix
- (Optional) Speed and size: FPS and latency per frame

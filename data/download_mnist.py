import kagglehub
from pathlib import Path


# Output Directory for downloaded dataset files
DATA_DIR = Path("data/raw_data")

# Check if the output directory exists, if not create it
if not DATA_DIR.exists():
    DATA_DIR.mkdir(parents=True, exist_ok=True)

# Download latest version
path = kagglehub.dataset_download("datamunge/sign-language-mnist", output_dir=DATA_DIR)

print("Path to dataset files:", path)
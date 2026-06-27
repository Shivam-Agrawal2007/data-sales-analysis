import os

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATASET_DIR = os.path.join(PROJECT_ROOT, "dataset")
REPORTS_DIR = os.path.join(PROJECT_ROOT, "reports")
CHARTS_DIR = os.path.join(PROJECT_ROOT, "charts")

TRAIN_DATA = os.path.join(DATASET_DIR, "train.csv")
CLEANED_DATA = os.path.join(DATASET_DIR, "cleaned_sales.csv")
# LOG_DIR = os.path.join(PROJECT_ROOT, "logs")
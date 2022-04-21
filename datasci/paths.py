from pathlib import Path

SRC_DIR = Path(__file__).absolute().parent
ROOT_DIR = SRC_DIR.parent

DATA_DIR = ROOT_DIR / 'data'

RAW_DIR = DATA_DIR / 'raw'
INTERIM_DIR = DATA_DIR / 'interim'
PROCESSED_DIR = DATA_DIR / 'processed'
ARTIFACTS_DIR = DATA_DIR / 'artifacts'
OUTPUT_DIR = DATA_DIR / 'output'

"""Shared paths and constants for the VisDrone dataset scripts."""

from pathlib import Path

# Root of the downloaded, unzipped VisDrone2019-DET-train folder
# (contains `images/` and `annotations/` subfolders of raw VisDrone data).
RAW_TRAIN_DIR = Path(
    r"C:\Users\aaron\OneDrive\Documents\Personal\Summer Project 2026\visdrone_data\VisDrone2019-DET-train"
)

# Where converted YOLO-format data (images/{split} + labels/{split}) will live.
YOLO_DATA_DIR = Path(__file__).resolve().parent.parent / "data" / "visdrone_yolo"

# VisDrone category id (as it appears in the raw annotation files, column 6)
# -> class name. Category 0 ("ignored regions") and 11 ("others") are not
# real object classes and should be excluded during conversion.
VISDRONE_CATEGORIES = {
    0: "ignored-region",
    1: "pedestrian",
    2: "people",
    3: "bicycle",
    4: "car",
    5: "van",
    6: "truck",
    7: "tricycle",
    8: "awning-tricycle",
    9: "bus",
    10: "motor",
    11: "others",
}

# YOLO class index -> name (category id - 1, only for ids 1-10).
YOLO_CLASSES = {i - 1: name for i, name in VISDRONE_CATEGORIES.items() if 1 <= i <= 10}

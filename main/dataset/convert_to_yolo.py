"""Convert raw VisDrone annotations into YOLO label format.

YOLO format: one .txt file per image, same base filename, one line per
object:

    <class_id> <x_center> <y_center> <width> <height>

All four numeric values are normalised to [0, 1] by dividing by the image
width/height (x_center/width by image width, y_center/height by image
height). class_id is 0-indexed.

This script should NOT split into train/val/test - that happens afterwards
in split_dataset.py, once every image in RAW_TRAIN_DIR has been converted
into one flat pool. Trying to do conversion and splitting in the same pass
makes both harder to test independently.

Output layout (flat, pre-split):
    YOLO_DATA_DIR/all/images/<name>.jpg   (copied or linked from raw)
    YOLO_DATA_DIR/all/labels/<name>.txt   (converted annotation)
"""

from config import RAW_TRAIN_DIR, YOLO_DATA_DIR


def convert_annotation(txt_path, img_width, img_height):
    """Convert one raw VisDrone .txt file's contents into YOLO-format lines.

    Steps per object line in the raw file:
    1. Skip it if score == 0 (ignored region - not a real object).
    2. Skip it if category is 0 or 11 (ignored-region / others - not one
       of the 10 real classes YOLO_CLASSES covers).
    3. class_id = category - 1 (VisDrone categories 1-10 -> YOLO 0-9).
    4. Convert (left, top, width, height) in pixels to
       (x_center, y_center, width, height) normalised by img_width/img_height.
    5. Format as "<class_id> <x_center:.6f> <y_center:.6f> <w:.6f> <h:.6f>".

    Return a list of formatted line strings (no trailing images needed).

    Consider reusing explore.load_annotations() to parse the raw file rather
    than re-implementing the CSV parsing here.

    TODO: implement.
    """
    raise NotImplementedError


def convert_dataset(raw_dir=RAW_TRAIN_DIR, out_dir=YOLO_DATA_DIR):
    """Convert every annotation in raw_dir into YOLO format under
    out_dir/all/{images,labels}.

    Steps:
    1. Create out_dir/all/images and out_dir/all/labels.
    2. For each annotation file in raw_dir/annotations:
       a. Open the matching image (raw_dir/images/<name>.jpg) to get its
          (width, height) - PIL's Image.open(path).size is enough, no need
          to decode pixels.
       b. Call convert_annotation() and write the result to
          out_dir/all/labels/<name>.txt.
       c. Copy (not move - keep the raw data intact) the image into
          out_dir/all/images/<name>.jpg.
    3. Print a short progress indicator (e.g. every N images) since this
       will run over ~6500 images.

    TODO: implement.
    """
    raise NotImplementedError


def main():
    convert_dataset()


if __name__ == "__main__":
    main()

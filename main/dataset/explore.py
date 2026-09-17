"""Sanity-check the raw VisDrone annotation format before converting anything.

Goal: load ONE image + its matching annotation file, parse it, and draw the
boxes on the image with OpenCV so you can visually confirm you understand the
raw format (and catch coordinate mistakes early, before they get baked into
a converted dataset).

Raw VisDrone annotation file format (one line per object, comma-separated,
no header), from the VisDrone2019-DET annotation spec:

    <bbox_left>,<bbox_top>,<bbox_width>,<bbox_height>,<score>,<category>,<truncation>,<occlusion>

- bbox_left, bbox_top: top-left corner of the box, in pixels
- bbox_width, bbox_height: box size, in pixels
- score: 1 = valid object for evaluation, 0 = "ignored region" (not a real
  object - should be skipped/excluded)
- category: object class id, see config.VISDRONE_CATEGORIES
    (note: this is 1-indexed for real classes; 0 = ignored region, 11 = others)
- truncation: 0 = not truncated, 1 = partially outside the frame
- occlusion: 0 = none, 1 = partial (<50%), 2 = heavy (>50%)

Run this against a handful of images from RAW_TRAIN_DIR and eyeball the
result before writing stats.py or convert_to_yolo.py.
"""

import cv2 as cv

from config import RAW_TRAIN_DIR, VISDRONE_CATEGORIES


def load_annotations(txt_path):
    """Parse a single VisDrone .txt annotation file.

    Return a list of dicts, one per object, each with keys:
    left, top, width, height, score, category, truncation, occlusion
    (all ints). Skip malformed/blank lines.

    TODO: implement.
    """


def draw_boxes(image, annotations):
    """Draw a rectangle + class-name label for each annotation onto `image`.

    - Use cv2.rectangle for the box.
    - Use cv2.putText for the class name (look up via VISDRONE_CATEGORIES).
    - Consider skipping / drawing differently boxes where score == 0
      (ignored regions) so you can visually tell them apart.
    - Return the modified image (or modify in place, your choice).

    TODO: implement.
    """
    raise NotImplementedError


def main():
    """Pick one image, load its annotations, draw them, and show the result.

    Steps:
    1. Pick a filename stem present in both RAW_TRAIN_DIR/images and
       RAW_TRAIN_DIR/annotations (e.g. iterate images/ and take the first).
    2. Load the image with cv2.imread.
    3. Parse the matching annotation file with load_annotations.
    4. Print a quick summary: how many objects, how many per category.
    5. Draw the boxes with draw_boxes and cv2.imshow the result
       (cv2.waitKey(0) + cv2.destroyAllWindows() to close it).

    TODO: implement.
    """

    test_img =  RAW_TRAIN_DIR/"0000002_00005_d_0000014.jpg"
    #test_label = VISDRONE_CATEGORIES/"0000002_00005_d_0000014"
    cv.imread(test_img)
    cv.imshow("test", test_img)


if __name__ == "__main__":
    main()

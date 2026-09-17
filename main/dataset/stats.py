"""Dataset-wide statistics for the raw VisDrone train split.

Run this AFTER explore.py has confirmed you're parsing the raw annotation
format correctly. This script walks the *entire* dataset (not just one
image) to build up the numbers that actually matter for training decisions:

- Class distribution: how many boxes per category, across all images.
  VisDrone is known to be heavily imbalanced (lots of cars/pedestrians,
  few buses/awning-tricycles) - this number is what will later justify
  things like class weighting or augmentation choices.
- Image size distribution: are all images the same resolution, or mixed?
  Affects whether you can assume a fixed input size.
- Annotations-per-image distribution: how crowded are VisDrone images?
  (VisDrone scenes can have 100+ objects in one frame - very different
  from something like COCO.)

Suggested plots (matplotlib): a bar chart of class counts, a histogram of
image widths/heights, a histogram of objects-per-image.
"""

from collections import Counter

from config import RAW_TRAIN_DIR, VISDRONE_CATEGORIES


def collect_stats(raw_dir=RAW_TRAIN_DIR):
    """Walk every annotation file in raw_dir/annotations and every image in
    raw_dir/images, and return the raw numbers needed for the plots below.

    Suggested return value: a dict with keys like
        "class_counts": Counter mapping category id -> box count
        "image_sizes": list of (width, height) tuples
        "boxes_per_image": list of ints (one entry per image)

    Notes:
    - Reuse explore.load_annotations() rather than re-writing the parser.
    - Decide whether ignored regions (score == 0) should count towards
      "boxes_per_image" - probably not, since they're not real objects.
    - Getting image size without loading the full image into memory is
      possible with PIL (Image.open(path).size doesn't decode pixels) -
      worth comparing against cv2.imread if you're curious about speed.

    TODO: implement.
    """
    raise NotImplementedError


def plot_class_distribution(class_counts):
    """Bar chart: category name (x) vs total box count (y).

    Use VISDRONE_CATEGORIES to map ids to readable names. Consider a log
    scale on the y-axis given how imbalanced VisDrone is.

    TODO: implement.
    """
    raise NotImplementedError


def plot_image_sizes(image_sizes):
    """Scatter or 2D histogram of image width vs height.

    TODO: implement.
    """
    raise NotImplementedError


def plot_boxes_per_image(boxes_per_image):
    """Histogram of objects-per-image.

    TODO: implement.
    """
    raise NotImplementedError


def main():
    """Collect stats, print a short text summary, then show the plots.

    Text summary should include at minimum: total images, total boxes,
    min/max/mean boxes per image, and the count for each class sorted
    descending (this is the number you'll actually reference later).

    TODO: implement.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()

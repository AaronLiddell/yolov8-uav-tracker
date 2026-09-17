"""Split the converted YOLO-format pool into train/val/test.

You're only working with the VisDrone *train* split right now (no official
val/test-dev downloaded), so this does a random split of the ~6471 images
in YOLO_DATA_DIR/all/ rather than using VisDrone's own predefined splits.

A reasonable default is 80/10/10 (train/val/test), but that's a judgement
call worth thinking about, not a fixed rule - e.g. with only 6471 images and
10 imbalanced classes, you may want val/test large enough that rare classes
(bus, awning-tricycle) actually appear in them at all.

Output layout (this is the structure Ultralytics' VisDrone.yaml expects):
    YOLO_DATA_DIR/images/train/, images/val/, images/test/
    YOLO_DATA_DIR/labels/train/, labels/val/, labels/test/
"""

import random

from config import YOLO_DATA_DIR


def split_filenames(all_images_dir, train_ratio=0.8, val_ratio=0.1, seed=42):
    """Return (train_names, val_names, test_names) - lists of image
    filenames (no path, no extension) from all_images_dir, randomly
    shuffled and partitioned according to the given ratios.

    test_ratio is implied as 1 - train_ratio - val_ratio.

    Use a fixed `seed` so the split is reproducible across runs - important
    so that if you rerun this script later you get the SAME split, not a
    new random one that silently invalidates any results tied to the old
    split.

    TODO: implement.
    """
    raise NotImplementedError


def move_split(names, split_name, all_dir=YOLO_DATA_DIR / "all", out_dir=YOLO_DATA_DIR):
    """Move (not copy) each image + matching label file for `names` from
    all_dir/{images,labels} into out_dir/images/<split_name>/ and
    out_dir/labels/<split_name>/.

    TODO: implement.
    """
    raise NotImplementedError


def main():
    """Run split_filenames on YOLO_DATA_DIR/all/images, then move_split for
    each of train/val/test.

    After this runs, YOLO_DATA_DIR/all/ should be empty and can be removed -
    print the final counts per split before finishing so you can sanity
    check nothing was silently dropped (train + val + test == total).

    TODO: implement.
    """
    raise NotImplementedError


if __name__ == "__main__":
    main()

import os

folder = r"C:\Users\Milsort\Dropbox\computer_vision\semantic_segmentation\data\wheat\all_training_data\tiled_data\fltr"

for filename in os.listdir(folder):
    if "_watershed_mask" in filename:
        new_name = filename.replace("_watershed_mask", "_mask")
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

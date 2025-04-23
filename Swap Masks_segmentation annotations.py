import os

folder = r"C:\Users\path to mask"

# STEP 1: Rename all '-1' to '-TEMP' to avoid overwriting
for filename in os.listdir(folder):
    if "-5_color_mask" in filename or "-5_mask" in filename or "-5_watershed_mask" in filename:
        new_name = filename.replace("-5_", "-TEMP_")
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

# STEP 2: Rename all '-3' to '-1'
for filename in os.listdir(folder):
    if "-7_color_mask" in filename or "-7_mask" in filename or "-7_watershed_mask" in filename:
        new_name = filename.replace("-7_", "-5_")
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

# STEP 3: Rename all '-TEMP' to '-3'
for filename in os.listdir(folder):
    if "-TEMP_color_mask" in filename or "-TEMP_mask" in filename or "-TEMP_watershed_mask" in filename:
        new_name = filename.replace("-TEMP_", "-7_")
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

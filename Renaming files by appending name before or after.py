import os

folder = r"C:\Userspath_to_folder"

for filename in os.listdir(folder):
    # Skip directories
    if os.path.isfile(os.path.join(folder, filename)):
        name, ext = os.path.splitext(filename)
        new_name = f"{name}_color_mask{ext}"
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

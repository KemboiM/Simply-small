import os

folder = r"C:\Users\path"

for filename in os.listdir(folder):
    if "old_name" in filename:
        new_name = filename.replace("old_Name", "current_name")
        os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

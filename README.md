# Simply-small

Python Steps

Download the script
Save the file as rename.py.
Edit paths to the folder
Open Command Prompt.
Navigate to the folder where rename.py is saved using cd command.
Run:


PowerShell Steps


Press Win + X, then select Windows PowerShell or Windows Terminal.
Navigate to your folder
Run this command to rename the files
Get-ChildItem -Filter "*Current_name*" | Rename-Item -NewName { $_.Name -replace '_current_name','required_name' }

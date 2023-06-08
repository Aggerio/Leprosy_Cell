import os

print("TRYING TO DOWNLOAD REQUIREMENTS")

try:
    os.system("pip install -r requirements.txt")
except Exception as e:
    print(f"The following exception occured {e}!!")


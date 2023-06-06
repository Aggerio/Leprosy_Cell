import os

print("TRYING TO DOWNLOAD REQUIREMENTS")

try:
    os.system("pip install opencv-python matplotlib random numpy")
except Exception as e:
    print(f"The following exception occured {e}!!")


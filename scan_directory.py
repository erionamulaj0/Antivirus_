import os

def scanFiles(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            
            
            
if __name__ == "__main__":
    specified_folder = r"C:\Users\Admin\Desktop\Certificates"
    scanFiles(specified_folder)
import os

def isFileCorrupted(file_path, expected_signature):
    try:
        with open(file_path, 'rb') as file:
            actual_signature = file.read(len(expected_signature))
            return actual_signature == expected_signature
                 
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred while checking {file_path}: {e}")
        
    
def scanFiles(directory, expected_signature):
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            print(file_path)
            isFileCorrupted(file_path,expected_signature)
            if isFileCorrupted(file_path, expected_signature):
                print("File is not corrupted")
            else:
                print("File is definetly corrupted, seek help now!!!")
                        
            
if __name__ == "__main__":
    #specified_folder = r"C:\Users\Admin\Desktop\AA"  #FILE NOT CORRUPTED
    specified_folder = r"C:\Users\Admin\Desktop\Hyrje ne sigurine e informacionit" 
    expected_signature = b"\x89PNG\r\n\x1a\n"            
    scanFiles(specified_folder, expected_signature)
    


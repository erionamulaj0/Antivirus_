def isFileCorrupted(file_path, expected_signature):
    try:
        with open(file_path, 'rb') as file:
            actual_signature = file.read(len(expected_signature))
            return actual_signature == expected_signature
           
        
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return False
    except Exception as e:
        print(f"An error occurred while checking {file_path}: {e}")
        return False
    

if __name__ == "__main__":
    file_path = r"C:\Users\Admin\Desktop\Antivirus\pictures\comp.jpg"
    expected_signature = b"GIF89a"  #file corrupted  
    #expected_signature = b"\xff\xd8"  #file not corrupted
    isFileCorrupted(file_path, expected_signature)
    if isFileCorrupted(file_path, expected_signature):
        print("File is not corrupted.")
    else:
        print("File may be corrupted.")
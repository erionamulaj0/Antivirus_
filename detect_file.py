import os

def is_malicious_file(file_path, malicious_signature):
    try:
        with open(file_path, "rb") as file:
            file_content = file.read()
            if malicious_signature in file_content:
                return True
        return False
    except FileNotFoundError:
        print("File not found.")
        return False

if __name__ == "__main__":
    malicious_signature = b"X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*"
    file_path = r"C:\Users\Admin\Desktop\Antivirus\Eicar\eicar.com"

    if is_malicious_file(file_path, malicious_signature):
        print("Malicious file has been detected.")
        input('Do you want to delete')
        os.remove(file_path)
        print("File deleted")
    else:
        print("File appears to be clean.")
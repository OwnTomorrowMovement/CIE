import os
import zipfile
import requests
import tkinter as tk
from tkinter import simpledialog
import subprocess
import time
import shutil

def download_file(url, password, local_filename):
    try:
        headers = {'password': password}
        with requests.get(url, headers=headers, stream=True) as r:
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)
        return local_filename
    except Exception as e:
        print(f"Error downloading file: {e}")
        return None

def upload_file(url, password, file_path):
    try:
        headers = {'password': password}
        with open(file_path, 'rb') as f:
            files = {'file': f}
            response = requests.post(url, headers=headers, files=files)
        return response
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None

def unzip_file(zip_path, extract_to):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_to)
    except Exception as e:
        print(f"Error unzipping file: {e}")

def zip_directory(directory_path, zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(directory_path):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory_path))
    except Exception as e:
        print(f"Error zipping directory: {e}")

def delete_directory_contents(directory_path):
    try:
        shutil.rmtree(directory_path)
        os.makedirs(directory_path)
    except Exception as e:
        print(f"Error deleting directory contents: {e}")

# GUI to get server IP, port, and password
root = tk.Tk()
root.withdraw()
server_ip = simpledialog.askstring("Input", "Enter server IP:", initialvalue="127.0.0.1")
server_port = simpledialog.askstring("Input", "Enter server port:", initialvalue="443")
password = simpledialog.askstring("Input", "Enter password:", show='*')

download_url = f"http://{server_ip}:{server_port}/download/Data.zip"
upload_url = f"http://{server_ip}:{server_port}/upload"

# Download and unzip Data.zip
local_zip_path = './Data.zip'
if download_file(download_url, password, local_zip_path):
    unzip_file(local_zip_path, './Data/')

    # Start FirefoxPortable.exe
    try:
        firefox_process = subprocess.Popen(["./FirefoxPortable.exe"])
    except Exception as e:
        print(f"Error starting FirefoxPortable.exe: {e}")

    # Wait for FirefoxPortable.exe to be closed
    while firefox_process.poll() is None:
        time.sleep(1)

    # Zip the Data directory and upload
    zip_directory('./Data/', './Data.zip')
    upload_file(upload_url, password, './Data.zip')

    # Delete contents of Data directory
    delete_directory_contents('./Data/')

    print("Process completed successfully.")
else:
    print("Download failed.")

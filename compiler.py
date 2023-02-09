import PyInstaller.__main__
from pathlib import Path
import os
import shutil
import time
import hjson
path = Path.cwd()
bin_path = os.path.join(path, "bin")


def removedir(dir):
    if os.path.exists(dir):
        print(f"deleting '{dir}' folder")
        for filename in os.listdir(dir):
            file_path = os.path.join(dir, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print("Failed to delete %s. Reason: %s" % (file_path, e))
        os.removedirs(dir)
        time.sleep(1)


removedir(bin_path)
with open('settings.py', 'w')as f:
    with open('settings.hjson', 'r') as j:
        read = j.read()
        f.write(str(hjson.loads(read)))
        
        
        

print("compiling")
PyInstaller.__main__.run(
    [
        "main.py",
        "--onefile",
        "-w",  # change to "-c" for console
        "-i",
        "./Icon.ico",
        "--distpath",
        "./bin",
        "-n",
        "Lil Brute and friends",
        "--add-data",
        "settings.py",
        "--log-level",
        "ERROR",
    ]
)
removedir(os.path.join(path, "build"))
os.remove("settings.py")
 
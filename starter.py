import requests
import subprocess
from config import SERVER_VERSION, API_URLS, MINECRAFT_PATH
from database.database import Database
import os

cwd = os.getcwd()


db = Database("main")

def download_build(latest_build):
    print("Downloading...")
    download_name_request = requests.get(API_URLS["download_name"].format(version=SERVER_VERSION, build=latest_build))
    download_name = download_name_request.json()["downloads"]["application"]["name"]
    
    download_file_request = requests.get(API_URLS["download_build"].format(version=SERVER_VERSION, build=latest_build, download_name=download_name))
    with open(f"{cwd}/{MINECRAFT_PATH}server.jar", "wb") as file:
        file.write(download_file_request.content)
    
    print("Done!")
    
    db.set_value("paper-version", latest_build)


def get_latest_build():
    build_request = requests.get(API_URLS["version_builds"] + SERVER_VERSION)
    latest_build = build_request.json()["builds"][-1]
    return latest_build


def is_update_available(latest_build):
    print("Checking for updates...")
    version = db.get_value("paper-version")
    if version is None:
        print("No version in database, downloading latest...")
        return True
    else:        
        if version == latest_build:
            print("Latest version already downloaded!")
            return False
        else:
            print("New version available!")
            return True


def server_worker():
    print("Starting server...")
    start_args = ["java", "-Xms2G", "-Xmx2G", "-jar", f"{cwd}/{MINECRAFT_PATH}server.jar", "nogui"]
    subprocess.run(start_args)
    print("Server stopped!")	
    


def main():
    latest_build = get_latest_build()
    if is_update_available(latest_build):
        download_build(latest_build)
    server_worker()
    
    
    


if __name__ == "__main__":
    main()
import os
import requests
import zipfile
import shutil

def update_folder_with_repository(username, repo_name):
    # Create a temporary directory to store the downloaded repository
    temp_dir = 'temp'
    os.makedirs(temp_dir, exist_ok=True)

    try:
        # Download the repository as a zip file
        download_url = f"https://github.com/FlicksDaModdle/HomeAssetDl/archive/refs/heads/main.zip"
        response = requests.get(download_url)

        if response.status_code == 200:
            # Save the zip file
            zip_path = os.path.join(temp_dir, f"{repo_name}.zip")
            with open(zip_path, 'wb') as zip_file:
                zip_file.write(response.content)

            # Extract the zip file to the temporary directory
            extract_dir = os.path.join(temp_dir, 'extracted')
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(extract_dir)

            # Move the extracted files to the current directory
            source_dir = os.path.join(extract_dir, f"{repo_name}-main")
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    source_path = os.path.join(root, file)
                    target_path = os.path.join(os.getcwd(), file)
                    shutil.copy2(source_path, target_path)

            print("Update completed successfully.")
        else:
            print("Failed to download the repository.")
    except Exception as e:
        print("An error occurred:", str(e))
    finally:
        # Remove the temporary directory
        shutil.rmtree(temp_dir, ignore_errors=True)

# Example usage
repository_username = "FlicksDaModdle"
repository_name = "HomeAssetDl"
update_folder_with_repository(repository_username, repository_name)

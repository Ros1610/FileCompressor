import zipfile

def extract_archive(archive_path, dest_dir):
    with zipfile.ZipFile(archive_path, 'r') as file:
        file.extractall(dest_dir)

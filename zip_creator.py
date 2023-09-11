import zipfile
import pathlib

def make_archive(filepath_arg, folder_arg):
    """Create a path for the compressed file"""
    end_path = pathlib.Path(folder_arg, "compressed.zip")
    """Create a path for the original files"""
    filepath_arg = map(pathlib.Path, filepath_arg)

    with zipfile.ZipFile(end_path, 'w') as file:
        """Write files to the compressed file"""
        for filepath in filepath_arg:
            file.write(filepath, arcname=filepath.name)

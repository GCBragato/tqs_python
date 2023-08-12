import os


def get_all_folders(dirname):
    """Returns all folders and subfolders in a directory"""

    dirname = os.path.normpath(dirname)
    subfolders = [f.path for f in os.scandir(dirname) if f.is_dir()]
    for dirname in list(subfolders):
        subfolders.extend(get_all_folders(dirname))

    return subfolders


def tqs_filter(dirs: str) -> str:
    """Filters out only the folders that are TQS projects."""

    for dir in dirs[:]:
        current_dir = os.path.join(dir, 'EDIFICIO.BDE')
        if not os.path.exists(current_dir):
            dirs.remove(dir)

    return dirs


def main(tqs_folder: str):
    dirs = get_all_folders(tqs_folder)
    projects = tqs_filter(dirs)
    #print(projects)
    return projects


if __name__ == '__main__':
    tqs_folder = os.path.normpath('C:\\TQS\\')
    main(tqs_folder)

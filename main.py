
def get_path():
    import configparser

    f_path = None

    try:
        parser = configparser.ConfigParser()
        parser.read("config.conf")
        f_path = parser.get('general', 'files_path')
    except Exception as e:
        print(f"ERROR GETTING FILES_PATH: {e}")

    return f_path


def get_list():
    f_list = []

    try:
        with open("list.txt", "r", encoding='utf-8') as f:
            f_list = f.readlines()
        f_list = [x.replace('\n', '') for x in f_list]
    except Exception as e:
        print(f"ERROR GETTING LIST: {e}")

    return f_list


def move_files(f_path, f_list):
    import os
    import shutil

    # Create directory to move files in
    moved_path = f"{f_path}{os.sep}moved"
    try:
        if not os.path.exists(moved_path):
            os.mkdir(moved_path)
    except Exception as e:
        print("Couldn't find/create subfolder to move the files. Maybe check the config file?")
        raise e

    directory = os.fsencode(f_path)
    files_to_move = []
    files_moved = []

    # Get all files to move
    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if os.path.isfile(os.path.join(f_path, filename)) and filename not in f_list:
            files_to_move.append(filename)

    # Move them
    for filename in files_to_move:
        shutil.move(f"{f_path}{os.sep}{filename}", moved_path)
        files_moved.append(filename)

    return files_moved


if __name__ == '__main__':
    print("Getting files path...", end='')
    path = get_path()
    print("OK!")
    print("Getting list of files to not move...", end='')
    files_list = get_list()
    print("OK!")
    print(f"Moving files...")
    moved_files = move_files(path, files_list)
    print(f"Process done successfully!")
    if moved_files:
        print(f"Files moved: {moved_files}")
    else:
        print(f"No files were moved.")

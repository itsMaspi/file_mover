# file_mover
This simple python tool moves all the not wanted files into a subfolder.

## Usage
### config.conf
This file is used to indicate which folder to use.

    [general]
    files_path=/home/user/files_to_move/

### list.txt
This file contains all the files that won't be moved. Further information is found in the file itself.

### Excecution
When everything is properly configured, you just have to run the `main.py` file.

    python main.py

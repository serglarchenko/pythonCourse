import os
import fnmatch

path = r'C:\Users\Serhii_Larchenko\Desktop\ORKE'


def print_files_and_directories(path_, subject_to_find=None, file_pattern=None):
    info = list(os.walk(path_))
    if subject_to_find == 'f' and file_pattern is not None:
        for (root, dirs, files) in info:
            print(fnmatch.filter(files, file_pattern))
    elif subject_to_find == 'f' and file_pattern is None:
        for (root, dirs, files) in info:
            print(files)
    elif subject_to_find == 'd':
        for (root, dirs, files) in info:
            print(dirs)
    else:
        for root, dirs, files in info:
            for name in files:
                print(os.path.join(root, name))


print_files_and_directories(path, 'f', '*.json')

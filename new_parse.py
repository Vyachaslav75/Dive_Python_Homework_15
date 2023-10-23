import os
from collections import namedtuple
from pathlib import Path
import argparse
import logging


def main():
    parser=argparse.ArgumentParser(description='My path parser')
    parser.add_argument('path', metavar='path', type=str, nargs=1, help='Input path for analyse')
    args=parser.parse_args()
    if Path(args.path[0]).exists():
        my_walk(args.path[0])
    else:
        print('Path does not exists')


def my_walk(my_path=os.getcwd()):
    logging.basicConfig(filename='path_log.log.', filemode='w', encoding='utf-8', level=logging.INFO)
    logger = logging.getLogger('main')
    
    fs = os.walk(my_path)
    FileInfo = namedtuple('FileInfo', ['name', 'ext', 'parent_folder'])
    folder_list = []
    for f in fs:
        if len(f[1]) > 0:
            for i in f[1]:
                temp_info = FileInfo(i, 'folder', f[0])
                folder_list.append(temp_info)
                logging.info(temp_info)
        if len(f[2]) > 0:
            for i in f[2]:
                name = Path(f[0], i)
                temp_info = FileInfo(name.stem, name.suffix, f[0])
                folder_list.append(temp_info)
                logging.info(temp_info)
 
    # for i in folder_list:
    #     print(i)



if __name__ == "__main__":
    main()

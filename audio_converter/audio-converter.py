import os
import fnmatch
import sys


# is necessary install ffmpeg 

command_ffmpeg = 'ffmpeg' # if your OS is Linux, if not, use Windows command.
source = '/home/user/videos/' # path where are the files to be converted.
final_source = '/home/user/convert/' # path where the converted files will be

for root, folder, file in os.walk(source):

    for file in file:
        print('Converting the file : {}'.format(file))

        full_path = os.path.join(root, file)
        file_name, file_ext = os.path.splitext(full_path)
        file_name, file_ext = os.path.splitext(file)

        new_file = final_source + file_name + '.m4a' # modify with the extension you want
        exit_file = os.path.join(root, new_file)

        command = '{} -i {} -c:a aac {}'.format(command_ffmpeg, full_path, exit_file)

        os.system(command)
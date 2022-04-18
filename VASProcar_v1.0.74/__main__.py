
import os
import sys
import shutil

dir_files = os.getcwd()

os.chdir(os.path.dirname(sys.executable) + '\Lib' + '\\VASProcar')

# src directory to the main python codes
main_dir = 'src\\'
run = main_dir + '_settings.py'
exec(open(run).read())

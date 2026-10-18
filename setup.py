from distutils.core import setup
import py2exe

setup(windows=['main.py'])


# setup(
#     windows=['main_script.py'],
#     data_files=[('',
#                  ['path_to_image1.jpg',
#                   'path_to_image2.png',
#                   'path_to_data.json'])]
# )

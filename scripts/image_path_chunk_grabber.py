'''
<license>
CSPLN_MaryKeelerEdition; Manages images to which notes can be added.
Copyright (C) 2015, Thomas Kercheval

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
___________________________________________________________</license>

Description:
    Grabs chunks of image_paths to be processed by other scripts.

Inputs:
    Amount of images_per_app
    Processed images.

Outputs:
    Dictionary form {P_:[array]}, P_ referring to the specific web_app
        arrays consisting of image_file_paths.

Currently:

To Do:

Done:
'''

import os

def grab_image_paths():
    """Returns a list of processed png image paths"""
    image_path_list = []
    for root, dirs, files in os.walk("../images/processed_images",
                                     topdown=False):
        del dirs
        for name in files:
            if name[-4:] == '.png':
                image_path_list.append((os.path.join(root, name)))
    return image_path_list

def chunk_it_out(image_path_list, images_per_app):
    """
    Returns a list of arrays, each array has a maximum number of
        images that is specified by images_per_app.
    """
    array_list = []
    while len(image_path_list) > 0:
        array = []
        for _ in range(images_per_app):
            if len(image_path_list) == 0:
                break
            array.append(image_path_list.pop(0))
        array.sort()
        array_list.append(array)
    return array_list

def image_path_chunk_grabber(images_per_app):
    """
    Assigns each array of image paths a key in a dictionary,
        which corresponds to which application the images will belong to.
    """
    path_list = grab_image_paths()
    chunk_list = chunk_it_out(path_list, images_per_app)
    count = 0
    chunk_dict = {}
    for array in chunk_list:
        count += 1
        chunk_dict['P{}'.format(count)] = array
    return chunk_dict

if __name__ == "__main__":
    IMAGES_PER_APP = 66
    CHUNKS = image_path_chunk_grabber(IMAGES_PER_APP)
    for part in CHUNKS:
        print part, '\n', CHUNKS[part], '\n'

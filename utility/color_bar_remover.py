# -*- coding: utf-8 -*-
"""
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
    Removes the color bar from the processed images.

Inputs:
    Processed tiff images, with color bars.

Outputs:
    Processed tiff images, without color bars.

Currently:


To Do:

Done:
"""

from PIL import Image
import sys
import os

def gather_image_paths(image_dir):
    """Gathers image paths to be cropped."""
    print "\n    Gathering image paths from specified directory..."
    path_list = []
    for root, dirs, files in os.walk(image_dir["path"], topdown=False):
        del dirs
        for name in files:
            if name[-4:] == '.tif':
                path_list.append((os.path.join(root, name)))
    return path_list

def define_out_paths(path_list):
    """Modifies image paths to their output form."""
    print "    Generating out paths, based on origianl image paths."
    out_path_list = []
    for path in path_list:
        out_path_list.append(path.replace("processed_images", 
                                          "processed_wcb_images").replace(
                                          "M2JT", "M2JTwcb"))
    return path_list, out_path_list
    
def crop_image(image_path, out_path, crop_amount):
    """Crops an image, by a specified amount, and saves it at a location."""
    original = Image.open(image_path)
    width, height = original.size
    box = (0, 0, width - crop_amount, height) # Defines new image dimensions.
    cropped_image = original.crop(box)
    print "    Saving cropped image at `{}`.".format(out_path)
    cropped_image.save(os.path.abspath(out_path))
    return None
    
def create_dirs(out_paths):
    """If a directory doesn't exist, create it."""
    import shutil
    for path in out_paths:
        if not os.path.exists(path[:-12]):
            os.makedirs(path[:-12])
        else:
            shutil.rmtree(path[:-12])
    return None    

def does_it_all(image_dict):
    """
    Uses all the functions and crops the color bar out of all the images...
    
    image_dict - a dictionary with all of the nessecary information.
       keys:
           "path" - the path to the directory with images to process.
           "bar_size" - the size of the area which needs to be cropped.
    """
    print "Beginning to crop color bar off images..."
    path_list, out_paths = define_out_paths(gather_image_paths(image_dict))
    create_dirs(out_paths)
    for num in range(len(path_list)):
        crop_image(path_list[num], out_paths[num], image_dict["bar_size"])
    print "\nFinished cropping images..."
    return None

if __name__ == "__main__":
    IMAGE_DIR = {"path": "../images/processed_images", "bar_size": 305}
    does_it_all(IMAGE_DIR)


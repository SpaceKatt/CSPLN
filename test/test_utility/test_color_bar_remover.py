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
    Tests the color bar remover for the set of images provided by Mary Keeler
        of Charles Sanders Pierce's Logic Notebook.

Inputs:
    Test image. "../test_processed_images"

Outputs:
    Test image w/o color bar, which is deleted in teardown.

Currently:

To Do:

Done:
"""

import sys
import os
import shutil
from PIL import Image
import webbrowser

basepath = os.path.dirname(__file__) # Path to this file. 
folderpath = os.path.abspath(os.path.join(basepath, "..", "..", "utility"))
sys.path.insert(0, folderpath) # Adding utility file to system path.
import color_bar_remover as c_b # Import from utitity file.

# Defining paths such that they many be defined relatively and called from
#     a directory that is not their own.
TEST_IMAGE_DIR = os.path.abspath(os.path.join(basepath, "..", 
                                 "test_processed_images"))
IMAGE_DICT = {"path":TEST_IMAGE_DIR, "bar_size":31}
TEST_IMAGE = os.path.abspath(os.path.join(basepath, "..", 
                             "test_processed_images/M2JT0000.tif"))
GENERATED_PATH = os.path.abspath(os.path.join(basepath, "..", 
                                 "test_processed_wcb_images/M2JTwcb0000.tif"))
CROP_IMAGE_DIR = os.path.abspath(os.path.join(basepath, "..", 
                                 "test_processed_wcb_images"))

def set_up():
    """
    Checks if test image exists and deletes previously 
        processed test image.
    """
    print "Begining test of color bar removal from notebook images..."
    print "_"*79
    if not os.path.exists(TEST_IMAGE):
        sys.exit("Test image does not exist!")
    if os.path.exists(CROP_IMAGE_DIR):
        shutil.rmtree(CROP_IMAGE_DIR)
    return None

def tear_down():
    """Deletes processed test image."""
    print "Ending test of color bar removal from notebook images..."    
    print "_"*79
    shutil.rmtree(CROP_IMAGE_DIR)
    return None

def test_color_bar_removal():
    """Tests the color bar removal function."""
    set_up()
    print "Gathering information from original image..."
    original = Image.open(TEST_IMAGE)
    orig_width, orig_height = original.size
    original.close()
    #print "Opening original image..."
    #webbrowser.open(os.path.abspath(TEST_IMAGE))

    print "Processing image...\n\n"    
    c_b.does_it_all(IMAGE_DICT)
    print "Gathering information from cropped color bar..."
    cropped_image = Image.open(GENERATED_PATH)    
    crop_width, crop_height = cropped_image.size
    cropped_image.close()
    assert orig_height == crop_height
    print "Height remains unchanged..."
    assert orig_width == (crop_width + IMAGE_DICT["bar_size"])
    print "Specified amount was cropped off image..."
    #print "Opening cropped image..."
    #webbrowser.open(os.path.abspath(GENERATED_PATH))
    tear_down()
    
if __name__ == "__main__":
    test_color_bar_removal()
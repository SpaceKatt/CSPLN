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

BASEPATH = os.path.dirname(__file__) # Path to this file.
FOLDERPATH = os.path.abspath(os.path.join(BASEPATH, "..", "..", "utility"))
sys.path.insert(0, FOLDERPATH) # Adding utility file to system path.
import color_bar_remover as c_b # Import from utitity file.

# Defining paths such that they many be defined relatively and called from
#     a directory that is not their own.
DIR_NAME = "test_processed_images"
TEST_IMAGE_DIR = os.path.abspath(os.path.join(BASEPATH, "..", DIR_NAME))
IMAGE_DICT = {"path":TEST_IMAGE_DIR, "bar_size":31}
TEST_PATH = "test_processed_images/M2JT0000.tif"
TEST_IMAGE = os.path.abspath(os.path.join(BASEPATH, "..", TEST_PATH))
GENERATED_NAME = "test_processed_wcb_images/M2JTwcb0000.tif"
GENERATED_PATH = os.path.abspath(os.path.join(BASEPATH, "..", GENERATED_NAME))
CROP_DIR = "test_processed_wcb_images"
CROP_IMAGE_DIR = os.path.abspath(os.path.join(BASEPATH, "..", CROP_DIR))

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
    shutil.rmtree(CROP_IMAGE_DIR)
    print "Ending test of color bar removal from notebook images..."
    print "_"*79
    return None

def gather_original_image_info():
    """Returns the original image dimensions."""
    print "Gathering information from original image..."
    original = Image.open(TEST_IMAGE)
    orig_width, orig_height = original.size
    original.close()
    return orig_width, orig_height

def crop_image():
    """Crops the original image and returns new cropped dimensions."""
    print "Processing image...\n"
    c_b.does_it_all(IMAGE_DICT)
    print "Gathering information from cropped image..."
    cropped_image = Image.open(GENERATED_PATH)
    crop_width, crop_height = cropped_image.size
    cropped_image.close()
    return crop_width, crop_height

def test_color_bar_removal():
    """Tests the color bar removal function."""
    set_up()
    orig_width, orig_height = gather_original_image_info()
    crop_width, crop_height = crop_image()
    assert orig_height == crop_height
    print "Height remains unchanged..."
    assert orig_width == (crop_width + IMAGE_DICT["bar_size"])
    print "Specified amount was cropped off image..."
    tear_down()
    return None

if __name__ == "__main__":
    test_color_bar_removal()

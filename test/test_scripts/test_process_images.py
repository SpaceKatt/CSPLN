# -*- coding: utf-8 -*-
r"""
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
    Unit test for `process_images.py`.
    Checks to see that the image is processed correctly,
        and that the meta data is written for the image.

Inputs:
    `../../scripts/process_images.py`

Outputs:
    Test results.

Currently:

To Do:

Done:
"""

import sys, os
from filecmp import cmp
from script_testing_definitions import return_testing_dictionary
from script_testing_definitions import resolve_relative_path as resolve_path
from script_testing_definitions import add_import_path
add_import_path()

import process_images, reset_system


def set_up(test_dict):
    """Sets up the testing environment."""    
    print "Begining test of processing raw notebook images..."
    print "\n        `process_images.py`"
    print "_"*79
    folderpath = resolve_path(__file__, "../../scripts")
    folderpath += "/null" # Necessary for the resolve_path fnc
    test_image_path = resolve_path(folderpath, test_dict["test_image_path"])
    if not os.path.exists(test_image_path):
        sys.exit("Testing image does not exist!")
    reset_system.delete_dirs_no_print(test_dict["generated_dirs"])
    return None
    
def tear_down(test_dict):
    """Tears down the testing environment."""
    print "\nEnding test of image processing...\n"
    reset_system.delete_dirs_no_print(test_dict["generated_dirs"])
    print "_"*79    
    return None
    
def check_file_meta(test_dict):
    """Checks the meta-dictionary for a single image."""
    image_name = test_dict["image_name_form"].format("0000")    
    known_data = resolve_path(__file__ , test_dict["test_known_data"])
    known_data = os.path.join(known_data, image_name + ".txt")
    test_meta = resolve_path(__file__ , test_dict["test_processed_img"])
    test_meta = os.path.join(test_meta, image_name, image_name + ".txt")
    with open(known_data, "r") as known:
        with open(test_meta, "r") as test:
            known_stuff = known.read()
            test_stuff = test.read()
            assert(known_stuff[-210:] == test_stuff[-210:])
    print "    ...individual image meta data confirmed."
    return None
    
def check_meta_existence(test_dict):
    """Checks the meta data for the test images."""
    print "\nTesting validity of meta_data..."
    meta_path = test_dict["test_meta_path"]
    known_data = test_dict["test_known_data"]
    known_png_info = resolve_path(__file__, known_data + "/png_sizes.txt")
    known_tif_info = resolve_path(__file__, known_data + "/tif_sizes.txt")
    test_png_info = resolve_path(__file__, meta_path + "/png_sizes.txt")
    test_tif_info = resolve_path(__file__, meta_path + "/tif_sizes.txt")
    assert(cmp(known_png_info, test_png_info))
    print "    ...png info successfully recorded."
    assert(cmp(known_tif_info, test_tif_info))
    print "    ...tif info successfully recorded."
    check_file_meta(test_dict)
    return None

def check_processed_image(test_dict):
    """Checks the processed test image."""
    print "\nTesting processed image's presence and naming validity..."
    out_path = resolve_path(__file__, test_dict["test_processed_img"])
    processed_image = os.listdir(out_path)[0]
    proper_file_name = test_dict["image_name_form"].format("0000")
    assert(processed_image == proper_file_name)
    print "    ...passed with name `{}`.".format(proper_file_name)
    file_list = os.listdir(os.path.join(out_path, proper_file_name))
    assert(proper_file_name + ".png" in file_list)
    print "    ...png image created."
    assert(proper_file_name + ".tif" in file_list)
    print "    ...tif image created."
    return None    
    
def test_process_images():
    """Tests the image processing component."""
    test_dict = return_testing_dictionary()    
    set_up(test_dict)
    try:
        process_images.in_summary(test_dict)
        check_meta_existence(test_dict)
        check_processed_image(test_dict)
    finally:
        tear_down(test_dict)
    return None

if __name__ == "__main__":
    test_process_images()
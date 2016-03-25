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
    Defines paths for testing.

Inputs:


Outputs:
    Dictionary that contain paths necessary for testing.

Currently:

To Do:

Done:
    Defined paths.
"""
import sys

def return_testing_dictionary():
    """Returns the dictionary to be used by all scripts testing."""
    dir_dict = {"web_apps":"../test/test_apps/web_apps",
                "images_processed":"../test/test_images/test_processed_images",
                "populators":"../test/test_populators",
                "test_meta":"../test/test_data",
                "test_app_path":"../test/test_apps"}
    image_name = "000602456_MS_am_1632_339_0588.tif"
    im_path = "../test/test_images/test_raw_tif/" + image_name
    test_dict = {"version":"00_01_02",
                 "generated_dirs":dir_dict,
                 "tif_path":"../test/test_images/test_raw_tif",
                 "out_path":"../test/test_images/test_processed_images",
                 "image_name_form":"M2JT{}",
                 "meta_path":"../test/test_data",
                 "pop_path":"../test/test_populators/{}_populator.py",
                 "app_path":"../apps/web_apps/{os}/{pat}",
                 "test_image_path":im_path,
                 "test_known_data":"../test_images/test_known_data",
                 "test_known_alt":"../test/test_images/test_known_data",
                 "test_processed_img":"../test_images/test_processed_images",
                 "test_meta_path":"../test_data",
                 "test_app_path":"../test/test_apps/{os}/{pat}"}
    return test_dict

def resolve_relative_path(curr_file, rel_path):
    """
    This function returns the absolute path defined by a relative path,
        and always relative from the file which calls this function.
            curr_file - takes `__file__` as an argument.
            rel_path  - is a relatively defined path which uses either
                            "/" or "\\" as separators, or both.
    The call of abspath(...) in the return statement might be redundant.
    """
    from os.path import join, normpath, abspath, dirname
    path_list = [dirname(curr_file)]
    rel_path = normpath(rel_path)
    if "/" in rel_path:
        split_path = rel_path.split("/")
    elif "\\" in rel_path:
        split_path = rel_path.split("\\")
    else:
        split_path = [".", rel_path]
    for splint in split_path:
        path_list.append(splint)
    path = reduce(join, path_list)
    return abspath(normpath(path))

def add_import_path():
    """Adds the import path for scripts directory."""
    folderpath = resolve_relative_path(__file__, "../../scripts")
    sys.path.insert(0, folderpath) # Adding scripts file to system path.

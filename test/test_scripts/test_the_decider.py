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
    Tests `the_decider.py` script.

Inputs:
    `the_decider.py` script.
    Definitions from `script_testing_definitions.py`

Outputs:
    Test results.

Currently:

To Do:

Done:
"""

from script_testing_definitions import return_testing_dictionary
from script_testing_definitions import add_import_path
add_import_path()

import the_decider, reset_system

def set_up(test_dict):
    """Sets up the testing environment."""
    print "Begining test of `the_decider`..."
    print "\n        `the_decider.py`"
    print "_"*79
    reset_system.delete_dirs_no_print(test_dict["generated_dirs"])
    return None

def tear_down(test_dict):
    """Tears down the testing environment."""
    print "\nEnding test of `the_decider`...\n"
    reset_system.delete_dirs_no_print(test_dict["generated_dirs"])
    print "_"*79
    return None

def validate_results(how_many, images_per_app):
    """
    Check to make sure that the_decider not only does not reccomend
        more images per app than are available, but also that it
        does not reccomend too many applications.
    """
    print "Testing allocation of images into applications..."
    assert how_many == images_per_app == 1
    print "    ...the correct allocation was given."
    return None

def test_the_decider():
    """Tests `the_decider` component."""
    test_dict = return_testing_dictionary()
    set_up(test_dict)
    test_dict["meta_path"] = test_dict["test_known_alt"]
    try:
        how_many, images_per = the_decider.the_decider(1, test_dict)
        validate_results(how_many, images_per)
    finally:
        tear_down(test_dict)
    return None

if __name__ == "__main__":
    test_the_decider()

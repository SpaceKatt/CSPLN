# -*- coding: utf-8 -*-
r"""
<license>
CSPLN_MaryKeelerEdition; Manages images to which notes can be added.
Copyright (C) 2015-2016, Thomas Kercheval

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
    Unit test for `create_web_apps_linux.py`,
        `../../scripts/create_web_apps_mac.py`,
        and `../../scripts/create_web_apps_win.py`.
    Checks that the scaffolding is being deployed properly.

Inputs:
    `../../scripts/create_web_apps_linux.py`
    `../../scripts/create_web_apps_mac.py`
    `../../scripts/create_web_apps_win.py`

Outputs:
    Test results.

Currently:

To Do:

Done:
"""

import sys, os
from script_testing_definitions import return_testing_dictionary
from script_testing_definitions import resolve_relative_path as resolve_path
from script_testing_definitions import add_import_path
add_import_path()

import reset_system, create_web_apps_win, create_web_apps_mac
import create_web_apps_linux


def set_up(test_dict):
    """Sets up the testing environment."""
    print "Begining test of web_app creation process..."
    print "\n        `../../scripts/create_web_apps_linux.py`"
    print "        `../../scripts/create_web_apps_mac.py`"
    print "        `../../scripts/create_web_apps_win.py`"
    print "_"*79
    reset_system.delete_dirs_no_print(test_dict["generated_dirs"])
    return None

def tear_down(test_dict):
    """Tears down the testing environment."""
    print "\nEnding test of web_app creation process...\n"
    reset_system.delete_dirs_no_print(test_dict["generated_dirs"])
    print "_"*79
    return None

def check_apps_exist(test_dict):
    """Checks to see that the apps were actually created."""
    oses = ["win", "mac", "linux"]
    part = "P1"
    print "\n"
    for oz in oses:
        app_path = "../" + test_dict["test_app_path"]
        app_path = resolve_path(__file__, app_path.format(os=oz, pat=part))
        assert os.path.exists(app_path)
        print "    {} web app successfully deployed.".format(oz)
    return None

def test_create_web_apps():
    """Tests the web_app creation component."""
    test_dict = return_testing_dictionary()
    set_up(test_dict)
    version_app = test_dict["version"]
    how_many_apps = 1
    try:
        create_web_apps_win.deploy_scaffolding(version_app, how_many_apps,
                                               test_dict["test_app_path"])
        create_web_apps_mac.deploy_scaffolding(version_app, how_many_apps,
                                               test_dict["test_app_path"])
        create_web_apps_linux.deploy_scaffolding(version_app, how_many_apps,
                                                 test_dict["test_app_path"])
        check_apps_exist(test_dict)
    finally:
        tear_down(test_dict)
    return None

if __name__ == "__main__":
    test_create_web_apps()

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
    Updates the README's in child directories, then updates the one in this
        directory.

Inputs:
    README files in subdirectories.

Outputs:
    README file in current directory.

Currently:
    Gather generated README's.

To Do:
    Generate README in current directory.

Done:
    Call lower README generating functions.
"""

import os, sys
from os.path import isfile, join

def discover_directories():
    """Discovers files in directory this file belongs to."""
    directories = []
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    print curr_dir
    subdirs = [x[0] for x in os.walk(curr_dir)]
    for dur in subdirs:
        if "README.txt" in os.listdir(dur) and dur[-4:] != "test":
            directories.append(dur)
    return directories

def check_condition(file_name):
    """Checks to see if the file_name is one which generates a README."""
    update = file_name[:6] == "update"
    readme = file_name[-9:] == "readme.py"
    return (update and readme)

def discover_readme_functions(dir_list):
    """
    From a list of directories, a list of README generating scripts
        is created.
    """
    readme_script_paths = []
    for dur in dir_list:
        files = [f for f in os.listdir(dur) if isfile(join(dur, f))]
        for fil in files:
            if check_condition(fil):
                readme_script_paths.append(join(dur, fil))
    return readme_script_paths

def call_readme_function(py_script):
    """Run the python script to generate a README file."""
    import subprocess
    master_cmd = ("python " + py_script).split(' ')
    print "_"*79
    print "Generating readme from script at {}\n".format(py_script)
    first = subprocess.Popen(master_cmd)
    first.communicate()
    return None

def generate_all_readmes(script_paths):
    for path in script_paths:
        call_readme_function(path)
    return None

def gather_readmes(directory_list):
    """
    From a list of direcotries, discover the `README.txt` files within them,
        then save them as values in a dictionary. The corresponding keys
        will be the name of the directory which contains them.
    """
    readme_dic = {}

    return readme_dic

def update_readmes():
    """
    Updates all README's in subdirectories, then the one in this file's
        directory.
    """
    directories = discover_directories()
    generate_all_readmes(discover_readme_functions(directories))
    readme_dic = gather_readmes(directories)


if __name__ == '__main__':
    update_readmes()

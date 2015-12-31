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
    Creating README text.

To Do:
    Generate README in current directory,
        form lower direcotry README's.
    Generate subREADME in current direcotry,
        to document scripts in this file.
    Include subREADME in README.
    Change so this script accepts a dictionary which defines which
        directories to recurse into for README updates.
            -or-
        Create a higher lever funtion which calls a function like this in
            all directories of interest. update vs __aggregate__

Done:
    Gather generated README's.
    Call lower README generating functions.
"""

import os
from os.path import isfile, join

def discover_directories():
    """Discovers files in directory this file belongs to."""
    directories = []
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    subdirs = [x[0] for x in os.walk(curr_dir)]
    for dur in subdirs:
        if "README.txt" in os.listdir(dur) and dur != curr_dir:
            directories.append(dur)
    return directories

def check_condition(file_name):
    """Checks to see if the file_name is one which generates a README."""
    update = file_name[:6] == "update"
    readme = file_name[-9:] == "readme.py"
    return update and readme

def discover_readme_functions(dir_list):
    """
    From a list of directories, a list of README generating scripts
        is created. These generating scripts must exist within one of the
        direcotries specified as an element of the directory list.
    """
    subpath = join(os.path.abspath(os.path.dirname(__file__)),
                   "subreadme.txt")
    readme_script_paths = [subpath]
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
    """For a list of paths, call the script located at each path."""
    for path in script_paths:
        call_readme_function(path)
    return None

def grab_lastpart_from_path(in_path):
    """Input a path, return last chunck"""
    import ntpath
    head, tail = ntpath.split(in_path)
    return tail or ntpath.basename(head)

def gather_readmes(directory_list):
    """
    From a list of direcotries, discover the `README.txt` files within them,
        then save their paths as values in a dictionary. The corresponding
        keys will be the name of the directory which contains them.
    """
    print "_"*79
    print "Gathering generated README's..."
    readme_dic = {}
    for dur in directory_list:
        print dur
        files = [f for f in os.listdir(dur) if isfile(join(dur, f))]
        for fil in files:
            if fil == "README.txt":
                dir_name = grab_lastpart_from_path(dur)
                readme_dic[dir_name] = join(dur, fil)
    return readme_dic

def grab_readme_snippet():
    """Grabs the text to go at the top of the README."""
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    with open(join(curr_dir, "readme_snippet.txt"), "r") as snippet:
        readme_snippet = snippet.read()
    return readme_snippet

def grab_subreadme():
    """Grabs the subreadme file in current direcotry."""
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    dir_name = grab_lastpart_from_path(curr_dir)
    title_string = "\n        README for {}".format(dir_name)
    subreadme = "_"*79 + "\n" + title_string + "\n" + "_"*79 + "\n\n"
    with open(join(curr_dir, "subreadme.txt"), "r") as sub:
        subreadme += sub.read()
    return subreadme

def grab_readme_text(readme_path):
    """Grabs the text out of a README, located at the path specified."""
    with open(readme_path, "r") as readme:
        readme_text = readme.read()
    return readme_text

def create_readme_text(readme_dic):
    """Creates the text to be written."""
    print "  Creating readme_text..."
    readme_text = grab_readme_snippet() + "\n" + grab_subreadme()
    direcotries = readme_dic.keys()
    for dur in direcotries:
        print "    Creating readme entry for README in {}".format(dur)
        title_string = "\n        README for {}".format(dur)
        readme_text += "_"*79 + "\n" + title_string + "\n" + "_"*79 + "\n"
        readme_text += "\n" + grab_readme_text(readme_dic[dur])
    readme_text += "_"*79
    return readme_text

def create_readme(readme_text):
    """Creates the README in the file's directory."""
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    with open(join(curr_dir, "README.txt"), "w") as readme:
        readme.write(readme_text)
    return None

def update_readmes():
    """
    Updates all README's in subdirectories, then the one in this file's
        directory.
    """
    print "_"*79
    print "\n                UPDATING README'S!!! :D"
    directories = discover_directories()
    generate_all_readmes(discover_readme_functions(directories))
    create_readme(create_readme_text(gather_readmes(directories)))
    print "\n                FINISHED UPDATING README's..."
    return None


if __name__ == '__main__':
    update_readmes()

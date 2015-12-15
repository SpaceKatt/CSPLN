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
    Replaces certian parts of python scripts that are suspected to cause
        problems between different operating systems.
    Be careful! This script doesn't create an archive, running it
        without proper care may cause a headache! Use proper string-
        escape notation.

Inputs:
    All scripts in this directory (other than self).

Outputs:
    All scripts, with specific words/phrases replaced.

Currently:

To Do:

Done:
'''

import os

def grab_scripts():
    """Grabs python scripts in the current directory."""
    file_list = os.listdir(os.getcwd())
    path_list = []
    for name in file_list:
        if name[-3:] == '.py':
            path_list.append(name)
    return path_list

def define_replacement():
    """Returns a dictionary of replacements to be made."""
    replacements = {'\\\\':'/', "doesn/'t":"doesn\\'t", '/n': '\\n'}
    return replacements

def replace_numbers(line, keys, rep_dict):
    """
    For every key in the dictionary,
        if the key is found in the current line,
            replace the key with its value.
    Always return the line.
    """
    for item in keys:
        if item in line:
            line = line.replace(item, rep_dict[item])
    return line

def replace_file_contents(path, rep_dic):
    """
    For a file and dictionary of replacements,
        perform said replacements and write over file.
    """
    keys = rep_dic.keys()
    lines_to_write = []
    with open(path, 'r') as file_now:
        for line in file_now:
            final_line = replace_numbers(line, keys, rep_dic)
            lines_to_write.append(final_line)
    with open(path, 'w') as file_again:
        for w_line in lines_to_write:
            file_again.write(w_line)
    return None

def main():
    """
    Grabs scripts in current directory, other than itself,
        and performs replacements on every one.
    """
    script_list = grab_scripts()
    rep_dict = define_replacement()
    print rep_dict
    for path in script_list:
        if path != 'os_script_modifier.py':
            replace_file_contents(path, rep_dict)

if __name__ == '__main__':
    main()

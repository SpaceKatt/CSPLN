'''
Description:

Inputs:

Outputs:

Currently:

To Do:

Done:
'''
'''
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
'''
import os

def grab_scripts():
    file_list = os.listdir(os.getcwd())
    path_list = []
    for name in file_list:
        if name[-3:] == '.py':
            path_list.append(name)
    return path_list

def define_replacement():
    replacements = {'\\':'/'}
    return replacements

def replace_numbers(line, keys, rep_dict):
    for item in keys:
        if item in line:
            line = line.replace(item, rep_dict[item])
    return line

def replace_file_contents(path, rep_dic):
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
    script_list = grab_scripts()
    rep_dict = define_replacement()
    for path in script_list:
        if path != 'os_script_modifier.py':
            replace_file_contents(path, rep_dict)

if __name__ == '__main__':
    main()

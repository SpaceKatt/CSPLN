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
    Changes the 'default/index.html' view to reflect the correct
        image numbers.

Inputs:
    Dictionary form {P_:[array]}, P_ referring to the specific web_app
        arrays consisting of image_file_paths.
    Existing web_apps with views.

Outputs:
    Changes the 'default/index.html' view to reflect the correct
        image numbers.

Currently:

To Do:

Done:
'''

import os

def gather_info(app_part, first_path):
    """
    Determines which is the first image number to appear in
        a specific application.
    """
    first_num = first_path[-8:-4]
    while first_num[0] == str(0) and len(first_num) > 1:
        first_num = first_num[1:]
    index_print = "    The first image number in this index is: {first}"
    print index_print.format(first=first_num)
    return app_part, first_num

def grab_view_path(which_app, w_os):
    """Grabs the path of the view file to be modified."""
    if w_os == 'mac':
        app_dir = '../apps/web_apps/{os}/{app}/web2py/{ext}/applications'
        extra = 'web2py.app/Contents/Resources'
        app_dir = app_dir.format(os=w_os, app=which_app, ext=extra)
        file_loc = 'MKE_Static_Name/views/default/index.html'
        path = os.path.join(app_dir, file_loc)
    else:
        app_dir = '../apps/web_apps/{os}/{app}/web2py/applications'
        app_dir = app_dir.format(os=w_os, app=which_app)
        file_loc = 'MKE_Static_Name/views/default/index.html'
        path = os.path.join(app_dir, file_loc)
    return path

def define_replacement(first_num):
    """
    Defines the replacement to be made to the starting index in the
        view file to be modified.
    """
    replacements = {' N = 0 ':' N = {} '.format(first_num)}
    return replacements

def replace_numbers(line, keys, rep_dict):
    """Does the replacement, in a line."""
    for item in keys:
        if item in line:
            line = line.replace(item, rep_dict[item])
    return line

def replace_file_contents(path, rep_dic):
    """
    Cycles through the lines in a file, calls replacement function
        for each line. Writes lines after cycle is complete.
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

def replace_view(app_part, first_path, w_os):
    """
    Facilitates the correction of file index numbers. Without this every
        application would start off by saying it had image zero as its
        first image.
    """
    which_app, first_num = gather_info(app_part, first_path)
    path = grab_view_path(which_app, w_os)
    rep_dict = define_replacement(first_num)
    replace_file_contents(path, rep_dict)
    print "Finished {part}.\n".format(part=app_part) + "_"*79
    return None

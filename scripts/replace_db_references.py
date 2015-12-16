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
    Replaces references to old databases in the scaffolding with references
        to the updated db_schema.
    Does this with dictionaries, mapping more complicated replacements
        before switching out simpler references.

Inputs:
    Dictionaries to map replacements (contained within this script).
    Scaffolding version, more specifically the files within the scaffolding
        that need this change.

Outputs:
    Files that have undergone operation will be written back into their
        respective places. And hopefully the web_apps will run!

Currently:

To Do:

Done:
    Create replacement dictionaries.
    Read files, search for things in need of replacement,
        do replacement, write files.
'''

import os

def check_file_exist(path):
    """Check if the file at the given path exists."""
    if os.path.exists(path):
        print path, 'exists!'
    else:
        import sys
        sys.exit('File {} doesn\'t exist'.format(path))
    return None

def grab_replacement_dictionaries():
    """
    Defines replacements to be made, seperates them by how many layers
        of specificity is given. Less specific replacements should take
        place after more specific replacements are made.
    """
    more_complex = {
        'page.title':'image.name', 'page.file':'image.file',
        'comment.page_id':'note.image_id', 'comment.author':'note.user_id',
        'comment.email':'note.email', 'comment.body':'note.body_text',
        'page.id':'image.id'
        }
    less_comp = {'page':'image', 'comment':'note'}
    return more_complex, less_comp

def grab_files_tobe_replaced(version):
    """
    Grabs the paths of files where database reference replacement
        is needed.
    """
    paths = []
    controllers = '../apps/scaffolding/version/MKE_v{}/controllers/default.py'
    views_dir = '../apps/scaffolding/version/MKE_v{ver}/views/{vfile}'
    views = ['default/show.html', 'default/index.html', ]
    paths.append(controllers.format(version))
    for path in views:
        paths.append(views_dir.format(ver=version, vfile=path))
    return paths

def replace_complex(line, keys, rep_dict):
    """Replaces the more specific items found in a line."""
    for item in keys:
        if item in line:
            line = line.replace(item, rep_dict[item])
    return line

def replace_less_complex(line, lesser_keys, less_dic):
    """Replaces the less specific items found in a line."""
    for lesser_item in lesser_keys:
        if lesser_item in line:
            line = line.replace(lesser_item, less_dic[lesser_item])
    return line

def replace_file_contents(path, rep_dic, less_rep):
    """For a given file, performs the necessary replacements."""
    keys = rep_dic.keys()
    lesser_keys = less_rep.keys()
    lines_to_write = []
    with open(path, 'r') as file_now:
        for line in file_now:
            new_line = replace_complex(line, keys, rep_dic)
            final_line = replace_less_complex(new_line, lesser_keys, less_rep)
            lines_to_write.append(final_line)
    with open(path, 'w') as file_again:
        for w_line in lines_to_write:
            file_again.write(w_line)
    return None

def replace_db_references(version):
    """
    For a specific version of the scaffolding application,
        gathers the specified replacements and performs them.
    Is only necessary to run this when working with unaltered
        web2py framework.
    """
    replacements, lesser_rep = grab_replacement_dictionaries()
    paths = grab_files_tobe_replaced(version)
    for path in paths:
        print '\n\n\n', path, '\n\n\n'
        check_file_exist(path)
        replace_file_contents(path, replacements, lesser_rep)
    return None

if __name__ == "__main__":
    VERSION = '00_01_02'
    replace_db_references(VERSION)

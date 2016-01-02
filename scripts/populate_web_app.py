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
    Populates single web_app with images,
        use interactive python environment w\web2py.
    Will be used by another module 'x', module 'x' will decide
        how_many_apps to create and how_many_images_per_app, which will
        determine how 'x' calls populate_web_app.
    Saves generated cmds to '.\populators', which are run in an environment
        which is populated by the db objects of the corresponding web_app.

Inputs:
    Specific images in '../image/processed_images'
    Specific web_app, and its database: 'image'.

Outputs:
    Populated database in specified web_app.

Currently:

To Do:

Done:
    Gather all relevant image information in a dictionary:
        {'png_md5':{png_md5}, 'name': {name}, 'png_size': {size},
         'tif_parent_md5': {tif_md5}, 'tif_parent_size': {tif_size},
         'file_path': {file_path}
         }
    Find way to upload images from command line,
        specifically from an interactive python shell.
        Will look like:
            db.image.insert(SOMETHING)
    Verify database gets populated correctly.
    Find way to pass generated commands to interpreter spawned from
        running web2py.py scripts to interact with web_app.
            Asked question on stackoverflow. (answered by Anthony)

"""

import os, sys
from the_decider import resolve_relative_path as resolve_path

def check_file_exist(path):
    """Check if the file at the given path exists."""
    if os.path.exists(path):
        pass
    else:
        sys.exit('File {} doesn\'t exist'.format(path))
    return None

def create_dirs(out_path):
    """If a directory doesn't exist at the specified path, create one."""
    if not os.path.exists(out_path):
        os.makedirs(out_path)

def check_images_exist(which_images):
    """For every specified file, check its existence."""
    for path in which_images:
        check_file_exist(path)
    return None

def grab_filename_from_path(in_path):
    """Input a path, return last chunck"""
    import ntpath
    head, tail = ntpath.split(in_path)
    return tail or ntpath.basename(head)

def grab_web2py_script_path(which_app, w_os):
    """
    For a list of operating systems, get the path of the web2py.py
        script for a specified application.
    """
    if w_os == 'mac':
        path_form = '../apps/web_apps/{os}/{app}/web2py/{maaa}/web2py.py'
        path_form = resolve_path(__file__, path_form)
        extra = 'web2py.app/Contents/Resources'
        path = path_form.format(os=w_os, app=str(which_app), maaa=extra)
    else:
        path_form = '../apps/web_apps/{os}/{app}/web2py/web2py.py'
        path_form = resolve_path(__file__, path_form)
        path = path_form.format(os=w_os, app=str(which_app))
    print "    web2py script path: {}\n".format(path)
    return path

def grab_txt(image_name, out_path):
    """Grabs metadata for a specified image and stores it as a dictionary."""
    import ast
    image_path_form = out_path + '/{name}/{name}.txt'
    image_path_form = resolve_path(__file__, image_path_form)
    with open(image_path_form.format(name=image_name), 'r') as meta_f:
        dic_str = meta_f.read()
        dictionary = ast.literal_eval(dic_str)
    return dictionary

def resolve_file_path(relative_path, ext):
    """From a relative_path and file extention, creates an absolute path."""
    path_interim = relative_path + ext
    abs_path = os.path.abspath(path_interim)
    return abs_path

def gather_png_info(image_path, out_path):
    """Retrieves and modifies png metadata, for further processing."""
    image_name_ext = grab_filename_from_path(image_path)
    image_name = image_name_ext[:-4]
    meta_dict = grab_txt(image_name, out_path)
    meta_dict['file'] = resolve_file_path(meta_dict['file'], '.png')
    return meta_dict

def create_single_cmd(image_path, out_path):
    """
    Creates a single command, which is used to put a single entry
        into a single database, for a specific application.
    """
    png_info = gather_png_info(image_path, out_path)
    keys = png_info.keys()
    insert_form = '{field}={value}'
    insert_cmd = 'db.image.insert({stuff})'
    insert_list = []

    print "Preparing {} for insertion...".format(png_info['name'])
    for key in keys:
        if key == 'file':
            object_file = "open('{}', 'rb')".format(png_info[key])
            single_cmd = insert_form.format(field=key, value=object_file)
            insert_list.append(single_cmd)
        elif isinstance(png_info[key], str):
            val = "'{}'".format(png_info[key])
            singlecmd = insert_form.format(field=key, value=val)
            insert_list.append(singlecmd)
        else:
            singlecmd = insert_form.format(field=key, value=png_info[key])
            insert_list.append(singlecmd)

    insert_string = ''
    for part in insert_list:
        if insert_string == '':
            insert_string = part
        else:
            insert_string = insert_string + ', ' + part

    cmd = insert_cmd.format(stuff=insert_string)
    return cmd

def create_cmds(web2py_script, which_images, out_path):
    """
    Creates an initial command, a series of insert commands, and
        a final commit command. These are relevant to a list of images
        to be inserted, and a specific webapp to be populated.
    """
    int_cmd = 'python {web2py_s} -S MKE_Static_Name -M -R '
    int_cmd = int_cmd.format(web2py_s=web2py_script)
    upload_cmds = []
    for image in which_images:
        cmd = create_single_cmd(image, out_path)
        upload_cmds.append(cmd)
    commit_cmd = 'db.commit()'
    return int_cmd, upload_cmds, commit_cmd

def create_python_scripts(up_cmds, commit_cmd, which_app, pop_path):
    """
    Creates a script, from a series of commands,
        to be read by an interpreter.
    """
    path_form = resolve_path(__file__, pop_path)
    path = os.path.abspath(path_form.format(which_app))
    create_dirs(path_form[:-15])
    with open(path, 'w') as python_file:
        for cmd in up_cmds:
            python_file.write(cmd + '\n')
        python_file.write('\n' + commit_cmd + '\n')
    return path


def pass_cmds(int_cmd, py_pop):
    """Run py_pop commands in a web2py environment spawned by int_cmd."""
    import subprocess
    master_cmd = (int_cmd + py_pop).split(' ')
    print "\n    Communicating insertions...\n"
    first = subprocess.Popen(master_cmd)
    first.communicate()
    return None

def populate_web_app(which_app, which_images, w_os, adict):
    """
    Runs everything, populates a single webapp with a set of images,
        for a specific operating system.
    """
    string_print = "\n    Now populating {which} of the {oz} application."
    print string_print.format(which=which_app, oz=w_os)
    print "_"*79 + "\n"
    check_images_exist(which_images)
    web2py = os.path.abspath(grab_web2py_script_path(which_app, w_os))
    out_path = adict["out_path"]
    pop_path = adict["pop_path"]
    int_cmd, up_cmds, commit_cmd = create_cmds(web2py, which_images, out_path)
    py_pop = create_python_scripts(up_cmds, commit_cmd, which_app, pop_path)
    pass_cmds(int_cmd, py_pop)
    return None

if __name__ == "__main__":
    WHICH_APP = 'P1'
    WHICH_IMAGES = ['../images/processed_images/M2JT0000/M2JT0000.png',
                    '../images/processed_images/M2JT0001/M2JT0001.png',
                    '../images/processed_images/M2JT0002/M2JT0002.png']
    W_OS = 'mac'
    AUTO_DICT = {"out_path":"../images/processed_images",
                 "pop_path":"./populators/{}_populator.py"}
    populate_web_app(WHICH_APP, WHICH_IMAGES, W_OS, AUTO_DICT)

'''
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

def check_file_exist(path):
    if os.path.exists(path):
        print path, 'exists!'
    else:
        sys.exit('File {} doesn\'t exist'.format(path))
    return None

def create_dirs(out_path):
    if not os.path.exists(out_path):
	    os.makedirs(out_path)

def check_images_exist(which_images):
    for path in which_images:
        check_file_exist(path)
    return None

def grab_filename_from_path(in_path):
    '''Input a path, return last chunck'''
    import ntpath
    head, tail = ntpath.split(in_path)
    return tail or ntpath.basename(head)

def grab_web2py_script_path(which_app, w_os):
    path_form = '../apps/web_apps/{os}/{app}/web2py/web2py.py'
    path = path_form.format(os=w_os, app=str(which_app))
    return path

def grab_txt(image_name):
    image_path_form = '../images/processed_images/{name}/{name}.txt'
    with open(image_path_form.format(name=image_name), 'r') as meta_f:
        dic_str = meta_f.read()
        dictionary = eval(dic_str)
    return dictionary

def resolve_file_path(relative_path, ext):
    path_interim = relative_path + ext
    abs_path = os.path.abspath(path_interim)
    return abs_path

def gather_png_info(image_path):
    image_name_ext = grab_filename_from_path(image_path)
    image_name = image_name_ext[:-4]
    meta_dict = grab_txt(image_name)
    meta_dict['file'] = resolve_file_path(meta_dict['file'], '.png')
    return meta_dict

def create_single_cmd(image_path):
    png_info = gather_png_info(image_path)
    keys = png_info.keys()
    insert_form = '{field}={value}'
    insert_cmd = 'db.image.insert({stuff})'
    insert_list = []
    for key in keys:
        if key == 'file':
            object_file = "open('{}', 'rb')".format(png_info[key])
            single_cmd = insert_form.format(field=key, value=object_file)
            insert_list.append(single_cmd)
        elif type(png_info[key]) == str:
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

def create_cmds(web2py_script, which_images):
    int_cmd = 'python {web2py_s} -S MKE_Static_Name -M -R '
    int_cmd = int_cmd.format(web2py_s=web2py_script)
    upload_cmds = []
    for image in which_images:
        cmd = create_single_cmd(image)
        upload_cmds.append(cmd)
    commit_cmd = 'db.commit()'
    return int_cmd, upload_cmds, commit_cmd

def create_python_scripts(up_cmds, commit_cmd, which_app):
    path_form = './populators/{}_populator.py'
    path = os.path.abspath(path_form.format(which_app))
    create_dirs(path_form[:-15])
    with open(path, 'w') as python_file:
        for cmd in up_cmds:
            python_file.write(cmd + '\n')
        python_file.write('\n' + commit_cmd + '\n')
    return path


def pass_cmds(int_cmd, py_pop):
    import subprocess
    master_cmd = (int_cmd + py_pop).split(' ')
    first = subprocess.Popen(master_cmd)
    first.communicate()
    return None

def populate_web_app(which_app, which_images, w_os):
    check_images_exist(which_images)
    web2py = os.path.abspath(grab_web2py_script_path(which_app, w_os))
    int_cmd, up_cmds, commit_cmd = create_cmds(web2py, which_images)
    py_pop = create_python_scripts(up_cmds, commit_cmd, which_app)
    pass_cmds(int_cmd, py_pop)
    return None

if __name__ == "__main__":
    which_app = 'P6'
    which_images = ['../images/processed_images/M2JT0000/M2JT0000.png',
                    '../images/processed_images/M2JT0001/M2JT0001.png',
                    '../images/processed_images/M2JT0002/M2JT0002.png'
                    ]
    w_os = 'win'
    populate_web_app(which_app, which_images, w_os)

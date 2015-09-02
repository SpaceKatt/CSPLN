'''
THIS SCRIPT DOESN'T WORK! (yet)

Description:
    Populates single web_app with images,
        use interactive python environment w/web2py.
    Will be used by another module 'x', module 'x' will decide
        how_many_apps to create and how_many_images_per_app, which will
        determine how 'x' calls populate_web_app.

Inputs:
    Specific images in '..\\image\\processed_images'
    Specific web_app, and its database: 'image'.

Outputs:
    Populated database in specified web_app.

Currently:
    Find way to pass generated commands to interpreter spawned from
        running web2py.py scripts to interact with web_app.
            Asked question on stackoverflow.

To Do:
    Verify database gets populated correctly.

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

which_app = 'P5'
which_images = ['..\\images\\processed_images\\M2JT0000\\M2JT0000.png',
                '..\\images\\processed_images\\M2JT0001\\M2JT0001.png',
                '..\\images\\processed_images\\M2JT0002\\M2JT0002.png'
                ]

which_im = ['M2JT0000', 'M2JT0001']

def check_file_exist(path):
    if os.path.exists(path):
        print path, 'exists!'
    else:
        sys.exit('File {} doesn\'t exist'.format(path))
    return None

def check_images_exist(which_images):
    for path in which_images:
        check_file_exist(path)
    return None

def grab_filename_from_path(in_path):
    '''Input a path, return last chunck'''
    import ntpath
    head, tail = ntpath.split(in_path)
    return tail or ntpath.basename(head)

def grab_web2py_script_path(which_app):
    path_form = '..\\apps\\web_apps\\{}\\web2py\\web2py.py'
    path = path_form.format(str(which_app))
    return path

def grab_txt(image_name):
    image_path_form = '..\\images\\processed_images\\{name}\\{name}.txt'
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

def create_cmds(which_app, web2py_script, which_images):
    int_cmd = 'python {} -S MKE_Static_Name -M'.format(web2py_script)
    upload_cmds = []
    for image in which_images:
        cmd = create_single_cmd(image)
        upload_cmds.append(cmd)
    commit_cmd = 'db.commit()'
    return int_cmd, upload_cmds, commit_cmd

def pass_cmds(int_cmd, up_cmds, commit_cmd):
    import subprocess, time
    print int_cmd
    #first = subprocess.Popen(int_cmd, stdin=subprocess.PIPE, shell=True)
    #for cmd in up_cmds:
    #    time.sleep(0.5)
    #    first.stdin.write(cmd)
        #print cmd
        #first.communicate(up_cmds)
    #print commit_cmd
    #first.communicate(commit_cmd)
    return None

def populate_web_app(which_app, which_images):
    check_images_exist(which_images)
    web2py = grab_web2py_script_path(which_app)
    int_cmd, up_cmds, commit_cmd = create_cmds(which_app, web2py, which_images)
    print int_cmd, '\n\n', up_cmds, '\n\n', commit_cmd
    up_cmdsj = ["db.image.insert(md5='1689ed6f239701c7921beda212abf73f', name='M2JT0002', size=10078429, tif_parent_md5='c39828230d3436717109ab69dc3fcd30', file=open('C:\Users\Thomas\Desktop\CSPLN_Final\images\processed_images\M2JT0002\M2JT0002.png', 'rb'), size_tiff_parent=30500872)"]
    #pass_cmds(int_cmd, up_cmds, commit_cmd)
    return None


populate_web_app(which_app, which_images)

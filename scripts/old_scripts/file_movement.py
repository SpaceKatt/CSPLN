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

import os, sys, shutil

def grab_filename_from_path(in_path):
    '''Input a path, return last chunck'''
    import ntpath
    head, tail = ntpath.split(in_path)
    return tail or ntpath.basename(head)

def check_file_exist(path):
    if os.path.exists(path):
        print path, 'exists!'
    else:
        sys.exit('File {} doesn\'t exist'.format(path))

def grab_path_list(out_path, filename):
    '''From a designated out_path, create a
	new path for every part of the CSPLN project'''
    path_list = []
    for part in range(1, 11):
        spec_path = out_path.format(part)
        spec_path = os.path.join(spec_path, filename)
        path_list.append(spec_path)
    return path_list

def get_current_date():
    import datetime
    now = datetime.datetime.now()
    nowtime = now.isoformat()
    return nowtime[0:-7]

def date_copy(filename, path, archive_path):
    '''For every path of the CSPLN,
    copy the file to be replaced, add a timestamp to
    its path first. Then delete file.'''
    time = get_current_date()
    time = time.replace(':', '_')
    filename = time + filename
    archive_path = os.path.join(archive_path, filename)
    shutil.copy2(path, archive_path)
    os.remove(path)
    string = "Deleted {a}, archived to {b}."
    print string.format(a=path, b=archive_path)

def create_dirs(out_path):
    if not os.path.exists(out_path):
	    os.makedirs(out_path)

def copy_in_to_final(in_path, out_path):
    print in_path
    shutil.copy2(in_path, out_path)

def do_stuff(in_path, out_path, archive_path):
    check_file_exist(in_path)
    filename = grab_filename_from_path(in_path)
    out_paths = grab_path_list(out_path, filename)
    for path in out_paths:
        if os.path.exists(path):
            specific_archive = date_copy(filename, path, archive_path)
        copy_in_to_final(in_path, path)


def just_do_it():
    nowpath = os.path.dirname(os.getcwd())
    inpath = os.path.join(nowpath, 'admin\\widgt.py')
    outpath = os.path.join(nowpath, 'P{}\\web2py\\gluon')
    archpath = os.path.join(nowpath, 'archive')
    do_stuff(inpath, outpath, archpath)

just_do_it()

#def ask_for_stuff():
#    in_path = raw_input('What is the abspath of the in file? ')
#	print '''To enter in out_path, use following format:
#	P{}/gluon/etc...'''

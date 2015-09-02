'''Starting in .../CSPLN/admin;

Discover number of CSPLN apps, store quantity as an integer.

Grab all update_file_paths in ./updates, add them to a list.

for update_element in update_path_list:
    1: check_update_path_exist
    2: split path of update_element into (dirpath, filename)
    3: for each CSPLN app:
           create a specific out_path #(e.g., ../P_10/dirpath/filename)
           add out_path to a list -> out_paths
    4: for out_path in out_paths:
           if out_path is an existing file:
               timestamp&&archive -> ../archive/dirpath/timestamp&&filename
           copy update_element to out_path
    5: copy update_element to ./updated/dirpath/timestamp&&filename
    6: delete update_element from ./updates

This process allows us to automate the update process,
    without having to change any code or add input for new cases.
Archiving is done when files are replaced,
    and when updates are first introduced (since they may be modified
    before they are replaced).
To prepare files for update, drag and drop them into ./updates,
    nested within their corresponding directory path(s) from the CSPLN apps.
        (Should automate this step.)
To update files, run this script!
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

import os, sys, shutil

def how_many_cspln_apps():
    dir_list = []
    for name in os.listdir('..'):
        dir_list.append(name)
    num_of_apps = 0
    for name in dir_list:
        if name[0] == 'P':
            num_of_apps += 1
    return int(num_of_apps)

def grab_update_paths():
#    filename_list = []
#    dir_list = []
    update_path_list = []
    for root, dirs, files in os.walk(".\\updates", topdown=False):
        del dirs
        for name in files:
            update_path_list.append((os.path.join(root, name)))
#            filename_list.append(name)
#        for name in dirs:
#            dir_list.append((os.path.join(root, name)))
    return update_path_list#, dir_list, filename_list

def check_file_exist(path):
    if os.path.exists(path):
        print path, 'exists!'
    else:
        sys.exit('File {} doesn\'t exist'.format(path))

def get_current_date():
    import datetime
    now = datetime.datetime.now()
    nowtime = now.isoformat()
    nowtime = nowtime.replace(':', '_')
    return nowtime[0:-7]

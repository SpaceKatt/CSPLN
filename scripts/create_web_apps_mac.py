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
    For creating CSPLN webapps for MACINTOSH, from scaffolding.

Inputs:
    Version number, of MKE_vxx_xx_xx scaffolding file.
        Where each x corresponds to a current version number.
        Input as "xx_xx_xx"
    Number of web applications

Outputs:
    Web applications, number depends on Input.
    Puts web2py.py in each web_app (not included in windows version).
    Puts scaffolding (current app version) into each web2py frame.
    Renames scaffolding application to 'MKE_Static_Name'.

Currently:

To Do:

Done:
'''

import os, sys, shutil
from the_decider import resolve_relative_path as resolve_path

def check_file_exist(path):
    """Check if the file at the given path exists."""
    if os.path.exists(path):
        pass
    else:
        sys.exit('File {} doesn\'t exist'.format(path))
    return None

def grab_out_paths(number_apps):
    """
    From the number of applications necessary,  create a list
        of pathnames where we will create mac applications.
    """
    out_dir = resolve_path(__file__, '../apps/web_apps/mac/{pat}')
    project_part = 'P{}'
    out_paths = []
    for num in range(1, number_apps + 1):
        strin = project_part.format(str(num))
        print "{part}, preparing for generation.".format(part=strin)
        out_paths.append(out_dir.format(pat=strin))
    return out_paths

def grab_web2py_frame():
    """Grab the path of the web2py framework and check its existence."""
    webframe = resolve_path(__file__, '../apps/scaffolding/mac/web2py')
    check_file_exist(webframe)
    return webframe

def grab_scaffold_app(version):
    """Grab the path of our scaffolding and check its existence."""
    mkever = '../apps/scaffolding/version/MKE_v{}'.format(version)
    mkever = resolve_path(__file__, mkever)
    check_file_exist(mkever)
    return mkever

def copy_webframez(num_apps):
    """
    For each path where we intend to create a mac application,
        create a copy of the web2py framework.
    """
    webframe = grab_web2py_frame()
    out_paths = grab_out_paths(num_apps)
    mac_path = 'web2py'
    for path in out_paths:
        shutil.copytree(webframe, os.path.join(path, mac_path))
        print '    web2py frame copied to: {}'.format(path)
    return out_paths

def modify_out_paths(int_paths):
    """
    Modifies the out_paths from the locations of the web2py framework
        to where our applications will be generated.
    """
    mod_out = []
    addition = 'web2py/web2py.app/Contents/Resources/applications'
    for path in int_paths:
        new_path = os.path.join(path, addition)
        mod_out.append(new_path)
    return mod_out

def grab_filename_from_path(in_path):
    """Input a path, return last chunck"""
    import ntpath
    head, tail = ntpath.split(in_path)
    return tail or ntpath.basename(head)

def copy_app(version, out_paths):
    """
    Creates an application for every copy of the web2py framework,
        from scaffolding application.
    """
    scaff_app = grab_scaffold_app(version)
    filename = grab_filename_from_path(scaff_app)
    for path in out_paths:
        shutil.copytree(scaff_app, os.path.join(path, filename))
        old_name = os.path.join(path, filename)
        new_name = os.path.join(path, 'MKE_Static_Name')
        os.rename(old_name, new_name)
    return None

def deploy_scaffolding(current_version, num_apps):
    """
    Deploys the web2py framework and the current version of our
        scaffolding, as many times as is necessary.
    """
    print "\n    Creating Mac applications...\n" + "_"*79
    out_paths = copy_webframez(num_apps)
    new_paths = modify_out_paths(out_paths)
    copy_app(current_version, new_paths)
    print "_"*79
    return None

if __name__ == "__main__":
    NUM_APPS = 2
    VERSION = '00_01_02'
    deploy_scaffolding(VERSION, NUM_APPS)

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
    Does it all! (more descriptive description later)

Inputs:
    All the scripts!
    Version number of current scaffolding_app
    Images in '../images/raw_tiff'
    OS Versions of web2py framework in '../scaffolidng'

Outputs:
    All the things!
    All populated web_apps.
    The final project output, for Linux, Mac, and Windows.
    Updates README

Currently:

To Do:
    Rewrite Description, Inputs, and Outputs.
    Create version_search, which determines most up to date version.

Done:
'''

import create_web_apps_win
import create_web_apps_mac
import create_web_apps_linux
import image_path_chunk_grabber as impcg
import populate_web_app as popu
import process_images
import the_decider as t_d
import view_change as v_c
import update_readme

import os

def discover_how_many_tifs():
    """Discovers how many tiffs are intended to be processed."""
    dir_list = os.listdir('../images/raw_tiff')
    number_images_to_process = len(dir_list)
    return number_images_to_process

def prepare_png_images():
    """
    Processes raw tiff images, creates png images for web_apps.
    Creates data for web_app database population.
    Decides how png images will be distributed between a number of apps.
    """
    total_image_num = discover_how_many_tifs()
    process_images.in_summary()
    how_many_apps, images_per_app = t_d.the_decider(total_image_num)
    return how_many_apps, images_per_app

def create_web_app_population(version_app, how_many_apps, images_per_app):
    """
    Creates web_apps for Linux, Windows, and Mac. (from scaffolding)
    Populates web_apps with png images and corresponding data.
    """
    os_list = ['win', 'mac', 'linux']
    create_web_apps_win.deploy_scaffolding(version_app, how_many_apps)
    create_web_apps_mac.deploy_scaffolding(version_app, how_many_apps)
    create_web_apps_linux.deploy_scaffolding(version_app, how_many_apps)
    dict_image_p = impcg.image_path_chunk_grabber(images_per_app)
    for w_os in os_list:
        for key_part in dict_image_p:
            popu.populate_web_app(key_part, dict_image_p[key_part], w_os)
            v_c.replace_view(key_part, dict_image_p[key_part][0], w_os)
    return None

def final(curr_version):
    """Runs everything. Updates README.txt"""
    how_many_apps, images_per_app = prepare_png_images()
    print '\nApps nessecary: ', how_many_apps
    print '\nImages per app: ', images_per_app, '\n'
    create_web_app_population(curr_version, how_many_apps, images_per_app)
    print "\n    Finished, now updating readme...\n"
    update_readme.update_readme()
    return None

if __name__ == "__main__":
    TEST_VERSION = '00_01_02'
    final(TEST_VERSION)

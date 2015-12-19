"""
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
    Deletes all generated files.
    Resets the system for further testing.

Inputs:
    Generated files.

Outputs:
    Environment fresh for generation.

Currently:


To Do:

Done:
    Resets the system so `./automate_everything.py` may be run
"""

import shutil

def grab_directories_deletion_paths():
    """Contains directory paths to be deleted."""
    web_apps = "../apps/web_apps"
    images_processed = "../images/processed_images"
    return web_apps, images_processed

def delete_directories():
    """Resets system so further files may be deleted."""
    print "Resetting system...\n"
    for path in grab_directories_deletion_paths():
        print "Deleteing {}.".format(path)
        shutil.rmtree(path)
    return None

if __name__ == '__main__':
    delete_directories()

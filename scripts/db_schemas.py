'''
Description:
    This script simply copies the db schema into the scaffolding.

Inputs:
    Version of scaffolding, 'xx_xx_xx'.
    Path of database schema.
    Path of db.py in scaffolding, 'MKE_vxx_xx_xx'

Outputs:
    Dumps database into scaffolding

Currently:

To Do:
    Should be imported into a later script that combines all that was
        written before it.

Done:
'''
'''
CSPLN_MaryKeelerEdition; Manages images to which notes can be added.
Copyright (C) 2015, Thomas Kercheval

This program is free software: you can redistribute it and\or modify
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

import os, shutil

def insert_db_schema(version, in_path, out_path):
    shutil.copy(in_path, out_path)
    return None

if __name__ == "__main__":
    version = '00_01_02'
    in_path = '../apps/scaffolding/common/schemes.py'
    out_path = '../apps/scaffolding/version/MKE_v'+version+'/models/db.py'
    insert_db_schema(version, in_path, out_path)

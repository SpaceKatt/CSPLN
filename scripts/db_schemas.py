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
    This script simply copies the db schema into the scaffolding.

Inputs:
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

import shutil

def insert_db_schema(in_path, out_path):
    """Replaces db schema. Doesn't need to run everytime."""
    shutil.copy(in_path, out_path)
    return None

if __name__ == "__main__":
    VERSION = '00_01_02'
    IN_PATH = '../apps/scaffolding/common/schemes.py'
    OUT_PATH = '../apps/scaffolding/version/MKE_v'+VERSION+'/models/db.py'
    insert_db_schema(IN_PATH, OUT_PATH)

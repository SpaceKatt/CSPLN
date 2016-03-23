# -*- coding: utf-8 -*-
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
    Runs all the tests for the utility module.

Inputs:
    Tests in `test_utility` folder.

Outputs:
    Test results

Currently:

To Do:

Done:
"""

import test_utility.test_color_bar_remover as t_c_b

def run_tests():
    """Runs all tests of utility functions."""
    t_c_b.test_color_bar_removal()

if __name__ == "__main__":
    run_tests()

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
    Updates README.txt file in the specified directory.

Inputs:
    Functions that are in the specified directory.
        discover_functions() detects them automatically.

Outputs:
    README.txt file, with Scope&&Details listed.
        Covers functions in specified directory.

Currently:

To Do:

Done:
    Update readme file with current functions&&their docstrings.
"""

import os

def discover_functions(directory):
    """Discorvers python modules in current directory."""
    function_names = []
    curr_dir = os.listdir(directory)
    for name in curr_dir:
        if name[-3:] == '.py':
            function_names.append(str(name))
    return function_names

def grab_docstrings(directory):
    """"Grabs the docstrings of all python modules specified."""
    import ast
    docstrings = {}
    for name in discover_functions(directory):
        path_name = os.path.join(directory, name)
        thing = ast.parse(''.join(open(path_name)))
        docstring = ast.get_docstring(thing)
        docstrings[name] = docstring
    return docstrings

def create_readme(doc_dic, directory):
    """Strips off license statement, formats readme, returns readme text."""
    scope = '''Scope:
    {}'''
    details = '''Details:{}'''
    scopelist = []
    detaillist = []
    scopestuff = ''
    detailstuff = ''
    # Now to create the contents of the README...
    scripts = doc_dic.keys()
    scripts.sort()
    for script in scripts:
        print "    Creating readme entry for: {}...".format(script)
        if doc_dic[script] == None:
            print "        But it has no docstring..."
            continue
        scopelist.append(script+'\n    ')
        docstring = doc_dic[script].replace('\n', '\n    ')
        doc_index = docstring.find("</license>") + 11
        # Stripping off the license in the docstring...
        docstring = docstring[doc_index:]
        detaillist.append('\n\n'+script+'\n')
        detaillist.append('    '+docstring)
    for item in scopelist:
        scopestuff += item
    for ano_item in detaillist:
        detailstuff += ano_item
    # Now to put the contents in their correct place...
    readme = (scope.format(scopestuff[:-4]) + '\n'
              + details.format(detailstuff) + '\n')
    # And write the README in its directory...
    write_readme(readme, directory)
    return None

def write_readme(r_text, directory):
    """Writes the readme!"""
    readme_path = os.path.join(directory, 'README.txt')
    with open(readme_path, 'w') as readme:
        readme.write(r_text)
    return None

def update_readme(directory):
    """Updates the readme everytime this script is called."""
    documentation_dict = grab_docstrings(directory)
    create_readme(documentation_dict, directory)
    return None

if __name__ == "__main__":
    CURR_DIR = os.path.abspath(os.path.dirname(__file__))
    update_readme(CURR_DIR)

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
    Updates README.txt file in current directory.

Inputs:
    Functions that share its directory. (discover_functions automatically)

Outputs:
    README.txt file, with Scope&&Details listed.
        Covers functions in current directory.

Currently:

To Do:
    Include story.txt in the README.

Done:
    Update readme file with current functions&&their docstrings.
'''

import os

def discover_functions():
    '''Discorvers python modules in current directory.'''
    function_names = []
    curr_dir = os.listdir('.')
    for name in curr_dir:
        if name[-3:] == '.py':
            function_names.append(str(name))
    return function_names

def grab_docstrings(fcn_names):
    """"Grabs the docstrings of all python modules specified."""
    import ast
    docstrings = {}
    for name in fcn_names:
        thing = ast.parse(''.join(open(name)))
        docstring = ast.get_docstring(thing)
        docstrings[name] = docstring
    return docstrings

def create_readme():
    """Strips off license statement, formats readme, returns readme text."""
    end_lisence = "</license>"
    scope = '''Scope:
    {}'''
    details = '''Details:{}'''
    scopelist = []
    detaillist = []
    scopestuff = ''
    detailstuff = ''

    doc_dic = grab_docstrings(discover_functions())
    scripts = doc_dic.keys()
    scripts.sort()
    for script in scripts:
        print "Creating readme entry for: {}...".format(script)
        scopelist.append(script+'\n    ')
        docstring = doc_dic[script].replace('\n', '\n    ')
        doc_index = docstring.find(end_lisence) + 11
        docstring = docstring[doc_index:]
        detaillist.append('\n\n'+script+'\n')
        detaillist.append('    '+docstring)
    for item in scopelist:
        scopestuff += item
    for ano_item in detaillist:
        detailstuff += ano_item
    readme = (scope.format(scopestuff[:-4]) + '\n'
              + details.format(detailstuff) + '\n')
    return readme

def write_readme(r_text):
    """Writes the readme!"""
    with open('./README.txt', 'w') as readme:
        readme.write(r_text)

def update_readme():
    """Updates the readme everytime `./automate_everything.py` is run."""
    note = '''For higher level to-do-list, see \'./story.txt\'.\n\n'''
    readme_text = create_readme()
    readme_text = note + readme_text
    write_readme(readme_text)

if __name__ == "__main__":
    update_readme()

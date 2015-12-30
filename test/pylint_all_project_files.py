# -*- coding: utf-8 -*-
"""
Module that runs pylint on all python scripts found in a directory tree...

Modifed version of a basic script found here:
    https://gist.github.com/PatrickSchiffmann/94b31329fbcef92bead8
"""

import os
import re
import subprocess

class Counter(object):
    """A counter to keep track of things globally."""
    def __init__(self):
        """Sets up counters for total score and module count."""
        self.total = 0.0
        self.count = 0

    def increase_count(self):
        """Increases the module count by one."""
        self.count += 1

    def increase_total(self, amount):
        """Increases the total score count by an amount."""
        self.total += amount

    def return_count(self):
        """Returns the module count."""
        return self.count

    def return_total(self):
        """Returns the total score count."""
        return self.total


def check(counter, module):
    """Apply pylint to the file specified if it is a `*.py` file."""
    if module[-3:] == ".py":
        print "CHECKING ", module
        pout = subprocess.Popen("pylint %s" % module,
                                stdout=subprocess.PIPE).stdout.read()
        for line in pout.split("\n"):
            if re.match("E....:.", line):
                print line
            if "Your code has been rated at" in line:
                print line
                score = re.findall(r"(-?\d+\.\d+)", line)[0]
                counter.increase_total(float(score))
                counter.increase_count()
    return None

def check_dir(counter, base_directory):
    """
    Applies pylint to all subdirectories under a base_directory.
    If it is undesireable for a directory to be checked,
        add a conditional to `first or second or third` so that if the root
        contains the undesired directory name the condition is true, and thus
        the files contained in the directory are not checked.
    """
    print "looking for *.py scripts in subdirectories of ", base_directory
    for root, dirs, files in os.walk(base_directory):
        del dirs
        # Define directories NOT to pylint...
        first = "populators" in root # So we don't check scripts in populators
        second = "old_scripts" in root
        third = "null" in root
        for name in files:
            filepath = os.path.join(root, name)
            if (first or second or third) == False:
                check(counter, filepath)
    return None

def print_results(counter):
    """Prints out the results of linting the code."""
    print "==" * 50
    print "%d modules found" % counter.return_count()
    print "AVERAGE SCORE = %.02f" % (counter.return_total() /
                                     counter.return_count())
    return None

def define_directories():
    """Contains the directories which contain project files."""
    dir_list = []
    basepath = os.path.dirname(__file__)
    # Now we resolve relatively defined path names.
    utilities = os.path.abspath(os.path.join(basepath, "..", "utility"))
    scripts = os.path.abspath(os.path.join(basepath, "..", "scripts"))
    tests = os.path.abspath(os.path.join(basepath, "..", "test"))
    # And add them to the list, to be processed.
    dir_list.append(utilities)
    dir_list.append(scripts)
    dir_list.append(tests)
    return dir_list

def run_it():
    """Pylints all files in directories defined."""
    counter = Counter()
    for dir_path in define_directories():
        check_dir(counter, dir_path)
    print_results(counter)
    return None

if __name__ == "__main__":
    run_it()

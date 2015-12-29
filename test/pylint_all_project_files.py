# -*- coding: utf-8 -*-
'''
Module that runs pylint on all python scripts found in a directory tree..
'''

import os
import re
import subprocess

class Counter(object):
    """A counter to keep track of things globally."""
    def __init__(self):
        self.total = 0.0
        self.count = 0

    def increase_count(self):
        self.count += 1

    def increase_total(self, amount):
        self.total += amount

    def return_count(self):
        return self.count

    def return_total(self):
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
                counter.increate_total(float(score))
                counter.increase_count()
    return None

def check_dir(counter, base_directory):
    print "looking for *.py scripts in subdirectories of ", base_directory
    for root, dirs, files in os.walk(base_directory):
        del dirs
        # Define directories NOT to pylint...
        first = "populators" in root
        second = "old_scripts" in root
        third = "null" in root
        for name in files:
            filepath = os.path.join(root, name)
            if (first or second or third) == False:
                check(counter, filepath)
    return None

def print_results(counter):
    print "==" * 50
    print "%d modules found" % counter.return_count()
    print "AVERAGE SCORE = %.02f" % (counter.return_total() /
                                     counter.return_count())
    return None

def define_directories():
    dir_list = []
    basepath = os.path.dirname(__file__)
    utilities = os.path.abspath(os.path.join(basepath, "..", "utility"))
    scripts = os.path.abspath(os.path.join(basepath, "..", "scripts"))
    tests = os.path.abspath(os.path.join(basepath, "..", "test"))
    dir_list.append(utilities)
    dir_list.append(scripts)
    dir_list.append(tests)
    return dir_list

def run_it():
    counter = Counter()
    for dir_path in define_directories():
        check_dir(counter, dir_path)
    print_results(counter)
    return None

if __name__ == "__main__":
    run_it()

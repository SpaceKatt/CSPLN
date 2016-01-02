Project Objective:
    From a set of images, create a set of full-stack web applications to
        host said images.

    Further utilities to aid in image analysis will be provided as separate
        components.

Instructions:
        To create a set of web applications to host a set of images:
    Clone or download a zip of the git repo.
    > cd scripts
    > python automate_everything.py
    # Runs with example images provided (low-resolution).
    # To run using other images, simply put them in './image/raw_tiff'
    #     then run automate_everything.py

Main readme in scripts folder.

Main to-do-list in 'scripts\story.txt'.

Based on the web2py framework: http://www.web2py.com/

On windows, this might not work with powershell due to how path-strings
    are named. This problem can be solved by using a command-shell that
    is well designed. (I find ConEmu is a better option)

TESTING:
    There exist two options for testing the project code:

    1 (using pytest):
    > cd test
    > py.test

    2:
    > cd test
    > python run_all_tests.py

PYLINT:
    To pylint all project files:
    > cd test
    > python pylint_all_project_files.py
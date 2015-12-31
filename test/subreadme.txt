Scope:
    aggregate_test_readme.py
    pylint_all_project_files.py
    run_all_tests.py
    update_test_subreadme.py

Details:

aggregate_test_readme.py
        
    Description:
        Updates the README's in child directories, then updates the one in this
            directory.
    
    Inputs:
        README files in subdirectories.
    
    Outputs:
        README file in current directory.
    
    Currently:
        Creating README text.
    
    To Do:
        Generate README in current directory,
            form lower direcotry README's.
        Generate subREADME in current direcotry,
            to document scripts in this file.
        Include subREADME in README.
        Change so this script accepts a dictionary which defines which
            directories to recurse into for README updates.
                -or-
            Create a higher lever funtion which calls a function like this in
                all directories of interest. update vs __aggregate__
    
    Done:
        Gather generated README's.
        Call lower README generating functions.

pylint_all_project_files.py
        
    Description:
        Module that runs pylint on all python scripts found in a directory tree...
    
        Heavily modifed version of a script found here:
            https://gist.github.com/PatrickSchiffmann/94b31329fbcef92bead8
            General method and all regular expressions were present in original
                scripts, referenced above.
    
    Inputs:
        All project files.
    
    Outputs:
        Pylint score of all files.
        Average score.
        Module count.
    
    Currently:
    
    To Do:
        Rewrite to accept a dictionary of directory paths.
            This will make it more portable, and easier to test...
        Rework procedure to skip checks on undesired direcotries.
    
    Done:
        Make process more visible through pretty printing.
        Fixing process documentation.
        Now pylint compatible.

run_all_tests.py
        
    Description:
        Runs all the tests, for all the modules.
    
    Inputs:
        Tests in `./test_utility`.
        Tests in `./test_scripts`.
    
    Outputs:
        Test results
    
    Currently:
        Adding more tests...
    
    To Do:
    
    Done:

update_test_subreadme.py
        
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

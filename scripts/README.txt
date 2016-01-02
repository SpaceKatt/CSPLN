Scope:
    automate_everything.py
    create_web_apps_linux.py
    create_web_apps_mac.py
    create_web_apps_win.py
    db_schemas.py
    image_path_chunk_grabber.py
    os_script_modifier.py
    populate_web_app.py
    process_images.py
    replace_db_references.py
    reset_system.py
    the_decider.py
    update_readme.py
    view_change.py

Details:

automate_everything.py
        
    Description:
        Does it all! (more descriptive description later)
    
    Inputs:
        All the scripts!
        Version number of current scaffolding_app
        Images in '../images/raw_tiff'
        OS Versions of web2py framework in '../scaffolidng'
    
    Outputs:
        All the things!
        All populated web_apps.
        The final project output, for Linux, Mac, and Windows.
        Updates README
    
    Currently:
        Rewriting scripts to avoid errors while calling from
            different directories.
    
    To Do:
        Rewrite Description, Inputs, and Outputs.
        Create version_search, which determines most up to date version.
    
    Done:

create_web_apps_linux.py
        
    Description:
        For creating CSPLN webapps for LINUX, from scaffolding.
    
    Inputs:
        Version number, of MKE_vxx_xx_xx scaffolding file.
            Where each x corresponds to a current version number.
            Input as "xx_xx_xx"
        Number of web applications
    
    Outputs:
        Web applications, number depends on Input.
        Puts web2py.py in each web_app (not included in windows version).
        Puts scaffolding (current app version) into each web2py frame.
        Renames scaffolding application to 'MKE_Static_Name'.
    
    Currently:
    
    To Do:
    
    Done:

create_web_apps_mac.py
        
    Description:
        For creating CSPLN webapps for MACINTOSH, from scaffolding.
    
    Inputs:
        Version number, of MKE_vxx_xx_xx scaffolding file.
            Where each x corresponds to a current version number.
            Input as "xx_xx_xx"
        Number of web applications
    
    Outputs:
        Web applications, number depends on Input.
        Puts web2py.py in each web_app (not included in windows version).
        Puts scaffolding (current app version) into each web2py frame.
        Renames scaffolding application to 'MKE_Static_Name'.
    
    Currently:
    
    To Do:
    
    Done:

create_web_apps_win.py
        
    Description:
        For creating CSPLN webapps for WINDOWS, from scaffolding.
    
    Inputs:
        Version number, of MKE_vxx_xx_xx scaffolding file.
            Where each x corresponds to a current version number.
            Input as "xx_xx_xx"
        Number of web applications
    
    Outputs:
        Web applications, number depends on Input.
        Puts web2py.py in each web_app (not included in windows version).
        Puts scaffolding (current app version) into each web2py frame.
        Renames scaffolding application to 'MKE_Static_Name'.
        Renames 'MKE_PT_.bat' shortcut to match application number.
    
    Currently:
    
    To do:
    
    Done:
        Delete examples and welcome apps in web2py framework.

db_schemas.py
        
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

image_path_chunk_grabber.py
        
    Description:
        Grabs chunks of image_paths to be processed by other scripts.
    
    Inputs:
        Amount of images_per_app
        Processed images.
    
    Outputs:
        Dictionary form {P_:[array]}, P_ referring to the specific web_app
            arrays consisting of image_file_paths.
    
    Currently:
    
    To Do:
    
    Done:

os_script_modifier.py
        
    Description:
        Replaces certian parts of python scripts that are suspected to cause
            problems between different operating systems.
        Be careful! This script doesn't create an archive, running it
            without proper care may cause a headache! Use proper string-
            escape notation.
    
    Inputs:
        All scripts in this directory (other than self).
    
    Outputs:
        All scripts, with specific words/phrases replaced.
    
    Currently:
    
    To Do:
    
    Done:

populate_web_app.py
        
    Description:
        Populates single web_app with images,
            use interactive python environment w\web2py.
        Will be used by another module 'x', module 'x' will decide
            how_many_apps to create and how_many_images_per_app, which will
            determine how 'x' calls populate_web_app.
        Saves generated cmds to '.\populators', which are run in an environment
            which is populated by the db objects of the corresponding web_app.
    
    Inputs:
        Specific images in '../image/processed_images'
        Specific web_app, and its database: 'image'.
    
    Outputs:
        Populated database in specified web_app.
    
    Currently:
    
    To Do:
    
    Done:
        Gather all relevant image information in a dictionary:
            {'png_md5':{png_md5}, 'name': {name}, 'png_size': {size},
             'tif_parent_md5': {tif_md5}, 'tif_parent_size': {tif_size},
             'file_path': {file_path}
             }
        Find way to upload images from command line,
            specifically from an interactive python shell.
            Will look like:
                db.image.insert(SOMETHING)
        Verify database gets populated correctly.
        Find way to pass generated commands to interpreter spawned from
            running web2py.py scripts to interact with web_app.
                Asked question on stackoverflow. (answered by Anthony)

process_images.py
        
    Description:
        Move tif files into '../images/raw_tiff', then run this script.
    
    Inputs:
        Tif files in '../images/raw_tiff'
    
    Outputs:
        Will produce folders in '../images/processed_images',
            which are labeled with 'M2JT' prefix, and given a unique number.
            Each folder will have both the parent tif and its child png, along
            with a txt file containing both their size and md5.
        Will produce text files in '../data', which are dictionaries.
            These should be made coherent by the name of the *.txt file.
            Dictionary format is {md5:file_size}
    
    Currently:
    
    To Do:
        Update documentation -- especially clarify obscure function params.
    
    Done:
        Make text files produced in '../data' contain dictionaries, not lists.
            This is important because we can present data as; {md5, size}.
            This change would prevent information loss and allow for better
                search/traceability.
        Store original file name in metadata!

replace_db_references.py
        
    Description:
        Replaces references to old databases in the scaffolding with references
            to the updated db_schema.
        Does this with dictionaries, mapping more complicated replacements
            before switching out simpler references.
    
    Inputs:
        Dictionaries to map replacements (contained within this script).
        Scaffolding version, more specifically the files within the scaffolding
            that need this change.
    
    Outputs:
        Files that have undergone operation will be written back into their
            respective places. And hopefully the web_apps will run!
    
    Currently:
    
    To Do:
    
    Done:
        Create replacement dictionaries.
        Read files, search for things in need of replacement,
            do replacement, write files.

reset_system.py
        
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

the_decider.py
        
    Description:
        Decide how many web_apps to make,
            and how many images should be in each.
    Inputs:
        Dictionaries in '../data',
            {md5:size}
    
    Outputs:
        how_many_apps
        images_per_app
    
    Currently:
        Add support for prime numbers of images.
            Prime numbers of images might create an infinite loop...
    
    To Do:
    
    Done:
        Take average image size.
        Decide how many average images could fit inside a 800Mb application.
        Decide how many applications will be nessecary to contain all
            images based on how many images_per_app.

update_readme.py
        
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

view_change.py
        
    Description:
        Changes the 'default/index.html' view to reflect the correct
            image numbers.
    
    Inputs:
        Dictionary form {P_:[array]}, P_ referring to the specific web_app
            arrays consisting of image_file_paths.
        Existing web_apps with views.
    
    Outputs:
        Changes the 'default/index.html' view to reflect the correct
            image numbers.
    
    Currently:
    
    To Do:
    
    Done:

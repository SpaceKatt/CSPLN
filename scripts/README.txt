For higher level to-do-list, see '.\story.txt'.

Scope:

    create_web_apps_win.py
    db_schemas.py
    populate_web_app.py
    process_images.py
    replace_db_references.py
    update_readme.py

Details:

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

populate_web_app.py

    THIS SCRIPT DOESN'T WORK! (yet)
    
    Description:
        Populates single web_app with images,
            use interactive python environment w/web2py.
        Will be used by another module 'x', module 'x' will decide
            how_many_apps to create and how_many_images_per_app, which will
            determine how 'x' calls populate_web_app.
    
    Inputs:
        Specific images in '..\image\processed_images'
        Specific web_app, and its database: 'image'.
    
    Outputs:
        Populated database in specified web_app.
    
    Currently:
        Find way to pass generated commands to interpreter spawned from
            running web2py.py scripts to interact with web_app.
                Asked question on stackoverflow.
    
    To Do:
        Verify database gets populated correctly.
    
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

process_images.py

    Description:
        Move tif files into '..\images\raw_tiff', then run this script.
    
    Inputs:
        Tif files in '..\images\raw_tiff'
    
    Outputs:
        Will produce folders in '..\images\processed_images',
            which are labeled with 'M2JT' prefix, and given a unique number.
            Each folder will have both the parent tif and its child png, along
            with a txt file containing both their size and md5.
        Will produce text files in '..\data', which are dictionaries.
            These should be made coherent by the name of the *.txt file.
            Dictionary format is {md5:file_size}
    
    Currently:
    
    To Do:
    
    Done:
        Make text files produced in '..\data' contain dictionaries, not lists.
            This is important because we can present data as; {md5, size}.
            This change would prevent information loss and allow for better
                search/traceability.

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

update_readme.py

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

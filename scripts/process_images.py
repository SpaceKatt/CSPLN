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

Done:
    Make text files produced in '../data' contain dictionaries, not lists.
        This is important because we can present data as; {md5, size}.
        This change would prevent information loss and allow for better
            search/traceability.
    Store original file name in metadata!
"""

import os, sys, shutil
from PIL import Image
import hashlib

def check_file_exist(path):
    """Check if the file at the given path exists."""
    if os.path.exists(path):
        pass
    else:
        sys.exit('File {} doesn\'t exist'.format(path))
    return None

def grab_file_paths(tif_dir):
    """Grabs the paths of images to be processed and puts them in a list."""
    image_path_list = []
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    tif_path = os.path.join(curr_dir, tif_dir)
    for root, dirs, files in os.walk(tif_path, topdown=False):
        del dirs
        for name in files:
            image_path_list.append((os.path.join(root, name)))
    return image_path_list

def grab_out_paths(image_path_list, adict):
    """
    Returns a list of filenames and the outpaths of processed images.


    """
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    out_dir = os.path.normpath((os.path.join(curr_dir, adict["out_path"])))
    image_name_form = adict["image_name_form"]
    out_paths = []
    file_names = []
    for num in range(len(image_path_list)):
        strin = image_name_form.format(str(num).zfill(4))
        file_names.append(strin)
        out_paths.append(out_dir.format(pat=strin))
    return out_paths, file_names

def grab_file_size(file_path):
    """Returns the size of a file."""
    data = os.path.getsize(file_path)
    return data

def md5check_grab(file_path):
    """Returns an md5 signature of a file."""
    check_file_exist(file_path)
    md5sum = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
    file_name = grab_filename_from_path(file_path)
    print '   {file}, md5: {m5}'.format(file=file_name, m5=md5sum)
    return md5sum

def grab_filename_from_path(in_path):
    """Input a path, return last chunck"""
    import ntpath
    head, tail = ntpath.split(in_path)
    return tail or ntpath.basename(head)

def transform_tiff_to_png(tiff_path, out_path, file_name):
    """For a single tiff file, create a png file, return its md5 and size."""
    new_path = os.path.join(out_path, file_name+'.png')
    image = Image.open(tiff_path)
    original_name = grab_filename_from_path(tiff_path)[:-4]
    image.save(new_path)
    size_file = grab_file_size(new_path)
    md5 = md5check_grab(new_path)
    return md5, size_file, original_name

def copy_tiff_to_final_loc(tiff_path, out_path, file_name):
    """Copy the original tiff to where its png counterpart is stored."""
    out_path = os.path.join(out_path, file_name+'.tif')
    shutil.copy(tiff_path, out_path)
    size_file = grab_file_size(out_path)
    md5 = md5check_grab(out_path)
    dec_s = "{tif} has been recorded as {fil}"
    print (dec_s.format(tif=grab_filename_from_path(tiff_path),
                        fil=file_name))
    return md5, size_file

def create_dirs(out_paths):
    """If a directory doesn't exist, create it."""
    for path in out_paths:
        if not os.path.exists(path):
            os.makedirs(path)
    return None

def write_image_meta(im_path, file_name, data):
    """Writes image metadata to a file in the same directory as the png."""
    meta_file = os.path.join(im_path, file_name+'.txt')
    with open(meta_file, 'w') as meta_stuff:
        meta_stuff.write(str(data))
    return None

def write_meta_data(data, adict):
    """
    Records sizes of all the pngs/tiffs in files that can later
        be read as dictionaries.
    ../data/png_sizes.txt
    ../data/tif_sizes.txt
    """
    curr_dir = os.path.abspath(os.path.dirname(__file__))
    meta_path = adict["meta_path"] + "/{}.txt"
    meta_path = os.path.normpath((os.path.join(curr_dir, meta_path)))
    keys = data.keys()
    for key in keys:
        with open(meta_path.format(key), 'w') as meta_file:
            sizes = str(data[key]) + '\n'
            meta_file.write(sizes)
    return None

def process_image(image_info):
    """
    For a single image, make a png, send the png to its ordered location,
        send a copy of the original tiff to the same location, record the
        necessary metadata, then write the image's metadata in the same
        location.
    """
    image = image_info["image_path"]
    out = image_info["out_path"]
    fil = image_info["file_name"]
    image_meta = {}
    md5png, png_sizei, original_name = transform_tiff_to_png(image, out, fil)
    md5tif, tif_sizei = copy_tiff_to_final_loc(image, out, fil)
    image_meta['md5'] = str(md5png)
    image_meta['size'] = int(png_sizei)
    image_meta['tif_parent_md5'] = str(md5tif)
    image_meta['size_tiff_parent'] = int(tif_sizei)
    image_meta['name'] = fil
    image_meta['original_name'] = original_name
    image_meta['file'] = os.path.join(out, fil)
    write_image_meta(out, fil, image_meta)
    return image_meta

def auto_rawr(adict):
    """
    Grabs the input paths (image file paths) and output paths (ordered
        file locations), creates directories at the outpaths, then
        processes each image and records their sizes in two dictionaries.
        These dictionaries are stored in files in ../data

    adict - dictionary that contains path information.
      keys:
        tif_path - relative path to raw_tif files.
    """
    png_file_size = {}
    tif_file_size = {}
    meta_d = {}
    image_paths = grab_file_paths(adict["tif_path"])
    out_p, file_n = grab_out_paths(image_paths, adict)
    create_dirs(out_p)
    assert len(image_paths) == len(out_p) == len(file_n)
    for num in range(len(image_paths)):
        image_info = {"image_path":image_paths[num],
                     "out_path":out_p[num],
                     "file_name":file_n[num]}
        dic = process_image(image_info)
        png_file_size[dic['md5']] = dic['size']
        tif_file_size[dic['tif_parent_md5']] = dic['size_tiff_parent']
    meta_d['png_sizes'] = png_file_size
    meta_d['tif_sizes'] = tif_file_size
    return meta_d

def in_summary(adict):
    """
    Processes everything and records necessary information.

    adict - dictionary that contains path information.
      keys:
        tif_path - relative path to raw_tif files.
    """
    stuff = auto_rawr(adict)
    write_meta_data(stuff, adict)
    return None

if __name__ == "__main__":
    ADICT = {"tif_path":"../images/raw_tiff",
             "out_path":"../images/processed_images/{pat}",
             "image_name_form":"M2JT{}",
             "meta_path":"../data"}
    in_summary(ADICT)

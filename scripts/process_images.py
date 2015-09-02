'''
Description:
    Move tif files into '..\\images\\raw_tiff', then run this script.

Inputs:
    Tif files in '..\\images\\raw_tiff'

Outputs:
    Will produce folders in '..\\images\\processed_images',
        which are labeled with 'M2JT' prefix, and given a unique number.
        Each folder will have both the parent tif and its child png, along
        with a txt file containing both their size and md5.
    Will produce text files in '..\\data', which are dictionaries.
        These should be made coherent by the name of the *.txt file.
        Dictionary format is {md5:file_size}

Currently:

To Do:

Done:
    Make text files produced in '..\\data' contain dictionaries, not lists.
        This is important because we can present data as; {md5, size}.
        This change would prevent information loss and allow for better
            search/traceability.
'''
'''
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
'''

import os, sys, shutil
from PIL import Image
import hashlib

def check_file_exist(path):
    if os.path.exists(path):
        print path, 'exists!'
    else:
        sys.exit('File {} doesn\'t exist'.format(path))
    return None

def grab_file_paths():
#    filename_list = []
#    dir_list = []
    image_path_list = []
    for root, dirs, files in os.walk("..\\images\\raw_tiff", topdown=False):
        del dirs
        for name in files:
            image_path_list.append((os.path.join(root, name)))
#            filename_list.append(name)
#        for name in dirs:
#            dir_list.append((os.path.join(root, name)))
    return image_path_list#, dir_list, filename_list

def grab_out_paths(image_path_list):
    out_dir = '..\\images\\processed_images\\{pat}'
    image_name_form = 'M2JT{}'
    out_paths = []
    file_names = []
    for num in range(len(image_path_list)):
        strin = image_name_form.format(str(num).zfill(4))
        file_names.append(strin)
        out_paths.append(out_dir.format(pat=strin))
    return out_paths, file_names

def grab_file_size(file_path):
    data = os.path.getsize(file_path)
    #print data
    return data

def md5check_grab(file_path):
    #print file_path
    check_file_exist(file_path)
    md5sum = hashlib.md5(open(file_path, 'rb').read()).hexdigest()
    print md5sum
    return md5sum

def transform_tiff_to_png(tiff_path, out_path, file_name):
    new_path = os.path.join(out_path, file_name+'.png')
    image = Image.open(tiff_path)
    image.save(new_path)
    size_file = grab_file_size(new_path)
    md5 = md5check_grab(new_path)
    return md5, size_file

def copy_tiff_to_final_loc(tiff_path, out_path, file_name):
    out_path = os.path.join(out_path, file_name+'.tif')
    shutil.copy(tiff_path, out_path)
    size_file = grab_file_size(out_path)
    md5 = md5check_grab(out_path)
    #deletetiff
    return md5, size_file

def create_dirs(out_paths):
    for path in out_paths:
        if not os.path.exists(path):
	        os.makedirs(path)
    return None

def write_image_meta(im_path, file_name, data):
    meta_file = os.path.join(im_path, file_name+'.txt')
    with open(meta_file, 'w') as meta_stuff:
#        keys = data.keys()
#        for key in keys:
#        strin = '{} = {}\n'.format(key, data[key])
        meta_stuff.write(str(data))
    return None

def write_meta_data(data):
    #print data
    meta_path = '..\\data\\{}.txt'
    keys = data.keys()
    for key in keys:
        with open(meta_path.format(key), 'w') as meta_file:
            sizes = str(data[key]) + '\n'
            meta_file.write(sizes)
    return None

def process_image(im, out, fi):
    image_meta = {}
    md5png, png_sizei = transform_tiff_to_png(im, out, fi)
    md5tif, tif_sizei = copy_tiff_to_final_loc(im, out, fi)
    image_meta['md5'] = str(md5png)
    image_meta['size'] = int(png_sizei)
    image_meta['tif_parent_md5'] = str(md5tif)
    image_meta['size_tiff_parent'] = int(tif_sizei)
    image_meta['name'] = fi
    image_meta['file'] = os.path.join(out, fi)
    write_image_meta(out, fi, image_meta)
    return image_meta

def auto_rawr():
    png_file_size = {}
    tif_file_size = {}
    meta_d = {}
    image_paths = grab_file_paths()
    out_p, file_n = grab_out_paths(image_paths)
    create_dirs(out_p)
    assert len(image_paths) == len(out_p) == len(file_n)
    for num in range(len(image_paths)):
        #print image_paths[num], out_p[num], file_n[num]
        dic = process_image(image_paths[num], out_p[num], file_n[num])
        png_file_size[dic['md5']] = dic['size']
        tif_file_size[dic['tif_parent_md5']] = dic['size_tiff_parent']
    meta_d['png_sizes'] = png_file_size
    meta_d['tif_sizes'] = tif_file_size
    return meta_d

def in_summary():
    stuff = auto_rawr()
    write_meta_data(stuff)
    return None

in_summary()

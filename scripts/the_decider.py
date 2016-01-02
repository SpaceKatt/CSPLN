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
'''
import ast

def resolve_relative_path(curr_file, rel_path):
    """
    This function returns the absolute path defined by a relative path,
        and always relative from the file which calls this function.
            curr_file - takes `__file__` as an argument.
            rel_path  - is a relatively defined path which uses either 
                            "/" or "\\" as separators, or both.
    The call of abspath(...) in the return statement might be redundant.
    """
    from os.path import join, normpath, abspath, dirname
    path_list = [dirname(curr_file)]
    rel_path = normpath(rel_path)
    if "/" in rel_path:
        split_path = rel_path.split("/")
    elif "\\" in rel_path:
        split_path = rel_path.split("\\")
    else:
        split_path = [".", rel_path]
    for splint in split_path:
        path_list.append(splint)
    path = reduce(lambda x, y: join(x, y), path_list)
    return abspath(normpath(path))

def grab_png_data(data_path):
    """Gathers png (processed images) size data."""
    path = resolve_relative_path(__file__, data_path + '/png_sizes.txt')
    with open(path, 'r') as dict_file:
        dictionary = ast.literal_eval(dict_file.read())
        return dictionary

def take_average(dictionary):
    """Takes the average size of all png files."""
    md5s = dictionary.keys()
    total, count = 0, 0
    for md5 in md5s:
        count += 1
        total += dictionary[md5]
    average = total / count
    return average

def how_many_images_fit(average, total_image_num):
    """Determines how many images can fit into a 800MB application."""
    eighthundomb = 800 * (10 ** 6)
    average_fit = eighthundomb // average
    images_per_app = average_fit
    for _ in range(images_per_app, images_per_app / 2, -1):
        images_per_app -= 1
        if total_image_num % images_per_app == 0:
            break
    if images_per_app > total_image_num:
        images_per_app = total_image_num
    return images_per_app

def apps_number(images_per_app, total_image_num):
    """
    From the amount of images that can fit into a single application,
        and the total amount of images, determines how many applications
        should be made.
    """
    how_many_apps = total_image_num // images_per_app
    if total_image_num % images_per_app != 0:
        how_many_apps += 1
    return how_many_apps

def the_decider(total_image_num, automation_dictionary):
    """
    Decides how many images each app should hold and how many apps to create.
    """
    print "\n\n    Deciding how many images to put in how many apps..."
    print "_"*79
    data_path = automation_dictionary["meta_path"]
    average = take_average(grab_png_data(data_path))
    print "\n    Average image size: {} B.".format(average)
    print "\n    Total number of Images: {}".format(total_image_num)
    images_per_app = how_many_images_fit(average, total_image_num)
    how_many_apps = apps_number(images_per_app, total_image_num)
    print '\n    Apps nessecary: ', how_many_apps
    print '\n    Images per app: ', images_per_app, '\n'
    print "_"*79
    return how_many_apps, images_per_app

if __name__ == "__main__":
    TOTAL_IMAGE_NUM = 659
    AUTO_DICT = {"meta_path":"../data"}
    HOW_MANY, IMAGES_PER = the_decider(TOTAL_IMAGE_NUM, AUTO_DICT)

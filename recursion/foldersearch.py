#!/usr/bin/env python3
import os
import fnmatch


IMAGE_GLOBS = {
    '*.png',
    '*.jpg',
}

def is_image(filename):
    '''
    Returns True if the given filename matches one of the IMAGE_GLOBS patterns.
    Just check the filename itself (don't inspect the file contents).
    '''
    for i in IMAGE_GLOBS:
        if fnmatch.fnmatch(filename, i):
            return True
    return False


def find_images(rootpath, subpath=''):
    '''
    Generator function that returns the images in the given directory
    tree (includes subdirectories). The returned image paths are relative to
    the given path.

    Use os.listdir() to get the files in the current directory (don't use os.walk
    or glob.glob).
    '''
    dirs = os.listdir(rootpath)
    for i in dirs:
        out = rootpath + '/' + i
        if is_image(i):
            yield out
        else:
            yield from find_images(out, i)
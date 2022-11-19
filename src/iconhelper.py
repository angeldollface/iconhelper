# ICON HELPER by Alexander Abraham, a.k.a. "Angel Dollface".
# Licensed under the MIT license.

import PIL
import os
import shutil
import colorama
import argparse
from os import makedirs
from os import chdir
from os import rmdir
from PIL import Image
from shutil import move
from argparse import ArgumentParser

def mainException():
    print('Invalid arguments supplied!')

def androidSizes():
    """
    Dictionary with the icon sizes for Android.
    """
    return {
      'hdpi':'72',
      'mdpi':'48',
      'xhdpi':'96',
      'xxhdpi':'144',
      'xxxhdpi':'192'
    }
def macOSSizes():
    """
    Dictionary with the icon sizes for Mac OSX.
    """
    return {
      '1':'16',
      '2':'32',
      '3':'64',
      '4':'128',
      '5':'256',
      '6':'512',
      '7':'1024',
    }
def windowsSizes():
    """
    Dictionary with the icon sizes for Windows.
    """
    return {
      '1':'256'
    }

def executeCompile(sourceImage, platform):
    """
    Iterates through the dictionary for the desired platform,
    resizes the input image into many copies, places the resulting
    image in a folder, and exits.
    """
    try:
        targetDir = 'dist' + platform
        makedirs(targetDir)
        chdir(targetDir)
        if platform == 'MacOS':
            src = '../' + sourceImage
            myImage = Image.open(src)
            prefix = 'app_icon_'
            for key in macOSSizes():
                size = int(macOSSizes()[key])
                new_image = myImage.resize((size, size))
                newString = prefix + macOSSizes()[key] + '.png'
                new_image.save(newString)
        elif platform == 'Android':
            src = '../' + sourceImage
            myImage = Image.open(src)
            imageName = 'ic_launcher.png'
            for key in androidSizes():
                dir = 'mipmap-' + key
                makedirs(dir)
                os.chdir(dir)
                size = int(androidSizes()[key])
                new_image = myImage.resize((size, size))
                new_image.save(imageName)
                chdir('..')
        elif platform == 'Windows':
            src = '../' + sourceImage
            myImage = Image.open(src)
            for key in windowsSizes():
                size = int(windowsSizes()[key])
                new_image = myImage.resize((size, size))
                newString = 'app_icon.ico'
                new_image.save(newString)
        else:
            pass
        chdir('..')
    except Exception as error:
        print(str(error))

def executeCleanUp():
    """
    Cleans up any residual
    directories.
    """
    dirList = [
      'dist',
      'distAndroid',
      'distMacOS',
      'distWindows',
    ]
    for item in dirList:
        try:
            rmdir(item)
        except Exception as error:
            print(str(error))

def version():
    """
    Prints out version info.
    """
    name = 'Icon Helper'
    version = '1.0.0'
    author = 'Alexander Abraham'
    license = 'MIT'
    print(name + 'v.' + version)
    print('by ' + author)
    print('Licensed under the ' + license + 'license!')

def cli():
    """
    The main CLI for the app.
    """
    parser = ArgumentParser()
    parser.add_argument('--version', help='displays version info', action='store_true')
    parser.add_argument('--source', help='the image for which to generate images')
    parser.add_argument('--platform', help='which platform to target')
    parser.add_argument('--clean', help='cleans up the current directory')
    args = parser.parse_args()
    if args.version:
        version()
    elif args.source and args.platform:
        executeCompile(args.source, args.platform)
    elif args.clean:
        executeCleanUp()
    elif args.source:
        try:
            executeCompile(args.source, 'Android')
            executeCompile(args.source, 'MacOS')
            executeCompile(args.source, 'Windows')
            makedirs('dist')
            move('distAndroid', 'dist')
            move('distMacOS', 'dist')
            move('distWindows', 'dist')
        except Exception as error:
            print(str(error))
    else:
        mainException()

def main():
    """
    Main point of entry 
    for the Python
    interpreter.
    """
    cli()


if __name__ == '__main__':
    main()

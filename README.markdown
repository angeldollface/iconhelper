# ICON HELPER :hammer: :snake:

![GitHub CI](https://github.com/angeldollface/iconhelper/actions/workflows/python.yml/badge.svg)

*A tool to help you generate all the different icon sets you need for a Flutter application. :hammer: :snake:*

## ABOUT :books:

I always hated generating different app icons of different sizes for different platforms manually using Photoshop. So, I decided to automate that process.
This tool, written in Python, my native language, lets you do just that. Currently supported platforms for generation of icon sets are:

- Mac OSX
- Android
- Windows

## USAGE :hammer:

### REQUIREMENTS

You should have the following tools installed and available from the command line:

- [Git](https://git-scm.org)
- [Python 3.5+](https://www.python.org/downloads/)
- Pip for Python 3.5+ (Usually comes with Python.)

### INSTALLING *ICON HELPER* ON YOUR SYSTEM

To use *Icon Helper* on your own system with your own projects, run the following command:

```bash
python -m pip install git+https://github.com/angeldollface/iconhelper
```

### USING *ICON HELPER* TO DOWNLOAD A FILE

To download a file, simply run this command (Here `mypng.png` represents a path to a PNG file.):

```bash
# For Mac OSX.
python -m python iconhelper --source mypng.png --platform MacOS

# For Android.
python -m python iconhelper --source mypng.png --platform Android

# For Windows.
python -m python iconhelper --source mypng.png --platform Windows
```

### CONSTRAINTS

- 1.) PNGs are the only supported input file type.
- 2.) Windows, Mac OSX, and Android are the only supported platforms.

## CHANGELOG :black_nib:

### Version 1.0.0

- Initial release.
- Upload to GitHub.

## NOTE :scroll:

- *Icon Helper :hammer: :snake:* by Alexander Abraham :black_heart: a.k.a. *"Angel Dollface" :dolls: :ribbon:*
- Licensed under the MIT license.


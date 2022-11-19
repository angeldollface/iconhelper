# ICON HELPER :hammer: :snake:

![GitHub CI](https://github.com/angeldollface/iconhelper/actions/workflows/python.yml/badge.svg)

*A tool to help you generate all the different icon sets you need for a Flutter application. :hammer: :snake:*

## ABOUT :books:

Generating icons for Flutter projects manually always seemed a bit tedious! To make this process a bit easier and faster, I wrote this tool, which automates the whole process.

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
python -m iconhelper --source mypng.png --platform MacOS

# For Android.
python -m iconhelper --source mypng.png --platform Android

# For Windows.
python -m iconhelper --source mypng.png --platform Windows
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


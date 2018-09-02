#!/usr/bin/env python

"""Unix implementation of userpaths.

Your application should not use this directly; "import userpaths" will
automatically select the correct implementation for the current platform.
"""

import os
import sys

# This is based in part on the XDG Base Directory Specification [1],
# and in part on observing how my own Unix system behaves in practice.
# If you know of other applicable standards, or closer common equivalents
# (i.e. not distribution-specific) to these paths' Windows counterparts,
# feel free to submit a patch.
#
# References:
# [1] https://specifications.freedesktop.org/basedir-spec/latest/


def _xdg_dir(env_name, default_value):
    """Return $env_name if specified, otherwise default_value."""

    if env_name:
        value = os.getenv(env_name)
    else:
        value = None

    if value:
        return value
    else:
        return os.path.expanduser(default_value)


def get_appdata():
    """Return the current user's roaming Application Data folder."""
    # FIXME: Is this actually the nearest equivalent in the XDG spec?
    return _xdg_dir("XDG_CONFIG_HOME", "~/.config")

def get_desktop():
    """Return the current user's Desktop folder."""
    return os.path.expanduser("~/Desktop")

def get_downloads():
    """Return the current user's Downloads folder."""
    return os.path.expanduser("~/Downloads")

def get_local_appdata():
    """Return the current user's local Application Data folder."""
    # FIXME: Is this actually the nearest equivalent in the XDG spec?
    return _xdg_dir("XDG_CONFIG_HOME", "~/.config")

def get_my_documents():
    """Return the current user's My Documents folder."""
    return os.path.expanduser("~")

def get_my_music():
    """Return the current user's My Music folder."""
    return os.path.expanduser("~")

def get_my_pictures():
    """Return the current user's My Pictures folder."""
    return os.path.expanduser("~")

def get_my_videos():
    """Return the current user's My Videos folder."""
    return os.path.expanduser("~")

def get_profile():
    """Return the current user's profile folder."""
    return os.path.expanduser("~")

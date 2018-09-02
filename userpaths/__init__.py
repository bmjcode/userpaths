#!/usr/bin/env python

"""Cross-platform access to a user's special folders.

The userpaths module provides cross-platform access to a user's special
folders (or directories) like My Documents, Desktop, and Application Data.

On Windows, it uses SHGetFolderPath() from shell32.dll. On other platforms,
it provides the closest standard or generally-used de facto equivalent.

The API is based on Ryan Ginstrom's winpaths [1], an existing module that
provides a Windows-specific solution to special folder access. However,
userpaths has a different overall focus (cross-platform access to a subset
of user folders), and is not intended as an exact drop-in replacement.

References:
[1] http://ginstrom.com/code/winpaths.html
"""

import os
import sys

if sys.platform.startswith("win"):
    from .windows import *
else:
    # Presume anything else is a Unix-like system
    from .unix import *

# Synonym for get_my_documents()
get_personal = get_my_documents

# These functions are defined in the individual platform modules
__all__ = [
    "get_appdata",
    "get_desktop",
    "get_downloads",
    "get_local_appdata",
    "get_my_documents",
    "get_my_music",         # not in winpaths
    "get_my_pictures",
    "get_my_videos",        # not in winpaths
    "get_personal",
    "get_profile",          # not in winpaths
]

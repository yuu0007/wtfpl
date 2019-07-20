#!/usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################

# Usage:
#
# $ py3 wtfpl.py
#     Name    : wtfpl.py
#     Version : 0
#     Status  : Development
#     Contact : <wtfpl@dtf.wtf>
#     Licence : WTFPLv3.1
#
#     Copyleft (ↄ) 2019, dtf <wtfpl@dtf.wtf>

################################################################

import datetime
import os


__version__    = "0"
__status__     = "Development"

__author__     = "dtf"
__credits__    = ["Banlu Kemiyatorn", "Sam Hocevar", "theiostream", __author__]
__maintainer__ = __author__
__email__      = "<wtfpl@dtf.wtf>"

__licence__    = "WTFPLv3.1"
__gcy__        = str(datetime.datetime.now().year)
__copyleft__   = "Copyleft (ↄ) {}, {} {}".format(__gcy__, __author__, __email__)
__license__    = __licence__
__copyright__  = __copyleft__

# This project is libre, and licenced under the terms of the
# DO WHAT THE FUCK YOU WANT TO PUBLIC LICENCE, version 3.1,
# as published by dtf on July 2019. See the COPYING file or
# https://ph.dtf.wtf/w/wtfpl/#version-3-1 for more details.


################################################################


if __name__ == "__main__":
    print("""
    Name    : {}
    Version : {}
    Status  : {}
    Contact : {}
    Licence : {}
    Credits : {}

    {}
    """.format(os.path.basename(__file__), __version__, __status__, __email__, __licence__, __credits__, __copyright__))


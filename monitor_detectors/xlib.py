"""
This file is part of the WallChange_Py Project.
Copyright © 2024-2024, Daniele Penazzo. All Rights Reserved.
The use of this code is governed by the BSD3 license attached.
See the LICENSE file for the full license.

Created on: 2024-12-24

Author: Penaz
"""
import Xlib.display
from .base import BaseDetector


class XlibDetector(BaseDetector):
    """
    Detector that finds monitors using Xlib
    """

    def get_monitors(self) -> list:
        """
        Get the monitors properties
        """
        # grab default X11 display (from $DISPLAY environment var)
        display = Xlib.display.Display()
        # get first and almost always the only X11 screen of this X11 display
        screen = display.screen()
        # Monitors are here
        monitors = screen.root.xrandr_get_monitors().monitors
        return [
            {
                "index": idx,
                "width": item["width_in_pixels"],
                "height": item["height_in_pixels"]
            }
            for idx, item in enumerate(monitors)
        ]

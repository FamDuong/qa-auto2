from pywinauto import Desktop
from utils_automation.common import FilesHandle
import logging

LOGGER = logging.getLogger(__name__)
file_handle = FilesHandle()


def enable_dark_mode_lbl_is_displayed(parent_window):
    try:
        enable_dark_mode_lbl = parent_window.child_window(title="Try enable to view the site in dark mode",
                                                          control_type="Text")
        if enable_dark_mode_lbl.is_visible() == 1:
            return True
    except Exception as e:
        LOGGER.info(e)
        return False


def click_dark_mode_enable_on_sites():
    import time
    time.sleep(5)
    coccoc_windows = Desktop(backend="uia").window(title_re='.* - Cốc Cốc.*')
    time.sleep(5)
    dark_mode_icon_omnibox = coccoc_windows.child_window(title="Enable/Disable Coc Coc Dark Mode on this site",
                                                         control_type="Button")
    time.sleep(5)
    dark_mode_icon_omnibox.click_input()
    dark_mode_popup = coccoc_windows.child_window(title="Dark Mode", control_type="Pane")

    if enable_dark_mode_lbl_is_displayed(dark_mode_popup):
        LOGGER.info("Click On dark mode")
        dark_mode_popup.Button3.click_input()


import pprint
import sys


def test():
    pprint.pprint(sys.path)

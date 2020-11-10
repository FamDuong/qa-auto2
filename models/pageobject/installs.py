from pywinauto import Desktop


def verify_installer_popup_appears():
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    # Find element on installer popup
    make_default_torrent_chk = coccoc_installer.child_window(title='Make Cốc Cốc your default torrent client')
    make_default_browser_chk = coccoc_installer.child_window(title='Make Cốc Cốc your default browser')
    run_browser_chk = coccoc_installer.child_window(title='Run browser on system start')
    install_btn = coccoc_installer.child_window(class_name="Button", control_type=50000)
    coccoc_img = coccoc_installer.child_window(class_name="Static", control_type=50006)
    # Verify element is visible
    assert make_default_torrent_chk.is_visible() == 1
    assert make_default_browser_chk.is_visible() == 1
    assert run_browser_chk.is_visible() == 1
    assert install_btn.is_visible()
    assert coccoc_img.is_visible()
    # Verify state of checkbox is checked/unchecked
    assert make_default_browser_chk.get_toggle_state() == 1
    assert make_default_torrent_chk.get_toggle_state() == 1
    assert run_browser_chk.get_toggle_state() == 0


def verify_installation_complete_popup_appears():
    coccoc_installer = Desktop(backend='uia').Cốc_Cốc_Installer
    # Find element on installer popup
    install_complete_lbl = coccoc_installer.child_window(title="Installation complete. Let's enjoy internet with "
                                                                   "Cốc Cốc.")
    close_btn = coccoc_installer.child_window(title="Close", class_name="Button", control_type=50000)
    # Verify element is visible
    assert install_complete_lbl.is_visible() == 1
    assert close_btn.is_visible() == 1
    from utils_automation.common_browser import cleanup
    cleanup()

import time

import pytest
from selenium import webdriver

from testscripts.smoketest.common import check_if_coccoc_is_installed, uninstall_coccoc_silently, \
    install_coccoc_silently, kill_browser_process, install_coccoc_not_set_as_default, \
    install_coccoc_set_system_start_up_on, install_coccoc_set_as_default, uninstall_then_install_coccoc_with_default, \
    chrome_options_preset, interact_dev_hosts
from utils_automation.common import WindowsHandler, modify_file_as_text

windows_handler = WindowsHandler()
current_user = windows_handler.get_current_login_user()


@pytest.fixture(scope='function')
def coccoc_install_instance_on_default_browser():
    uninstall_then_install_coccoc_with_default()
    driver = webdriver.Chrome(options=chrome_options_preset())
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def install_default_coccoc():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_silently()
    while check_if_coccoc_is_installed() is False:
        time.sleep(1)


@pytest.fixture(scope='function')
def install_default_coccoc_unsilently():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_set_as_default()
    while check_if_coccoc_is_installed() is False:
        time.sleep(1)


@pytest.fixture(scope='function')
def coccoc_install_instance_set_not_default_browser():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_not_set_as_default()
    driver = webdriver.Chrome(options=chrome_options_preset())
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def install_set_system_option_on():
    if check_if_coccoc_is_installed():
        uninstall_coccoc_silently()
    install_coccoc_set_system_start_up_on()


@pytest.fixture(scope='function')
def activate_then_deactive_hosts_for_coccoc_dev():
    interact_dev_hosts()
    yield
    interact_dev_hosts(action='deactivate')


@pytest.fixture(scope='function')
def install_coccoc_after_finish_test():
    yield
    install_coccoc_not_set_as_default()
    time.sleep(6)


def pytest_addoption(parser):
    parser.addoption(
        "--coccocdev", action="store_true", default=False, help="run tests with coccocdev mark"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "coccocdev: mark test as coccocdev to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--coccocdev"):
        # --coccocdev given in cli: do not skip coccocdev tests
        return
    skip_slow = pytest.mark.skip(reason="need --coccocdev option to run")
    for item in items:
        if "coccocdev" in item.keywords:
            item.add_marker(skip_slow)

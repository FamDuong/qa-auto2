import pytest

from testscripts.common_setup import clear_data_download, delete_all_mp4_file_download


@pytest.fixture()
def clear_download_page_and_download_folder(browser, get_current_download_folder):
    yield
    clear_data_download(browser)
    delete_all_mp4_file_download(get_current_download_folder, '.mp4')
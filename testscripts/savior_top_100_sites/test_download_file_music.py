from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail

from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.common_setup import implement_download_file, delete_all_mp4_file_download, \
    pause_or_play_video_by_javascript, download_file_via_main_download_button, get_resolution_info, \
    assert_file_download_value
from utils_automation.const import OtherSiteUrls

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
top_site_titles_action = TopSitesSaviorTitleAction()


class TestNhacVN:

    @pytestrail.case('C98782')
    def test_download_nhac_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.NHAC_VN_VIDEO_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        any_site_page_object.mouse_over_first_video_element(browser_top_sites)
        media_info = download_file_via_main_download_button(browser_top_sites, time_sleep=15)
        resolution_info = get_resolution_info(media_info)
        try:
            assert_file_download_value(get_current_download_folder_top_sites, resolution_info,
                                       start_with=video_title)
        finally:
            delete_all_mp4_file_download(get_current_download_folder_top_sites, '.mp4', startwith=video_title)
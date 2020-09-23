from pytest_testrail.plugin import pytestrail

from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
from testscripts.savior_top_100_sites.common import download_and_verify_video
from utils_automation.const import OtherSiteUrls

top_site_titles_action = TopSitesSaviorTitleAction()


class TestNhacVN:

    @pytestrail.case('C98782')
    def test_download_nhac_vn(self, browser_top_sites, get_current_download_folder_top_sites):
        browser_top_sites.get(OtherSiteUrls.NHAC_VN_VIDEO_URL)
        video_title = top_site_titles_action.get_website_title_by_javascript(browser_top_sites)
        download_and_verify_video(browser_top_sites, get_current_download_folder_top_sites, video_title)


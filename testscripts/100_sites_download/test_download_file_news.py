from datetime import datetime

from models.pageelements.sites import AnySiteElements
from models.pageobject.savior import SaviorPageObject
from models.pageobject.sites import AnySitePageObject
from pytest_testrail.plugin import pytestrail
from testscripts.sanitytest.savior.common_setup import delete_all_mp4_file_download, \
    clear_data_download, implement_download_file, \
    clear_data_download_in_browser_and_download_folder, verify_download_quality_high_frame, \
    verify_video_step_then_clear_data, choose_video_quality_medium_option, revert_high_quality_default_option
from utils_automation.const import OtherSiteUrls
from utils_automation.setup import WaitAfterEach

any_site_page_object = AnySitePageObject()
savior_page_object = SaviorPageObject()
any_site_element = AnySiteElements()


class Test24H:

    @staticmethod
    def mouse_over_video_element_24h(browser):
        browser.get(OtherSiteUrls.TWENTY_FOUR_H_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_24h(browser)

    def prepare_check_download(self, browser, download_folder):
        self.mouse_over_video_element_24h(browser)
        # download_folder_path = self.setting_page_obeject.get_download_folder(browser)
        delete_all_mp4_file_download(download_folder, '.mp4')
        WaitAfterEach.sleep_timer_after_each_step()

    @pytestrail.case('C96720')
    def test_download_file_24h(self, browser, get_current_download_folder):
        self.prepare_check_download(browser, get_current_download_folder)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.mouse_over_video_element_24h),
                                          clear_data_download(browser))


class TestKienThucDotNet:

    @staticmethod
    def prepare_appear_savior_option(browser):
        browser.get(OtherSiteUrls.KIENTHUC_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        any_site_page_object.click_video_item_kienthuc(browser)
        any_site_page_object.mouse_over_video_item_kienthuc(browser)

    @pytestrail.case('C96755')
    def test_download_file_kiethuc_dotnet(self, browser, get_current_download_folder):
        self.prepare_appear_savior_option(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestVietnamNet:

    @staticmethod
    def prepare_savior_option_displayed(browser):
        browser.get(OtherSiteUrls.VIETNAMNET_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_vietnamnet(browser)

    @pytestrail.case('C96759')
    def test_download_file_vietnamnet(self, browser, get_current_download_folder):
        self.prepare_savior_option_displayed(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_displayed),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestEvaVn:

    @staticmethod
    def prepare_savior_displayed(browser):
        browser.get(OtherSiteUrls.EVA_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_eva_vn(browser)

    @pytestrail.case('C96761')
    def test_download_file_eva_vn(self, browser, get_current_download_folder):
        self.prepare_savior_displayed(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_displayed),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestSoha:

    @staticmethod
    def prepare_savior_displayed(browser):
        browser.get(OtherSiteUrls.SOHA_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_soha(browser)

    @pytestrail.case('C98722')
    def test_download_file_soha(self, browser, get_current_download_folder):
        self.prepare_savior_displayed(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_displayed),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class Test2SaoVn:

    @staticmethod
    def prepare_savior_displayed(browser):
        browser.get(OtherSiteUrls.SAO_2_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_sao_2_vn(browser)

    @pytestrail.case('C98725')
    def test_download_file_test2sao(self, browser, get_current_download_folder):
        self.prepare_savior_displayed(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_displayed),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestPhuNuVaGiaDinh:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.PHUNU_GIADINH_VIDEO_URL)
        any_site_page_object.click_video_item_phunu_giadinh(browser)
        any_site_page_object.mouse_over_video_item_phunu_giadinh(browser)

    @pytestrail.case('C98734')
    def test_download_file_phunu_giadinh(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestTienPhong:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.TIEN_PHONG_VIDEO_URL)
        any_site_page_object.click_video_item_tien_phong(browser)
        WaitAfterEach.sleep_timer_after_each_step_longest_load()
        browser.switch_to.default_content()
        any_site_page_object.mouse_over_video_item_tien_phong(browser)

    @pytestrail.case('C98743')
    def test_download_file_tienphong(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestBongDaDotCom:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.BONG_DA_DOT_COM_VIDEO_URL)
        WaitAfterEach.sleep_timer_after_each_step()
        any_site_page_object.click_video_item_bong_da_dot_com(browser)
        any_site_page_object.mouse_over_video_item_bong_da_dot_com(browser)

    @pytestrail.case('C98746')
    def test_download_file_bongda_dotcom(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_appear),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestGiaDinhDotNet:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.GIA_DINH_DOT_NET_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_gia_dinh_dot_net(browser)

    @pytestrail.case('C98748')
    def test_download_file_gia_dinh_dotnet(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_appear),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestAFamily:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.A_FAMILY_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_a_family(browser)

    @pytestrail.case('C98749')
    def test_download_file_video_a_family(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_appear),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestGamek:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.GAMEK_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_gamek_vn(browser)

    @pytestrail.case('C98750')
    def test_download_file_video_gamek(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_appear),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestAnNinhThuDo:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.AN_NINH_THU_DO_VIDEO_URL)
        any_site_page_object.click_video_item_an_ninh_thu_do(browser)
        any_site_page_object.mouse_over_video_item_an_ninh_thu_do(browser)

    @pytestrail.case('C98752')
    def test_download_file_video_an_ninh_thu_do(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestTuoiTre:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.TUOI_TRE_VIDEO_URL)
        any_site_page_object.mouse_over_video_item_tuoi_tre(browser)

    @pytestrail.case('C98754')
    def test_download_file_video_tuoi_tre(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_appear),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestNgoiSaoVN:

    @pytestrail.case('C98763')
    def test_download_file_ngoi_sao_vn(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.NGOI_SAO_VN_URL)
        any_site_page_object.mouse_over_video_item_ngoi_sao_vn(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestVTCVN:

    @pytestrail.case('C98764')
    def test_download_file_vtc_vn(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.VTC_VN_VIDEO_URL)
        any_site_page_object.click_video_element_vtc_v(browser)
        any_site_page_object.mouse_over_video_element_vtc_vn(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestKenh14VN:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.KENH14_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_kenh14_vn(browser)

    @pytestrail.case('C98765')
    def test_download_file_kenh14_vn(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_appear),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestCafeVN:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.CAFE_VN_VIDEO_URL)
        any_site_page_object.mouse_over_video_element_cafe_vn(browser)

    @pytestrail.case('C98766')
    def test_download_file_cafe_vn(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_appear),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestTinTucOnlineVN:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.TIN_TUC_ONLINE_VIDEO_URL)
        any_site_page_object.mouse_over_video_detail_tin_tuc_online_vn(browser)

    @pytestrail.case('C98768')
    def test_download_file_tin_tuc_online(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(verify_download_quality_high_frame(browser, get_current_download_folder,
                                                                             self.prepare_savior_option_appear),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestGiaoDucThoiDai:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.GIAO_DUC_THOI_DAI_VIDEO_URL)
        any_site_page_object.click_video_giao_duc_thoi_dai(browser)
        any_site_page_object.mouse_over_video_giao_duc_thoi_dai(browser)

    @pytestrail.case('C98770')
    def test_download_file_tin_tuc_online(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestVNExpressNet:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.VN_EXPRESS_VIDEO_URL)
        any_site_page_object.mouse_over_video_vn_express(browser)

    @pytestrail.case('C98772')
    def test_download_file_tin_tuc_online(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestThanhNienVN:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.THANH_NIEN_VIDEO_URL)
        any_site_page_object.mouse_over_video_thanh_nien_vn(browser)

    @pytestrail.case('C98773')
    def test_download_file_tin_tuc_online(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestDanTriVN:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.DAN_TRI_VIDEO_URL)
        any_site_page_object.mouse_over_video_dan_tri_vn(browser)

    @pytestrail.case('C98775')
    def test_download_file_tin_tuc_online(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestNguoiLaoDongTV:

    @staticmethod
    def prepare_savior_option_appear(browser):
        browser.get(OtherSiteUrls.NGUOI_LAO_DONG_TV_URL)
        any_site_page_object.mouse_over_video_nguoi_lao_dong_tv(browser)

    @pytestrail.case('C98777')
    def test_download_file_nguoi_lao_dong_tv(self, browser, get_current_download_folder):
        self.prepare_savior_option_appear(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestTinMoi:

    @pytestrail.case('C98784')
    def test_download_file_tin_moi(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.TIN_MOI_VIDEO_URL)
        any_site_page_object.mouse_over_video_tin_moi(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestInfoNet:

    @pytestrail.case('C98787')
    def test_download_file_info_net(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.INFO_NET_VIDEO_URL)
        any_site_page_object.mouse_over_video_info_net(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestBongda24h:

    @pytestrail.case('C98788')
    def test_download_file_bong_da_24h(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.BONG_DA_24H_VIDEO_URL)
        any_site_page_object.mouse_over_video_bong_da_24h(browser)
        verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder),
                                          clear_data_download_in_browser_and_download_folder(browser,
                                                                                             get_current_download_folder))


class TestKeoNhaCai:

    @pytestrail.case('C98792')
    def test_download_file_keo_nha_cai(self, browser, get_current_download_folder):
        choose_video_quality_medium_option(browser)
        try:
            browser.get(OtherSiteUrls.KEO_NHA_CAI_VIDEO_URL)
            any_site_page_object.click_video_item_keo_nha_cai(browser)
            any_site_page_object.mouse_over_video_item_keo_nha_cai(browser)
            verify_video_step_then_clear_data(implement_download_file(browser, get_current_download_folder, file_type='very slow'),
                                              clear_data_download_in_browser_and_download_folder(browser,
                                                                                                 get_current_download_folder))
        finally:
            revert_high_quality_default_option(browser)


class TestVoV:

    @pytestrail.case('C98798')
    def test_download_file_vov(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.VOV_VIDEO_URL)
        any_site_page_object.click_video_item_vov_vn(browser)
        any_site_page_object.mouse_over_video_item_vov_vn_maximize_minimize(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder, file_type='slow'),
            clear_data_download_in_browser_and_download_folder(browser,
                                                               get_current_download_folder))


class TestDoiSongPhapLuat:

    @pytestrail.case('C98776')
    def test_download_doi_song_phap_luat(self, browser, get_current_download_folder):
        browser.get(OtherSiteUrls.DOI_SONG_PHAP_LUAT_VIDEO_URL)
        any_site_page_object.click_video_item_doi_song_phap_luat(browser)
        verify_video_step_then_clear_data(
            implement_download_file(browser, get_current_download_folder),
            clear_data_download_in_browser_and_download_folder(browser,
                                                               get_current_download_folder))




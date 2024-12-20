# import time
#
# import pytest
#
# from models.pagelocators.sites import AnySite
# from models.pageobject.savior import SaviorPageObject
# from models.pageobject.sites import AnySitePageObject
# from pytest_testrail.plugin import pytestrail
#
# from models.pageobject.top_savior_sites.top_savior_sites_title import TopSitesSaviorTitleAction
# from testscripts.common_setup import delete_all_mp4_file_download, \
#     implement_download_file, verify_download_quality_high_frame, \
#     choose_video_quality_medium_option, pause_or_play_video_by_javascript
# from testscripts.savior_top_100_sites.common import download_and_verify_video
# from utils_automation.const import OtherSiteUrls
# from utils_automation.setup import WaitAfterEach
#
# any_site_page_object = AnySitePageObject()
# savior_page_object = SaviorPageObject()
# top_site_titles_action = TopSitesSaviorTitleAction()
#
# class TestEvaVn:
#
#      @staticmethod
#      def prepare_savior_displayed(browser):
#          browser.get(OtherSiteUrls.EVA_VN_VIDEO_URL)
#          any_site_page_object.mouse_over_video_item_eva_vn(browser)
#
#      @pytestrail.case('C96761')
#      def test_download_file_eva_vn(self, browser, get_current_download_folder, clear_download_page):
#          self.prepare_savior_displayed(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder, self.prepare_savior_displayed)
#
#  class TestSoha:
#
#      @staticmethod
#      def prepare_savior_displayed(browser):
#          browser.get(OtherSiteUrls.SOHA_VIDEO_URL)
#          any_site_page_object.mouse_over_video_item_soha(browser)
#
#      @pytestrail.case('C98722')
#      def test_download_file_soha(self, browser, get_current_download_folder, clear_download_page):
#          self.prepare_savior_displayed(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder,
#                                             self.prepare_savior_displayed)
#
#
#  class Test2SaoVn:
#
#      @staticmethod
#      def prepare_savior_displayed(browser):
#          browser.get(OtherSiteUrls.SAO_2_VN_VIDEO_URL)
#          any_site_page_object.click_video_item_sao_2_vn(browser)
#          any_site_page_object.mouse_over_video_item_sao_2_vn(browser)
#
#      @pytestrail.case('C98725')
#      def test_download_file_test2sao(self, browser, get_current_download_folder,
#                                      clear_download_page):
#          self.prepare_savior_displayed(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder,
#                                             self.prepare_savior_displayed),
#
#  class TestPhuNuVaGiaDinh:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.PHUNU_GIADINH_VIDEO_URL)
#          any_site_page_object.click_video_item_phunu_giadinh(browser)
#          any_site_page_object.mouse_over_video_item_phunu_giadinh(browser)
#
#      @pytestrail.case('C98734')
#      def test_download_file_phunu_giadinh(self, browser, get_current_download_folder,
#                                           clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          implement_download_file(browser, get_current_download_folder)
#
#  class TestTienPhong:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.TIEN_PHONG_VIDEO_URL)
#          any_site_page_object.click_video_item_tien_phong(browser)
#          any_site_page_object.mouse_over_video_item_tien_phong(browser)
#
#      @pytestrail.case('C98743')
#      def test_download_file_tienphong(self, browser, get_current_download_folder,
#                                       clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          implement_download_file(browser, get_current_download_folder)
#
#  class TestBongDaDotCom:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.BONG_DA_DOT_COM_VIDEO_URL)
#          any_site_page_object.click_video_item_bong_da_dot_com(browser)
#          any_site_page_object.mouse_over_video_item_bong_da_dot_com(browser)
#
#      @pytestrail.case('C98746')
#      def test_download_file_bongda_dotcom(self, browser, get_current_download_folder,
#                                           clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder,
#                                             self.prepare_savior_option_appear)
#
#  class TestGiaDinhDotNet:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.GIA_DINH_DOT_NET_VIDEO_URL)
#          any_site_page_object.mouse_over_video_item_gia_dinh_dot_net(browser)
#
#      @pytestrail.case('C98748')
#      def test_download_file_gia_dinh_dotnet(self, browser, get_current_download_folder
#                                             , clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder,
#                                             self.prepare_savior_option_appear)
#
#  class TestAFamily:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.A_FAMILY_VIDEO_URL)
#          any_site_page_object.mouse_over_video_item_a_family(browser)
#
#      @pytestrail.case('C98749')
#      def test_download_file_video_a_family(self, browser, get_current_download_folder
#                                            , clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder,
#                                             self.prepare_savior_option_appear),
#
#  class TestGamek:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.GAMEK_VN_VIDEO_URL)
#          any_site_page_object.mouse_over_video_item_gamek_vn(browser)
#
#      @pytestrail.case('C98750')
#      def test_download_file_video_gamek(self, browser, get_current_download_folder
#                                         , clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder,
#                                             self.prepare_savior_option_appear),
#
#  class TestAnNinhThuDo:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.AN_NINH_THU_DO_VIDEO_URL)
#          any_site_page_object.click_video_item_an_ninh_thu_do(browser)
#          any_site_page_object.mouse_over_video_item_an_ninh_thu_do(browser)
#
#      @pytestrail.case('C98752')
#      def test_download_file_video_an_ninh_thu_do(self, browser, get_current_download_folder
#                                                  , clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          implement_download_file(browser, get_current_download_folder)
#
#
#  class TestNgoiSaoVN:
#
#      @pytestrail.case('C98763')
#      def test_download_file_ngoi_sao_vn(self, browser, get_current_download_folder
#                                         , clear_download_page):
#          browser.get(OtherSiteUrls.NGOI_SAO_VN_URL)
#          any_site_page_object.mouse_over_video_item_ngoi_sao_vn(browser)
#          implement_download_file(browser, get_current_download_folder),
#
#
#  class TestCafeVN:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.CAFE_VN_VIDEO_URL)
#          any_site_page_object.mouse_over_video_element_cafe_vn(browser)
#
#      @pytestrail.case('C98766')
#      def test_download_file_cafe_vn(self, browser, get_current_download_folder
#                                     , clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder,
#                                             self.prepare_savior_option_appear),
#
#  class TestTinTucOnlineVN:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.TIN_TUC_ONLINE_VIDEO_URL)
#          any_site_page_object.mouse_over_video_detail_tin_tuc_online_vn(browser)
#
#      @pytestrail.case('C98768')
#      def test_download_file_tin_tuc_online(self, browser, get_current_download_folder
#                                            , clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          verify_download_quality_high_frame(browser, get_current_download_folder,
#                                             self.prepare_savior_option_appear),
#
#
#  class TestGiaoDucThoiDai:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.GIAO_DUC_THOI_DAI_VIDEO_URL)
#          any_site_page_object.click_video_giao_duc_thoi_dai(browser)
#          any_site_page_object.mouse_over_video_giao_duc_thoi_dai(browser)
#
#      @pytestrail.case('C98770')
#      def test_download_file_tin_tuc_online(self, browser, get_current_download_folder
#                                            , clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          implement_download_file(browser, get_current_download_folder),
#
#
#
#  class TestNguoiLaoDongTV:
#
#      @staticmethod
#      def prepare_savior_option_appear(browser):
#          browser.get(OtherSiteUrls.NGUOI_LAO_DONG_TV_URL)
#          any_site_page_object.click_video_nguoi_lao_dong_tv(browser)
#          any_site_page_object.mouse_over_video_nguoi_lao_dong_tv(browser)
#
#      @pytestrail.case('C98777')
#      def test_download_file_nguoi_lao_dong_tv(self, browser, get_current_download_folder
#                                               , clear_download_page):
#          self.prepare_savior_option_appear(browser)
#          implement_download_file(browser, get_current_download_folder),
#
#
#
#
#  class TestTinMoi:
#
#      @pytestrail.case('C98784')
#      def test_download_file_tin_moi(self, browser, get_current_download_folder
#                                     , clear_download_page):
#          browser.get(OtherSiteUrls.TIN_MOI_VIDEO_URL)
#          any_site_page_object.mouse_over_video_tin_moi(browser)
#          implement_download_file(browser, get_current_download_folder),
#
#  class TestInfoNet:
#
#      @pytestrail.case('C98787')
#      def test_download_file_info_net(self, browser, get_current_download_folder
#                                      , clear_download_page):
#          browser.get(OtherSiteUrls.INFO_NET_VIDEO_URL)
#          any_site_page_object.click_video_info_net(browser)
#          any_site_page_object.mouse_over_video_info_net(browser)
#          implement_download_file(browser, get_current_download_folder, file_size=1.00),
#
#
#
#  class TestBongda24h:
#
#      @pytestrail.case('C98788')
#      def test_download_file_bong_da_24h(self, browser, get_current_download_folder
#                                         , clear_download_page):
#          browser.get(OtherSiteUrls.BONG_DA_24H_VIDEO_URL)
#          any_site_page_object.click_video_bong_da_24h(browser)
#          any_site_page_object.mouse_over_video_bong_da_24h(browser)
#          implement_download_file(browser, get_current_download_folder),
#
#
#
#  class TestKeoNhaCai:
#
#      @pytestrail.case('C98792')
#      @pytestrail.defect('BR-1200')
#      @pytest.mark.skip('Cannot convert to mp4 due to BR-1200')
#      def test_download_file_keo_nha_cai(self, browser, get_current_download_folder
#                                         , clear_download_page, revert_high_quality_default_option):
#          choose_video_quality_medium_option(browser)
#          browser.get(OtherSiteUrls.KEO_NHA_CAI_VIDEO_URL)
#          any_site_page_object.click_video_item_keo_nha_cai(browser)
#          any_site_page_object.mouse_over_video_item_keo_nha_cai(browser)
#          implement_download_file(browser, get_current_download_folder, ),
#
#
#
#  class TestVoV:
#
#      @pytestrail.case('C98798')
#      def test_download_file_vov(self, browser_top_sites, get_current_download_folder_top_sites, enable_ublock_plus_extension):
#          browser_top_sites.get(OtherSiteUrls.VOV_VIDEO_URL)
#          any_site_page_object.switch_to_frame_vov_vn(browser_top_sites)
#          any_site_page_object.play_vov_vn_video(browser_top_sites)
#          browser_top_sites.switch_to.default_content()
#          any_site_page_object.mouse_over_video_item_vov_vn(browser_top_sites)
#          implement_download_file(browser_top_sites, get_current_download_folder_top_sites, time_sleep=8, ),
#
#
# class TestDoiSongPhapLuat:
#
#     @pytestrail.case('C98776')
#     def test_download_doi_song_phap_luat(self, browser, get_current_download_folder
#                                          , clear_download_page):
#         browser.get(OtherSiteUrls.DOI_SONG_PHAP_LUAT_VIDEO_URL)
#         any_site_page_object.click_video_item_doi_song_phap_luat(browser)
#         any_site_page_object.mouse_over_video_doi_song_phap_luat(browser)
#         implement_download_file(browser, get_current_download_folder),
#
#
# class TestSaoStar:
#
#     @pytestrail.case('C98785')
#     @pytestrail.defect('PF-497')
#     def test_download_sao_star(self, browser, get_current_download_folder
#                                , clear_download_page):
#         browser.get(OtherSiteUrls.SAO_STAR_VIDEO_URL)
#         any_site_page_object.mouse_over_video_sao_star_vn(browser)
#         implement_download_file(browser, get_current_download_folder),
#
#
#
#
#
# class TestBestieVN:
#
#     @pytestrail.case('C98791')
#     def test_download_bestie_vn_video(self, browser, get_current_download_folder
#                                       , clear_download_page
#                                       , choose_low_quality_option, revert_high_quality_default_option):
#         browser.get(OtherSiteUrls.BESTIE_VN_VIDEO_URL)
#         any_site_page_object.switch_to_first_iframe_bestie_vn(browser)
#         any_site_page_object.switch_to_second_iframe_bestie_vn(browser)
#         any_site_page_object.mouse_over_video_bestie_vn(browser)
#         implement_download_file(browser, get_current_download_folder),

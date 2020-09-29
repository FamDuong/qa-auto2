from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.sites import YoutubePageLocators, GooglePageLocators, AnySite
from utils_automation.setup import WaitAfterEach


class YoutubePageElements(BasePageElement):

    def find_any_video_item(self, driver, text):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(YoutubePageLocators.any_video_item(text)))

    def find_search_button(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(YoutubePageLocators.SEARCH_BTN))

    def search_video(self, driver, text_search):
        search_field = self.wait_for_element(driver).until(
            ec.presence_of_element_located(YoutubePageLocators.SEARCH_BOX))
        search_field.click()
        search_field.send_keys(text_search)
        self.find_search_button(driver).click()

    def find_video_player_item(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(YoutubePageLocators.VIDEO_PLAYER_ITEM))


class GooglePageElements(BasePageElement):

    def find_search_field(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(GooglePageLocators.SEARCH_FIELD))

    def find_search_button(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(GooglePageLocators.SEARCH_BUTTON))

    def find_video_search_btn(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(GooglePageLocators.VIDEO_SEARCH_BTN))

    def find_savior_icon(self, driver):
        shadow_root = self.wait_for_element(driver).until(
            ec.presence_of_element_located(GooglePageLocators.SHADOW_ROOT_CONTENT))
        element = driver.execute_script('return arguments[0].shadowRoot', shadow_root)
        return element.find_element_by_css_selector(GooglePageLocators.SAVIOR_ICON)


class AnySiteElements(BasePageElement):

    def click_first_video_element(self, driver):
        return driver.execute_script('document.getElementsByTagName("video")[0].click()')

    def find_first_video_element(self, driver):
        return driver.execute_script('return document.getElementsByTagName("video")[0]')

    def find_video_element_24h(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(AnySite.TWENTY_FOUR_H_VIDEO_ITEM))

    def find_video_element_mouse_over_phimmoi(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(AnySite.PHIMMOI_VIDEO_MOUSE_OVER))

    def find_close_popup_continue_watching(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.PHIMMOI_CONTINUE_WATCHING_CLOSE_ELEMENT))

    def find_close_image_popup_phim_moi(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(AnySite.PHIMMOI_CLOSE_IMAGE_AD))

    def find_elements_close_pop_up_ads_phim_moi(self, driver):
        return driver.find_elements_by_xpath('//a[@class="close"]')

    def find_video_ad_length_phim_moi(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.PHIMMOI_VIDEO_AD_LENGTH_LOCATOR))

    def find_video_item_in_facebook_page(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.FACEBOOK_VIDEO_ITEM))

    def find_video_item_in_messenger_chat(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.MESSENGER_CHAT_VIDEO_ITEM))

    def find_play_button_in_messenger_chat(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.MESSENGER_CHAT_VIDEO_PLAY_BTN))

    def find_video_item_in_instagram(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.INSTAGRAM_VIDEO_ITEM))

    def find_video_item_in_kienthuc(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.KIENTHUC_VIDEO_ITEM))

    # def find_video_item_vietnamnet(self, driver):
    #     return self.wait_for_element(driver).until(
    #         ec.presence_of_element_located(AnySite.VIETNAMNET_VIDEO_ITEM))

    def find_video_item_eva_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.EVA_VN_VIDEO_ITEM))

    def find_video_item_twitter(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TWITTER_VIDEO_ITEM))

    def find_media_view_option_twitter(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TWITTER_MEDIA_VIEW_OPTION))

    def find_elements_user_restricted_twitter(self, driver):
        WaitAfterEach.sleep_timer_after_each_step()
        return driver.find_elements_by_xpath(AnySite.TWITTER_AUTHORIZE_RESTRICTED_USER_BTN)

    def find_element_user_restricted_parent_twitter(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TWITTER_AUTHORIZE_RESTRICTER_USER_PARENT_BTN))

    def find_video_item_soha(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(AnySite.SOHA_VIDEO_ITEM))

    def find_video_item_2sao_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.SAO_2_VN_VIDEO_ITEM))

    def find_video_item_phunu_giadinh(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.PHUNU_GIADINH_VIDEO_ITEM))

    def find_video_item_tien_phong(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TIEN_PHONG_VIDEO_ITEM))

    def find_play_video_item_tien_phong(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TIEN_PHONG_PLAY_VIDEO_ITEM))

    def find_video_item_bong_da_dot_com(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.BONG_DA_DOT_COM_VIDEO_ITEM))

    def find_video_item_gia_dinh_dot_net(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.GIA_DINH_DOT_NET_VIDEO_ITEM))

    def find_video_item_a_family(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.A_FAMILY_VN_VIDEO_ITEM))

    def find_video_item_gamek_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.GAME_K_VN_VIDEO_ITEM))

    def find_video_item_an_ninh_thu_do(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.AN_NINH_THU_DO_VIDEO_ITEM))

    def find_video_item_tuoi_tre(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TUOI_TRE_VIDEO_ITEM))

    def find_video_item_mot_phim(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(AnySite.MOT_PHIM_VIDEO_ITEM))

    def find_play_button_video_mot_phim(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_PLAY_VIDEO_BUTTON))

    def find_video_item_player_mot_phim(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_VIDEO_PLAYER))

    def find_video_episode_mot_phim(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_EPISODE_ITEM))

    def find_video_box_player_mot_phim(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_BOX_PLAYER))

    def find_skip_ads_btn_tv_hay(self, driver):
        return self.wait_for_element(driver, 100).until(
            ec.presence_of_element_located(AnySite.TV_HAY_VN_SKIP_ADD_BTN))

    def find_play_btn_tv_hay(self, driver):
        return self.find_element_if_exist(driver, AnySite.TV_HAY_VN_PLAY_BTN)

    def find_play_btn_in_frame_tv_hay(self, driver):
        return self.find_element_if_exist(driver, AnySite.TV_HAY_VN_PLAY_BTN_IN_FRAME)

    def find_iframe_tv_hay(self, driver):
        return self.find_element_if_exist(driver, AnySite.TV_HAY_VN_IFRAME_LEVEL)

    def find_video_item_tv_hay(self, driver):
        driver.switch_to.frame(self.find_element_if_exist(driver, AnySite.TV_HAY_VN_IFRAME_LEVEL))
        return self.find_element_if_exist(driver, AnySite.TV_HAY_VN_IFRAME_LEVEL)

    def find_pause_btn_tv_hay(self, driver):
        return self.wait_for_element(driver).until(ec.element_to_be_clickable(AnySite.TV_HAY_VN_PAUSE_BTN))

    def find_video_item_ngoi_sao_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.NGOI_SAO_VN_VIDEO_ITEM))

    def find_video_item_vtc_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.VTC_VN_VIDEO_ITEM))

    def find_video_play_item_vtc_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.VTC_VN_VIDEO_PLAY_ITEM))

    def find_video_item_kenh14_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.KENH14_VN_VIDEO_ITEM))

    def find_video_item_cafe_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.CAFE_VN_VIDEO_ITEM))

    def find_video_item_tin_tuc_online_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TIN_TUC_VN_VIDEO_ITEM))

    def find_video_iframe_tin_tuc_online_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TIN_TUC_VN_VIDEO_IFRAME))

    def find_video_detail_tin_tuc_online_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.TIN_TUC_VN_VIDEO_DETAIL))

    def find_video_item_giao_duc_thoi_dai(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.GIAO_DUC_THOI_DAI_VIDEO_ITEM))

    def find_video_item_vn_express(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.VNEXPRESS_VIDEO_ITEM))

    def find_video_item_thanh_nien(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.THANH_NIEN_VIDEO_ITEM))

    def find_video_item_dan_tri_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.DAN_TRI_VIDEO_ITEM))

    def find_play_btn_dan_tri_vn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.DAN_TRI_PLAY_VIDEO_BTN))

    def find_video_item_nguoi_lao_dong_tv(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(AnySite.NGUOI_LAO_DONG_VIDEO_ITEM))

    def find_nguoi_lao_dong_pause_btn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.NGUOI_LAO_DONG_PAUSE_BTN))

    def find_video_item_anime_sub_tv(self, driver):
        return self.wait_for_element(driver, timeout=20).until(
            ec.presence_of_element_located(AnySite.ANIME_VSUB_TV_VIDEO_ITEM))

    def find_continue_from_start_popup_btn_anime_sub_tv(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.ANIME_VSBUT_TV_CLOSE_POP_UP_WHERE_TO_START_VIDEO))

    def find_wait_for_player_load_anime_vsub_tv(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(
            AnySite.ANIME_VSUB_WAIT_FOR_LOAD_PLAYER_ITEM))

    def find_elements_wait_for_player_load_anime_vsub_tv(self, driver):
        return driver.find_elements_by_xpath(AnySite.ANIME_VSUB_WAIT_FOR_LOAD_PLAYER_ITEM_XPATH)

    def find_close_ad_btn_anime_vsub_tv(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.ANIME_VSUB_TV_CLOSE_AD_BUTTON))

    def find_play_btn_anime_vsub_tv(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.ANIME_VSUB_TV_PLAY_BUTTON))

    def find_video_item_nhac_vn(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.NHAC_VN_VIDEO_URL))

    def find_video_item_xvideos(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.XVIDEO_VIDEO_ITEM))

    def find_play_btn_x_videos(self, driver):
        return self.wait_for_element(driver).until(ec.element_to_be_clickable(AnySite.XVIDEO_PLAY_BTN))

    def find_video_item_xnxx(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(AnySite.XNXX_VIDEO_ITEM))

    def find_play_btn_xnxx(self, driver):
        return self.wait_for_element(driver).until(
            ec.element_to_be_clickable(AnySite.XNXX_PLAY_BTN)
        )

    def find_video_play_btn_fr_porn_hub(self, driver):
        return self.find_element_if_exist(driver, AnySite.FR_PORN_HUB_VIDEO_PLAY_BTN)

    def find_video_item_fr_porn_hub(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.FR_PORN_HUB_VIDEO_ITEM))

    def find_iframe_skip_ad_phimmoi(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.PHIMMOI_IFRAME_SKIP_AD_ITEM))

    def find_iframe_perol_skip_ad_phimmoi(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.PHIMMOI_IFRAME_MAIN_PEROL_ADS_ID))

    def find_skip_ad_button_phimmoi(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.PHIMMOI_SKIP_AD_BUTTON))

    def find_an_skip_ad_button_phimmoi(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIMMOI_SKIP_VIDEO_AD))

    @staticmethod
    def check_if_skip_button_phimmoi_appear(driver):
        return len(driver.find_elements_by_id(AnySite.PHIMMOI_SKIP_VIDEO_AD_ID))

    @staticmethod
    def check_if_bo_qua_quang_cao_button_phimmoi_appear(driver):
        return len(driver.find_elements_by_xpath(AnySite.PHIMMOI_BO_QUA_QUANG_CAO_XPATH))

    def find_bo_qua_quang_cao_phimmoi(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIMMOI_BO_QUA_QUANG_CAO))

    def find_video_item_vlxx(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.VLXX_VIDEO_ITEM))

    def find_video_item_wrapper_vlxx(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.VLXX_VIDEO_ITEM_WRAPPER))

    def find_video_item_sex_top1(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.SEX_TOP1_VIDEO_ITEM))

    def find_video_item_wrapper_sex_top1(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.SEX_TOP1_VIDEO_WRAPPER))

    def find_video_item_wrapper_sex_hihi(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.SEX_HIHI_VIDEO_WRAPPER))

    def find_video_item_sex_hihi(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.SEX_HIHI_VIDEO_ITEM))

    def find_video_wrapper_jav_hd_pro(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.JAV_HD_VIDEO_WRAPPER))

    def find_video_jav_hd_pro(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.JAV_HD_VIDEO_ITEM))

    def find_iframe_phim_sex_porn_item(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.PHIM_SEX_PORN_IFRAME))

    def find_phim_sex_porn_play_btn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIM_SEX_PORN_PLAY_BTN))

    def find_phim_sex_porn_video_item(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIM_SEX_PORN_VIDEO_ITEM))

    def find_video_phim_jav_phim_wrapper(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.JAV_PHIM_VIDEO_ITEM_WRAPPER))

    def find_video_phim_jav_phim_item(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.JAV_PHIM_VIDEO_ITEM))

    def find_video_item_tin_moi(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.TIN_MOI_VIDEO_ITEM))

    def find_video_item_info_net(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.INFO_NET_VIDEO_ITEM))

    def find_video_iframe_info_net(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.INFO_NET_VIDEO_IFRAME))

    def find_video_play_btn_info_net(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.INFO_NET_VIDEO_PLAY_BTN))

    def find_video_item_bong_da_24h(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.BONGDA_24H_VIDEO_ITEM))

    def find_video_item_keo_nha_cai(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.KEO_NHA_CAI_VIDEO_ITEM))

    def find_video_item_daily_motion(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.DAILY_MOTION_VIDEO_ITEM))

    def find_video_vov_vn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.VOV_VN_VIDEO_ITEM))

    def find_video_vov_vn_wrapper(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.VOV_VN_VIDEO_ITEM_WRAPPER))

    def find_video_vov_vn_iframe(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.VOV_VN_IFRAME))

    def find_vov_vn_play_btn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.VOV_VN_PLAY_BTN))

    def find_video_sex_ngon(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.SEX_NGON_VIDEO_ITEM))

    def find_video_weibo(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.WEIBO_VIDEO_ITEM))

    def find_video_element_vu_vi_phim(self, driver):
        return self.find_element_if_exist(driver, AnySite.VU_VI_PHIM_VIDEO_ELEMENT)

    def find_play_btn_vu_vi_phim(self, driver):
        return self.find_element_if_exist(driver, AnySite.VU_VI_PHIM_PLAY_BTN)

    def find_frame_vu_vi_phim(self, driver):
        return self.find_element_if_exist(driver, AnySite.VU_VI_PHIM_IFRAME)

    def find_server_anime_tvn(self, driver, server_number):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.anime_tvn_server(server_number)))

    def find_iframe_video_item_anime_tvn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.ANIME_TVN_IFRAME_VIDEO_ITEM))

    def find_video_item_anime_tvn(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.ANIME_TVN_VIDEO_ITEM))

    def find_video_phim_bat_hu(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIM_BAT_HU_VIDEO_ITEM))

    def find_iframe_phim_bat_hu(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIM_BAT_HU_IFRAME))

    def find_video_inner_phim_bat_hu(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIM_BAT_HU_VIDEO_INNER_ITEM))

    def find_video_phim_bat_hu_play(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIM_BAT_HU_PLAY_VIDEO_ITEM))

    def find_pause_btn_phim_bat_hu(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIM_BAT_HU_PAUSE_BTN))

    @staticmethod
    def find_pause_elements_phim_bat_hu(driver):
        return driver.find_elements_by_xpath(AnySite.PHIM_BAT_HU_PAUSE_BTN_XPATH)

    def find_video_phim_sex_sub_wrapper(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(
            AnySite.PHIM_SEX_SUB_VIDEO_ITEM_WRAPPER))

    def find_video_phim_sex_sub_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.PHIM_SEX_SUB_VIDEO_ITEM))

    def find_video_vlive_tv_item(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.VLIVE_TV_VIDEO_ITEM))

    def find_video_wrapper_anime_hay_tv(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.ANIME_HAY_TV_WRAPPER_VIDEO_ITEM))

    def find_video_iframe_anime_hay_tv(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.ANIME_HAY_TV_IFRAME_VIDEO_ITEM))

    def find_video_iframe_doi_song_phap_luat(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.DOI_SONG_PHAP_LUAT_IFRAME_VIDEO_ITEM))

    def find_video_player_doi_song_phap_luat(self, driver):
        return self.find_element_if_exist(driver, AnySite.DOI_SONG_PHAP_LUAT_PLAYER_VIDEO)

    def find_sao_star_video_item(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.SAO_STAR_VN_VIDEO_ITEM))

    @staticmethod
    def find_elements_play_middle_button_viet_sub_tv(driver):
        return driver.find_elements_by_xpath(AnySite.VIET_SUB_TV_PLAY_MIDDLE_BUTTON_XPATH)

    def find_play_middle_button_viet_sub_tv(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.VIET_SUB_TV_PLAY_MIDDLE_BUTTON))

    def find_viet_sub_tv_video_item(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.VIET_SUB_TV_PLAYER_VIDEO_ITEM))

    @staticmethod
    def find_elements_ad_not_appear(driver):
        return driver.find_elements_by_xpath(AnySite.VIET_SUB_TV_AD_NOT_APPEAR_ITEM_XPATH)

    def find_dong_phim_video_item(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.DONG_PHIM_VIDEO_ITEM))

    def find_nhac_cua_tui_ad_item(self, driver):
        return driver.find_elements_by_xpath('//div[@class="iframe_video vpaid_iframe"]')

    def find_nhac_cua_tui_ad_item_skip_button(self, driver):
        return self.wait_for_element(driver=driver, timeout=7).until(
            ec.presence_of_element_located(AnySite.NHAC_CUA_TUI_AD_ITEM_SKIP_BUTTON))

    def find_dong_phim_video_iframe(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.DONG_PHIM_VIDEO_IFRAME))

    def find_dong_phim_play_video_item(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.DONG_PHIM_PLAY_VIDEO_ITEM))

    @staticmethod
    def find_elements_dong_phim_play_video_btn(driver):
        return driver.find_elements_by_css_selector(AnySite.DONG_PHIM_PLAY_VIDEO_ITEM_CSS)

    def find_hentaiz_net_video_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.HENTAIZ_NET_VIDEO_ITEM))

    def find_hentaiz_net_play_btn(self, driver):
        return self.wait_for_element(driver).until(ec.element_to_be_clickable(AnySite.HENTAIZ_NET_PLAY_BTN))

    def find_vtv16_info_net_video_element(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.VTV16_INFO_NET_VIDEO_ITEM))

    def find_vtv16_info_net_iframe(self, driver):
        return self.wait_for_element(driver).until(
            ec.presence_of_element_located(AnySite.VTV16_INFO_NET_IFRAME_ELEMENT))

    def find_bestie_vn_iframe_1(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.BESTIE_VN_IFRAME_ELEMENT_1))

    def find_bestie_vn_iframe_2(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.BESTIE_VN_IFRAME_ELEMENT_2))

    def find_bestie_vn_video_player(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.BESTIE_VN_VIDEO_PLAYER))

    def find_clip_anime_vn_video_player(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.CLIP_ANIME_COM_VIDEO_PLAYER))

    def find_vtv_go_vn_video_player(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.VTV_GO_VN_VIDEO_ITEM))

    def find_xem_vtv_net_video_player(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.XEM_VTV_NET_VIDEO_PLAYER))

    def find_xem_vtv_net_play_btn(self, driver):
        return self.find_element_if_exist(driver, AnySite.XEM_VTV_NET_PLAY_BTN)

    def find_video_item_ok_ru(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.OK_RU_VIDEO_ITEM))

    def find_nhaccuatui_video_title(self, driver):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(AnySite.NHACCUATUI_VIDEO_TITLE))

    def count_zingmp3_chon_giao_dien_button(self, driver):
        count_chon_giao_dien_button = driver.find_elements_by_xpath(AnySite.CHON_GIAO_DIEN_SUBMIT_BTN_XPATH)
        return len(count_chon_giao_dien_button)

    def find_zingmp3_chon_giao_dien_button(self, driver):
        if self.count_zingmp3_chon_giao_dien_button(driver) > 0:
            return self.wait_for_element(driver).until(
                ec.presence_of_element_located(AnySite.CHON_GIAO_DIEN_SUBMIT_BTN))

    def find_vietnamnet_video_iframe(self, driver):
        return self.find_element_if_exist(driver, AnySite.VIETNAMENET_VIDEO_IFRAME)

    def find_video_item_vietnamnet(self, driver):
        driver.switch_to.frame(self.find_element_if_exist(driver, AnySite.VIETNAMENET_VIDEO_IFRAME))
        return self.find_element_if_exist(driver, AnySite.VIETNAMENET_VIDEO_IFRAME)

    def find_video_title(self, driver, element):
        return self.wait_for_element(driver).until(ec.presence_of_element_located(element))

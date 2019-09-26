from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.pageelements.basepage_elements import BasePageElement
from models.pagelocators.sites import YoutubePageLocators, GooglePageLocators, AnySite
from utils_automation.setup import WaitAfterEach


class YoutubePageElements(BasePageElement):

    @staticmethod
    def find_any_video_item(driver, text):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(YoutubePageLocators.any_video_item(text)))

    @staticmethod
    def find_search_button(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(YoutubePageLocators.SEARCH_BTN))

    def search_video(self, driver, text_search):
        wait = WebDriverWait(driver, 20)
        search_field = wait.until(
            ec.presence_of_element_located(YoutubePageLocators.SEARCH_BOX))
        search_field.click()
        search_field.send_keys(text_search)
        self.find_search_button(driver).click()

    @staticmethod
    def find_video_player_item(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(YoutubePageLocators.VIDEO_PLAYER_ITEM))


class GooglePageElements(BasePageElement):

    @staticmethod
    def find_search_field(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(GooglePageLocators.SEARCH_FIELD))

    @staticmethod
    def find_search_button(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(GooglePageLocators.SEARCH_BUTTON))

    @staticmethod
    def find_video_search_btn(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.element_to_be_clickable(GooglePageLocators.VIDEO_SEARCH_BTN))

    @staticmethod
    def find_savior_icon(driver):
        wait = WebDriverWait(driver, 20)
        shadow_root = wait.until(
            ec.presence_of_element_located(GooglePageLocators.SHADOW_ROOT_CONTENT))
        element = driver.execute_script('return arguments[0].shadowRoot', shadow_root)
        return element.find_element_by_css_selector(GooglePageLocators.SAVIOR_ICON)


class AnySiteElements(BasePageElement):

    @staticmethod
    def click_first_video_element(driver):
        return driver.execute_script('document.getElementsByTagName("video")[0].click()')

    @staticmethod
    def find_first_video_element(driver):
        return driver.execute_script('return document.getElementsByTagName("video")[0]')

    @staticmethod
    def find_video_element_24h(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.TWENTY_FOUR_H_VIDEO_ITEM))

    @staticmethod
    def find_video_element_phimmoi(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.PHIMMOI_VIDEO_ITEM))

    @staticmethod
    def find_video_element_mouse_over_phimmoi(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.PHIMMOI_VIDEO_MOUSE_OVER))

    @staticmethod
    def find_close_popup_continue_watching(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.PHIMMOI_CONTINUE_WATCHING_CLOSE_ELEMENT))

    @staticmethod
    def find_close_image_popup_phim_moi(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.PHIMMOI_CLOSE_IMAGE_AD))

    @staticmethod
    def find_elements_close_pop_up_ads_phim_moi(driver):
        return driver.find_elements_by_xpath('//a[@class="close"]')

    @staticmethod
    def find_video_ad_length_phim_moi(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.PHIMMOI_VIDEO_AD_LENGTH_LOCATOR))

    @staticmethod
    def find_video_item_in_facebook_page(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.FACEBOOK_VIDEO_ITEM))

    @staticmethod
    def find_video_item_in_messenger_chat(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.MESSENGER_CHAT_VIDEO_ITEM))

    @staticmethod
    def click_video_item_in_messenger_chat(driver):
        driver.execute_script('document.querySelector(arguments[0]).click()',
                              AnySite.MESSENGER_CHAT_VIDEO_ITEM_SELECTOR)

    @staticmethod
    def find_video_item_in_instagram(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.INSTAGRAM_VIDEO_ITEM))

    @staticmethod
    def find_video_item_in_kienthuc(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.KIENTHUC_VIDEO_ITEM))

    @staticmethod
    def find_video_item_vietnamnet(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VIETNAMNET_VIDEO_ITEM))

    @staticmethod
    def find_video_item_eva_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.EVA_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_item_twitter(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TWITTER_VIDEO_ITEM))

    @staticmethod
    def find_media_view_option_twitter(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TWITTER_MEDIA_VIEW_OPTION))

    @staticmethod
    def find_elements_user_restricted_twitter(driver):
        WaitAfterEach.sleep_timer_after_each_step()
        return driver.find_elements_by_xpath(AnySite.TWITTER_AUTHORIZE_RESTRICTED_USER_BTN)

    @staticmethod
    def find_element_user_restricted_parent_twitter(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TWITTER_AUTHORIZE_RESTRICTER_USER_PARENT_BTN))

    @staticmethod
    def find_video_item_soha(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.element_to_be_clickable(AnySite.SOHA_VIDEO_ITEM))

    @staticmethod
    def find_video_item_2sao_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.SAO_2_VN_VIDEO_ITEM))

    @staticmethod
    def find_watch_beginning_fpt_play(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.FPT_PLAY_WATCH_FROM_BEGINNING_BTN))

    @staticmethod
    def find_video_item_fpt_play(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.FPT_VIDEO_ITEM))

    @staticmethod
    def find_video_item_phunu_giadinh(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.PHUNU_GIADINH_VIDEO_ITEM))

    @staticmethod
    def find_video_item_tien_phong(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(AnySite.TIEN_PHONG_VIDEO_ITEM))

    @staticmethod
    def find_play_video_item_tien_phong(driver):
        wait = WebDriverWait(driver, 20)
        return wait.until(
            ec.presence_of_element_located(AnySite.TIEN_PHONG_PLAY_VIDEO_ITEM))

    @staticmethod
    def find_iframe_tien_phong(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TIEN_PHONG_IFRAME))

    @staticmethod
    def find_iframe_bong_da_dot_com(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.BONG_DA_DOT_COM_IFRAME))

    @staticmethod
    def find_video_item_bong_da_dot_com(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.BONG_DA_DOT_COM_VIDEO_ITEM))

    @staticmethod
    def find_video_item_gia_dinh_dot_net(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.GIA_DINH_DOT_NET_VIDEO_ITEM))

    @staticmethod
    def find_video_item_a_family(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.A_FAMILY_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_item_gamek_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.GAME_K_VN_VIDEO_ITEM))

    @staticmethod
    def find_iframe_vu_vi_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VU_VI_PHIM_IFRAME))

    @staticmethod
    def find_video_item_vu_vi_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VU_VI_PHIM_VIDEO_ITEM))

    @staticmethod
    def find_full_screen_button_vu_vi_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VU_VI_PHIM_FULL_SCREEN_BUTTON))

    @staticmethod
    def find_play_video_button_vu_vi_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VU_VI_PHIM_PLAY_VIDEO_BUTTON))

    @staticmethod
    def find_video_item_vu_vi_phim_js(driver):
        return driver.execute_script('return document.getElementById("media")')

    @staticmethod
    def find_video_item_an_ninh_thu_do(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.AN_NINH_THU_DO_VIDEO_ITEM))

    @staticmethod
    def find_video_item_tuoi_tre(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TUOI_TRE_VIDEO_ITEM))

    @staticmethod
    def find_video_item_mot_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_VIDEO_ITEM))

    @staticmethod
    def find_play_button_video_mot_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_PLAY_VIDEO_BUTTON))

    @staticmethod
    def find_video_item_player_mot_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_VIDEO_PLAYER))

    @staticmethod
    def find_video_episode_mot_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_EPISODE_ITEM))

    @staticmethod
    def find_video_box_player_mot_phim(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.MOT_PHIM_BOX_PLAYER))

    @staticmethod
    def find_video_item_vtv_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VTV_VN_VIDEO_ITEM))

    @staticmethod
    def find_skip_ads_btn_tv_hay(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TV_HAY_VN_SKIP_ADD_BTN))

    @staticmethod
    def find_play_btn_tv_hay(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TV_HAY_VN_PLAY_BTN))

    @staticmethod
    def find_video_item_tv_hay(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TV_HAY_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_item_ngoi_sao_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.NGOI_SAO_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_item_vtc_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VTC_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_play_item_vtc_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VTC_VN_VIDEO_PLAY_ITEM))

    @staticmethod
    def find_video_item_kenh14_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.KENH14_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_item_cafe_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.CAFE_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_item_tin_tuc_online_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TIN_TUC_VN_VIDEO_ITEM))

    @staticmethod
    def find_video_iframe_tin_tuc_online_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TIN_TUC_VN_VIDEO_IFRAME))

    @staticmethod
    def find_video_detail_tin_tuc_online_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.TIN_TUC_VN_VIDEO_DETAIL))

    @staticmethod
    def find_video_item_giao_duc_thoi_dai(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.GIAO_DUC_THOI_DAI_VIDEO_ITEM))

    @staticmethod
    def find_video_item_vn_express(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VN_EXPRESS_VIDEO_ITEM))

    @staticmethod
    def find_video_item_thanh_nien(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.THANH_NIEN_VIDEO_ITEM))

    @staticmethod
    def find_video_item_dan_tri_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.DAN_TRI_VIDEO_ITEM))

    @staticmethod
    def find_video_item_nguoi_lao_dong_tv(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.NGUOI_LAO_DONG_VIDEO_ITEM))

    @staticmethod
    def find_video_item_anime_sub_tv(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.ANIME_VSUB_TV_VIDEO_ITEM))

    @staticmethod
    def find_continue_from_start_popup_btn_anime_sub_tv(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.ANIME_VSBUT_TV_CLOSE_POP_UP_WHERE_TO_START_VIDEO))

    @staticmethod
    def find_close_ad_btn_anime_vsub_tv(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.ANIME_VSUB_TV_CLOSE_AD_BUTTON))

    @staticmethod
    def find_video_item_nhac_vn(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.NHAC_VN_VIDEO_URL))

    @staticmethod
    def find_video_item_xvideos(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.XVIDEO_VIDEO_ITEM))

    @staticmethod
    def find_video_item_xnxx(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.XNXX_VIDEO_ITEM))

    @staticmethod
    def find_video_item_fr_porn_hub(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.FR_PORN_HUB_VIDEO_ITEM))

    @staticmethod
    def find_iframe_skip_ad_phimmoi(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.PHIMMOI_IFRAME_SKIP_AD_ITEM))

    @staticmethod
    def find_iframe_perol_skip_ad_phimmoi(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.PHIMMOI_IFRAME_MAIN_PEROL_ADS_ID))

    @staticmethod
    def find_skip_ad_button_phimmoi(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.PHIMMOI_SKIP_AD_BUTTON))

    @staticmethod
    def find_video_item_vlxx(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VLXX_VIDEO_ITEM))

    @staticmethod
    def find_video_item_wrapper_vlxx(driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(
            ec.presence_of_element_located(AnySite.VLXX_VIDEO_ITEM_WRAPPER))





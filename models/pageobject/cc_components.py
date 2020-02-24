import time
from models.pagelocators.cc_components import CoccocComponentPageLocators
from models.pageobject.basepage_object import BasePageObject
from utils_automation.const import Urls


class ComponentsPageObject(BasePageObject):
    component_page_locators = CoccocComponentPageLocators()

    def verify_component(self, browser):
        time.sleep(30)
        browser.get(Urls.COCCOC_COMPONENTS)
        from models.pagelocators.cc_components import CoccocComponentPageLocators
        component_page_locators = CoccocComponentPageLocators()
        mei_preload_version = BasePageObject.get_text_element_by_id(browser,
                                                                    component_page_locators.COMPONENTS_MEI_PRELOAD_VERSION)
        legacy_tls_deprection_configuration_version = BasePageObject.get_text_element_by_id(browser,
                                                                                            component_page_locators.
                                                                                            COMPONENTS_LEGACY_TLS_DEPRECATION_CONFIGURATION_VERSION)
        third_party_module_list_version = BasePageObject.get_text_element_by_id(browser,
                                                                                component_page_locators.
                                                                                COMPONENTS_THIRD_PARTY_MODULE_LIST_VERSION)
        certificate_error_assistant_version = BasePageObject.get_text_element_by_id(browser,
                                                                                    component_page_locators.
                                                                                    COMPONENTS_CERTIFICATE_ERROR_ASSISTANT_VERSION)
        crlset_version = BasePageObject.get_text_element_by_id(browser,
                                                               component_page_locators.COMPONENTS_CRLSET_VERSION)
        pnacl_version = BasePageObject.get_text_element_by_id(browser,
                                                              component_page_locators.COMPONENTS_PNACL_VERSION)
        safety_tips_version = BasePageObject.get_text_element_by_id(browser,
                                                                    component_page_locators.COMPONENTS_SAFETY_TIPS_VERSION)
        file_type_polocies_version = BasePageObject.get_text_element_by_id(browser,
                                                                           component_page_locators.
                                                                           COMPONENTS_FILE_TYPE_POLOCIES_VERSION)
        origin_trials_version = BasePageObject.get_text_element_by_id(browser,
                                                                      component_page_locators.
                                                                      COMPONENTS_ORIGIN_TRIALS_VERSION)
        adobe_flash_player_version = BasePageObject.get_text_element_by_id(browser,
                                                                           component_page_locators.
                                                                           COMPONENTS_ADOBE_FLASH_PLAYER_VERSION)
        widevine_content_decryption_module_version = BasePageObject.get_text_element_by_id(browser,
                                                                                           component_page_locators.
                                                                                           COMPONENTS_WIDEVINE_CONTENT_DECRYPTION_MODULE_VERSION)
        coccoc_subresource_filter_rules_version = BasePageObject.get_text_element_by_id(browser,
                                                                                        component_page_locators.
                                                                                        COMPONENTS_COCCOC_SUBRESOURCE_FILTER_RULES_VERSION)

        from testscripts.smoketest.common import login_then_get_latest_coccoc_dev_installer_version
        expect_adobe_version = login_then_get_latest_coccoc_dev_installer_version()
        assert adobe_flash_player_version in expect_adobe_version
        assert adobe_flash_player_version is not '0.0.0.0'
        assert mei_preload_version is not '0.0.0.0'
        assert legacy_tls_deprection_configuration_version is not '0.0.0.0'
        assert third_party_module_list_version is not '0.0.0.0'
        assert certificate_error_assistant_version is not '0.0.0.0'
        assert crlset_version is not '0.0.0.0'
        assert pnacl_version is not '0.0.0.0'
        assert safety_tips_version is not '0.0.0.0'
        assert file_type_polocies_version is not '0.0.0.0'
        assert origin_trials_version == '0.0.0.0'
        assert widevine_content_decryption_module_version is not '0.0.0.0'
        assert coccoc_subresource_filter_rules_version is not '0.0.0.0'

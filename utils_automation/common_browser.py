import fileinput
import logging

from selenium import webdriver

from utils_automation.common import WindowsCMD, WindowsHandler
windows_handler = WindowsHandler()
current_user = windows_handler.get_current_login_user()

LOGGER = logging.getLogger(__name__)


def check_if_duplicates_list(list_of_elems):
    """ Check if given list contains any duplicates """
    set_of_elems = set()
    for elem in list_of_elems:
        if elem in set_of_elems:
            return True
        else:
            set_of_elems.add(elem)
    return False


def find_text_in_file(text_file_path, text_to_search):
    found = 0
    with fileinput.FileInput(text_file_path, inplace=True) as file:
        for line in file:
            if text_to_search in line:
                found += 1
                break
    return found


def modify_file_as_text(text_file_path, text_to_search, replacement_text):
    try:
        with fileinput.FileInput(text_file_path, inplace=True, backup='.bak') as file:
            for line in file:
                LOGGER.info(line.replace(text_to_search, replacement_text), end='')
    except:
        LOGGER.info("Preferences file is not existed")


def cleanup(coccoc_update=True, firefox=True):
    # Kill all unncessary task
    if coccoc_update:
        WindowsCMD.execute_cmd('taskkill /im CocCocUpdate.exe /f')
        WindowsCMD.execute_cmd('taskkill /im CocCocCrashHandler.exe /f')
        WindowsCMD.execute_cmd('taskkill /im CocCocTorrentUpdate.exe /f')
    WindowsCMD.execute_cmd('taskkill /im browser.exe /f')
    WindowsCMD.execute_cmd('taskkill /im MicrosoftEdge.exe /f')
    WindowsCMD.execute_cmd('taskkill /im MicrosoftEdgeCP.exe /f')
    WindowsCMD.execute_cmd('taskkill /im iexplore.exe /f')
    # WindowsCMD.execute_cmd('taskkill /im chrome.exe /f')
    if firefox:
        WindowsCMD.execute_cmd('taskkill /im firefox.exe /f')


def check_if_preferences_is_created(user_data_path):
    file_name = 'Preferences'
    path = "\"" + "C:\\Users" + user_data_path + "Default\""
    import subprocess
    p = subprocess.Popen(["powershell.exe",
                          f"Get-ChildItem -Path {path} -Filter {file_name} -Recurse " + "| %{$_.FullName}"],
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result = p.communicate()[0]
    if file_name in str(result):
        return True
    else:
        return False


def chrome_options_preset():
    binary_path = f"C:\\Users\\{current_user}\\AppData\\Local\\CocCoc\\Browser\\Application\\browser.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = binary_path
    # chrome_options.add_extension(
    #     "C:\\Users\\Hangnt2\\Downloads\\mpbjkejclgfgadiemmefgebjfooflfhl-0.7.3-Crx4Chrome.com.crx")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--proxy-server='direct://'")
    chrome_options.add_argument("--proxy-bypass-list=*")
    chrome_options.add_argument("--start-maximized")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--allow-insecure-localhost")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-application-cache")
    chrome_options.add_argument("--disable-session-crashed-bubble")
    chrome_options.add_argument("--disable-features=RendererCodeIntegrity")
    chrome_options.add_experimental_option("prefs", {'safebrowsing.enabled': 'false'})
    chrome_options.add_experimental_option("useAutomationExtension", False)
    chrome_options.add_experimental_option("excludeSwitches", ['enable-automation'])


    split_after = binary_path.split('\\Local')
    user_data_path = split_after[0] + u'\\Local\\CocCoc\\Browser\\User Data'
    chrome_options.add_argument('--user-data-dir=' + user_data_path)
    if check_if_preferences_is_created(user_data_path):
        modify_file_as_text(user_data_path + '\\Default\\Preferences', 'Crashed', 'none')

    return chrome_options


def coccoc_instance(is_needed_clean_up=True):
        if is_needed_clean_up is True:
            cleanup()
        else:
            pass
        return webdriver.Chrome(options=chrome_options_preset())
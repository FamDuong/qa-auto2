import logging
import subprocess
import time
import psutil
import os
import multiprocessing as mp
import concurrent.futures

from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from utils_automation.common import get_from_csv, write_result_data_for_cpu_ram
from selenium import webdriver
from pytest_testrail.plugin import pytestrail
from utils_automation.cleanup import Browsers

LOGGER = logging.getLogger(__name__)


class TestCPURAM:

    def get_cpu_per_single_process(self, pid):
        try:
            current_cpu_utilization = psutil.Process(pid).cpu_percent(interval=2)
            if current_cpu_utilization is None:
                current_cpu_utilization = 0.0
            return current_cpu_utilization / psutil.cpu_count()
        except Exception as e:
            print('EXCEPTION:', e)
            return 0.0

    def get_memory_per_single_process(self, pid):
        try:
            memory_infor_pid = psutil.Process(pid).memory_info()[1]
            if memory_infor_pid is None:
                memory_infor_pid = 0.0
            return memory_infor_pid / float(2 ** 20)
        except Exception as e:
            print('EXCEPTION:', e)
            return 0.0

    def PID(self, process_name):
        pid_list = [p.info['pid'] for p in psutil.process_iter(attrs=['pid', 'name']) if process_name in p.info['name']]
        return pid_list

    def benchmark(self, pid_list):
        cpus = mp.cpu_count()  # check available memory of cpu
        start = time.perf_counter()  # point of time for starting running

        try:
            with concurrent.futures.ThreadPoolExecutor(cpus) as executor:
                total_cpu = 0
                total_mem = 0
                try:
                    for pid, cpu in zip(pid_list, executor.map(self.get_cpu_per_single_process, pid_list)):
                        print('%d has cpu usage: %s' % (pid, cpu))
                        total_cpu = total_cpu + cpu
                    for pid, memory in zip(pid_list, executor.map(self.get_memory_per_single_process, pid_list)):
                        print('%d has memory usage: %s' % (pid, memory))
                        total_mem = total_mem + memory
                except Exception as e:
                    print(e)
            end = time.perf_counter()
            print("All jobs finished in {}s".format(round(end - start, 2)))
            print("Total CPU used = %s" % total_cpu)
            print("Total Mem used = %s" % total_mem)
            return total_cpu, total_mem
        except Exception:
            print("Some pid is unavailable")

    def open_webpage_withtabs(self, filename, binary_file, default_dir, options_list=None, enabled_ads_block=False):
        browser = Browsers()
        browser.kill_all_browsers()

        listweb = get_from_csv(filename)
        opts = Options()
        opts.binary_location = binary_file
        opts.add_argument("start-maximized")
        opts.add_argument('user-data-dir=' + default_dir)
        if enabled_ads_block == "True":
            opts.add_argument("--start-maximized")
            opts.add_argument("--proxy-server='direct://'")
            opts.add_argument("--proxy-bypass-list=*")
            opts.add_argument("--start-maximized")
            opts.add_argument('--disable-gpu')
            opts.add_argument('--disable-dev-shm-usage')
            opts.add_argument('--no-sandbox')
            opts.add_argument('--ignore-certificate-errors')
            opts.add_argument("--allow-insecure-localhost")
            opts.add_argument("--enable-features=CocCocBlockAdByExtension")
        caps = DesiredCapabilities().CHROME
        # caps["pageLoadStrategy"] = "normal"  # complete
        caps["pageLoadStrategy"] = "eager"

        if options_list is not None:
            for i in options_list:
                opts.add_argument(i)
        # driver = webdriver.Chrome(executable_path=cc_driver, chrome_options=opts)
        # driver = webdriver.Chrome('/Users/itim/Downloads/python/chromedriver') #Environment: MAC OS
        driver = webdriver.Chrome(options=opts, desired_capabilities=caps)

        # first tab
        driver.get(listweb[0])

        # next tab
        for i in range(len(listweb)):
            if i + 1 < len(listweb):
                tabname = str(i + 1)
                jscommand = "window.open('about:blank', \'" + tabname + "\');"
                driver.execute_script(jscommand)
                driver.switch_to.window(tabname)
                print("%d . Open tab page: %s" % (i + 1, listweb[i + 1]))
                driver.get(listweb[i + 1])
        return driver

    def get_ram_cpu(self, filename, file_name_result, binary_file, default_dir, options_list=None,
                    enabled_ads_block=False):
        res = []
        i = 1
        LOGGER.info('%-25s' '%-60s' '%s' % ('No.', 'CPU', 'Memory'))
        for _ in range(10):
            browser = self.open_webpage_withtabs(filename, binary_file, default_dir, options_list,
                                                 enabled_ads_block=enabled_ads_block)
            pid_list = self.PID('browser')
            cpu, mem = self.benchmark(pid_list)
            res.append({"cpu": cpu, "mem": mem})
            LOGGER.info('%-25s' '%-60s' '%s' % (i, cpu, mem))
            i += 1
            browser.quit()
        write_result_data_for_cpu_ram(file_name_result, res, result_type='CPU RAM')

    @pytestrail.case('C82490')
    def test_ram_cpu(self, binary_path, default_directory, application_path, get_enabled_adblock_extension):
        # Define test filename
        enabled_adblock_extension = get_enabled_adblock_extension
        if enabled_adblock_extension == "True":
            subprocess.Popen(["powershell.exe",
                              f"cd {application_path}; .\\browser.exe --enable-features=CocCocBlockAdByExtension"],
                             stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            time.sleep(10)
            subprocess.Popen("taskkill /im browser.exe /f", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + r'\test_data' + r"\testbenchmark.csv"
        file_name_result = dirname + r'\test_result' + r"\results_cpu_ram.csv"
        self.get_ram_cpu(filename, file_name_result, binary_path, default_directory, None,
                         enabled_ads_block=enabled_adblock_extension)

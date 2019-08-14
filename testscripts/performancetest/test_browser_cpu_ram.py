import utils_automation.common as excelfile
import time
import settings_master as settings
import psutil
import os
import multiprocessing as mp
import concurrent.futures
from utils_automation.cleanup import Browsers
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from pytest_testrail.plugin import pytestrail


class TestCPURAM:
    def get_cpu_per_single_process(self, pid):
        try:
            return psutil.Process(pid).cpu_percent(interval=2) / psutil.cpu_count()
        except Exception as e:
            print('EXCEPTION:', e)


    def get_memory_per_single_process(self, pid):
        try:
            return psutil.Process(pid).memory_info()[1] / float(2 ** 20)
        except Exception as e:
            print('EXCEPTION:', e)


    def PID(self, process_name):
        pid_list = [p.info['pid'] for p in psutil.process_iter(attrs=['pid', 'name']) if process_name in p.info['name']]
        return pid_list


    def benchmark(self, pid_list):
        cpus = mp.cpu_count()  # check available memory of cpu
        start = time.clock()  # point of time for starting running

        try:
            with concurrent.futures.ThreadPoolExecutor(cpus) as executor:
                total_cpu = 0
                total_mem = 0
                for pid, cpu in zip(pid_list, executor.map(self.get_cpu_per_single_process, pid_list)):
                    print('%d has cpu usage: %s' % (pid, cpu))
                    total_cpu = total_cpu + cpu
                for pid, memory in zip(pid_list, executor.map(self.get_memory_per_single_process, pid_list)):
                    print('%d has memory usage: %s' % (pid, memory))
                    total_mem = total_mem + memory
            end = time.clock()
            print("All jobs finished in {}s".format(round(end - start, 2)))
            print("Total CPU used = %s" % total_cpu)
            print("Total Mem used = %s" % total_mem)
            return total_cpu, total_mem
        except Exception:
            print("Some pid is unavailable")


    def open_webpage_withtabs(self, filename, binary_file, options_list=None):
        browser = Browsers();
        browser.kill_all_browsers()

        listweb = excelfile.get_from_csv(filename)
        opts = Options()
        opts.binary_location = binary_file
        opts.add_argument("start-maximized")
        if options_list is not None:
            for i in options_list:
                opts.add_argument(i)

        # driver = webdriver.Chrome(executable_path=cc_driver, chrome_options=opts)
        # driver = webdriver.Chrome('/Users/itim/Downloads/python/chromedriver') #Environment: MAC OS
        driver = webdriver.Chrome(chrome_options=opts)

        # first tab
        driver.get(listweb[0]);

        # next tab
        for i in range(len(listweb)):
            if i + 1 < len(listweb):
                tabname = str(i + 1)
                jscommand = "window.open('about:blank', \'" + tabname + "\');"
                driver.execute_script(jscommand)
                driver.switch_to.window(tabname)
                driver.get(listweb[i + 1])
        return driver

    def get_ram_cpu(self, filename, binary_file, options_list=None):
        res = []
        for _ in range(10):
            browser = self.open_webpage_withtabs(filename, binary_file, options_list)
            pid_list = self.PID('browser')
            cpu, mem = self.benchmark(pid_list)
            res.append({"cpu": cpu, "mem": mem})
            browser.quit()
        for i in range(len(res)):
            print("i is %d" % i)
            print("CPU is %s, Mem is %s" % (res[i].get("cpu"), res[i].get("mem")))

    @pytestrail.case('C82490')
    def test_ram_cpu(self):
        # Define test filename
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + r"\testbenchmark.csv"
        # filename = os.path.abspath(r".\testbenchmark.csv")

        options_list = {"--enable-features=NetworkService"}
        self.get_ram_cpu(filename, settings.COCCOC_PATH, None)
        self.get_ram_cpu(filename, settings.COCCOC_PATH, options_list)
        self.get_ram_cpu(filename, settings.CHROME_PATH, None)



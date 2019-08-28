import os
import csv
import sys

from selenium.webdriver import ActionChains

from utils_automation.setup import WaitAfterEach


class CSVHandle:
    def get_from_csv(self, filename):
        list_temp = []
    # dirname, runname = os.path.split(os.path.abspath(__file__))
    # filename = dirname + filename
        with open(filename, 'r', newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            print("CSV Reader: READING CSV FILE >>", filename)
            try:
                for row in reader:
                    for q in row:
                        if q == None or len(q) == 0:
                            pass
                        else:
                            list_temp.append(q)
                print("CSV Reader: FINISHED READING CSV FILE =>", filename)
                return list_temp
            except csv.Error as i:
                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, i))
                return None
            except EOFError as e:
                print("Can not read file CSV:", filename)
                print("System error:", e)
                return None


class FilesHandle:
    def get_absolute_filename(self, filename):
        dirname, runname = os.path.split(os.path.abspath(__file__))
        filename = dirname + filename
        return filename

    def find_files_in_folder_by_modified_date(self, mydir, endwith):
        filelist = [f for f in os.listdir(mydir) if f.endswith(endwith)]
        return filelist

    @staticmethod
    def clear_downloaded_folder(folder):
        from utils_automation.cleanup import Files
        files = Files()
        files.delete_all_files_in_folder(folder)


class WebElements:

    @staticmethod
    def mouse_over_element(driver, element):
            hov = ActionChains(driver).move_to_element(element)
            hov.perform()


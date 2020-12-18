import lxml.html
import urllib.request
import urllib
# import lxml.html
# from urllib.parse import urlsplit
# import re
# import requests
# import feedparser
# from PIL import Image
# from io import BytesIO
# import os
# from newspaper import Article
# import metadata_parser
# from bs4 import BeautifulSoup
# from newsfetch.news import newspaper
# from newsplease import NewsPlease
# from datetime import datetime
# import inspect
# import time
import csv
import sys
import shutil
import os
from shutil import move
from tempfile import NamedTemporaryFile
from utils_automation.setup import WaitAfterEach
from PIL import Image

import logging

LOGGER = logging.getLogger(__name__)


class FileUtils():

    def create_empty_folder(self, foldername):
        LOGGER.info(foldername)
        if os.path.exists(foldername):
            os.chmod(foldername, 0o777)
            shutil.rmtree(foldername)
        os.makedirs(foldername, 0o777)

    def remove_file(self, filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            LOGGER.info('File does not exists')

    # Append list to a file
    def append_list_to_file(self, filename, input_lists, type="list"):
        if type == "string":
            input_lists = [input_lists]
        if os.path.exists(filename):
            file = open(filename, 'a', encoding="utf-8")
        else:
            file = open(filename, 'w+', encoding="utf-8")
        for i in input_lists:
            if i != '' and i is not None:
                file.write("%s\n" % (i))
        file.close()

    # Append s ring to a file
    def append_to_file(self, filename, string):
        if os.path.exists(filename):
            file = open(filename, 'a', encoding="utf-8")
        else:
            file = open(filename, 'w+', encoding="utf-8")
        if string != '' and string is not None:
            file.write("%s\n" % string)
        file.close()

    def get_current_dirname(self):
        dirname, runname = os.path.split(os.path.abspath(__file__))
        LOGGER.info(dirname)
        return dirname

    def get_from_csv(self, filename):
        LOGGER.info(filename)
        list_temp = []
        # dirname, runname = os.path.split(os.path.abspath(__file__))
        # filename = dirname + filename
        with open(filename, 'r', newline='', encoding="utf-8") as f:
            reader = csv.reader(f)
            # print("CSV Reader: READING CSV FILE >>", filename)
            try:
                for row in reader:
                    for q in row:
                        if q == None or len(q) == 0:
                            pass
                        else:
                            list_temp.append(q)
                # LOGGER.info("CSV Reader: FINISHED READING CSV FILE =>", filename)
                return list_temp
            except csv.Error as i:
                sys.exit('file {}, line {}: {}'.format(filename, reader.line_num, i))
                return None
            except EOFError as e:
                LOGGER.info("Can not read file CSV:", filename)
                # LOGGER.info("System error:", e)
                return None
            finally:
                f.close()

    # Copy file to other folder
    def copy_file(self, file_source, folder_destination):
        shutil.copy(file_source, folder_destination, follow_symlinks=True)

    def remove_first_line_in_file(self, filename):
        temp_path = None
        with open(filename, 'r') as f_in:
            with NamedTemporaryFile(mode='w', delete=False) as f_out:
                temp_path = f_out.name
                next(f_in)  # skip first line
                for line in f_in:
                    f_out.write(line)
        os.remove(filename)
        move(temp_path, filename)

    def clear_content_file(self, file_name):
        with open(file_name, 'a', encoding='utf-8') as file:
            file.truncate(0)

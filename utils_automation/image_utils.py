import os
import time
import cv2
from PIL import Image
from skimage import io
from Screenshot import Screenshot_Clipping

import logging
LOGGER = logging.getLogger(__name__)

class ImageUtils():
    THRESHOLD_DARKMODE_DOMINANT = (45, 45, 45)
    THRESHOLD_LIGHTMODE_DOMINANT = (238, 221, 130)
    dominant = None

    def get_screenshot(self, driver, filename):
        LOGGER.info("Starting chrome full page screenshot workaround ...")
        driver.get_screenshot_as_file(filename)
        LOGGER.info("Finishing chrome full page screenshot workaround...")
        return True

    def get_fullpage_screenshot_clipping(self, driver, path, filename):
        ob = Screenshot_Clipping.Screenshot()
        img_url = ob.full_Screenshot(driver, save_path=path, image_name=filename)

    def get_fullpage_screenshot_screen(self, filename):
        import pyautogui
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)

    def get_fullpage_screenshot(self, driver, filename):

        LOGGER.info("Starting chrome full page screenshot workaround ...")

        total_width = driver.execute_script("return document.body.offsetWidth")
        total_height = driver.execute_script("return document.body.parentNode.scrollHeight")
        viewport_width = driver.execute_script("return document.body.clientWidth")
        viewport_height = driver.execute_script("return window.innerHeight")
        print(
            "Total: ({0}, {1}), Viewport: ({2},{3})".format(total_width, total_height, viewport_width, viewport_height))
        rectangles = []

        i = 0
        while i < total_height:
            ii = 0
            top_height = i + viewport_height

            if top_height > total_height:
                top_height = total_height

            while ii < total_width:
                top_width = ii + viewport_width

                if top_width > total_width:
                    top_width = total_width

                print("Appending rectangle ({0},{1},{2},{3})".format(ii, i, top_width, top_height))
                rectangles.append((ii, i, top_width, top_height))

                ii = ii + viewport_width

            i = i + viewport_height

        stitched_image = Image.new('RGB', (total_width, total_height))
        previous = None
        part = 0

        for rectangle in rectangles:
            if not previous is None:
                driver.execute_script("window.scrollTo({0}, {1})".format(rectangle[0], rectangle[1]))
                print("Scrolled To ({0},{1})".format(rectangle[0], rectangle[1]))
                time.sleep(0.2)

            file_name = "part_{0}.png".format(part)
            print("Capturing {0} ...".format(file_name))

            driver.get_screenshot_as_file(file_name)
            screenshot = Image.open(file_name)

            if rectangle[1] + viewport_height > total_height:
                offset = (rectangle[0], total_height - viewport_height)
            else:
                offset = (rectangle[0], rectangle[1])

            LOGGER.info("Adding to stitched image with offset ({0}, {1})".format(offset[0], offset[1]))
            stitched_image.paste(screenshot, offset)

            del screenshot
            os.remove(file_name)
            part = part + 1
            previous = rectangle

        stitched_image.save(filename)
        LOGGER.info("Finishing chrome full page screenshot workaround...")
        return True

    # Get dominat color as RGB format
    def get_dominant_color(self, image_name):
        im = Image.open(image_name)
        dominant = max(im.getcolors(im.size[0] * im.size[1]))
        LOGGER.info(dominant)
        number_of_colors = dominant[0]
        dominant_color = dominant[1]
        LOGGER.info(dominant_color)
        return dominant_color

    # Convert color
    # Input: tuple of color
    def rgb2hex(self, r, g = 0, b = 0):
        if isinstance(r, tuple):
            g = r[1]
            b = r[2]
            r = r[0]
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    # Convert color
    # Input: tuple of color
    def hex2rgb(self, hexcode):
        return tuple(map(ord, hexcode[1:].decode('hex')))

    # Convert color
    def rgb2int(self, r, g = 0, b = 0):
        if isinstance(r, tuple):
            g = r[1]
            b = r[2]
            r = r[0]
        rgb_int = (r << 16) + (g << 8) + b
        LOGGER.info(rgb_int)
        return rgb_int

    # Compare colors
    def compare_dominant_color_threshold(self, image, dark_mode = True):
        result = True
        image_dominant = self.rgb2int(image)
        if dark_mode:
            threshold = self.rgb2int(self.THRESHOLD_DARKMODE_DOMINANT)
            LOGGER.info("Expect Darkmode: %s < %s" % (str(image_dominant), str(threshold)))
            if image_dominant > threshold:
                LOGGER.info("Dominant color is not Darkmode !!!")
                result = False
        else:
            threshold = self.rgb2int(self.THRESHOLD_LIGHTMODE_DOMINANT)
            LOGGER.info("Expect Lightmode: %s > %s" % (str(image_dominant), str(threshold)))
            if image_dominant < threshold:
                LOGGER.info("Dominant color is not Lightmode !!!")
                result = False
        return result

    # Find sub image in main image
    def find_subimage_in_image(self, main_image, sub_image, threshold=0.81):
        LOGGER.info(main_image)
        LOGGER.info(sub_image)
        # LOGGER.info(sub_image)
        is_find = True
        method = cv2.TM_CCOEFF_NORMED

        # Read the images from the file
        small_image = cv2.imread(sub_image)
        # small_image = io.imread(sub_image)
        large_image = cv2.imread(main_image)
        # large_image = io.imread(main_image)

        result = cv2.matchTemplate(small_image, large_image, method)

        # We want the minimum squared difference
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        LOGGER.info(max_val)
        if max_val > threshold:
            is_find = True
        else:
            is_find = False
        return is_find
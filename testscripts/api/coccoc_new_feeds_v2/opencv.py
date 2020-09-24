import sys                      # System bindings
import cv2                      # OpenCV bindings
import numpy as np
import logging
from collections import Counter
from base64 import b16encode
LOGGER = logging.getLogger(__name__)


class BackgroundColorDetector():
    def __init__(self, imageLoc):
        self.img = cv2.imread(imageLoc, 1)
        self.manual_count = {}
        self.w, self.h, self.channels = self.img.shape
        self.total_pixels = self.w*self.h

    def count(self):
        for y in range(0, self.h):
            for x in range(0, self.w):
                RGB = (self.img[x, y, 2], self.img[x, y, 1], self.img[x, y, 0])
                if RGB in self.manual_count:
                    self.manual_count[RGB] += 1
                else:
                    self.manual_count[RGB] = 1

    def average_colour(self):
        red = 0
        green = 0
        blue = 0
        sample = 10
        for top in range(0, sample):
            red += self.number_counter[top][0][0]
            green += self.number_counter[top][0][1]
            blue += self.number_counter[top][0][2]

        average_red = red / sample
        average_green = green / sample
        average_blue = blue / sample
        LOGGER.info("Average RGB for top ten is: (", average_red,
              ", ", average_green, ", ", average_blue, ")")
        triplet = (int(average_red), int(average_green), int(average_blue))
        LOGGER.info(b'#' + b16encode(bytes(triplet)))

    def twenty_most_common(self):
        self.count()
        self.number_counter = Counter(self.manual_count).most_common(20)
        for rgb, value in self.number_counter:
            LOGGER.info(rgb, value, ((float(value)/self.total_pixels)*100))

    def detect(self):
        self.twenty_most_common()
        self.percentage_of_first = (
            float(self.number_counter[0][1])/self.total_pixels)
        LOGGER.info(self.percentage_of_first)
        if self.percentage_of_first > 0.5:
            LOGGER.info("Background color is ", self.number_counter[0][0])
        else:
            self.average_colour()


from sklearn.cluster import KMeans
from collections import Counter
import cv2  # for resizing image

class DominantColorDetector():

    def get_dominant_color(image, k=4, image_processing_size=None):
        """
        takes an image as input
        returns the dominant color of the image as a list

        dominant color is found by running k means on the
        pixels & returning the centroid of the largest cluster

        processing time is sped up by working with a smaller image;
        this resizing can be done with the image_processing_size param
        which takes a tuple of image dims as input

        >>> get_dominant_color(my_image, k=4, image_processing_size = (25, 25))
        [56.2423442, 34.0834233, 70.1234123]
        """
        # resize image if new dims provided
        image = "image_1.jpg"
        if image_processing_size is not None:
            image = cv2.resize(image, image_processing_size,
                           interpolation=cv2.INTER_AREA)

        # reshape the image to be a list of pixels
        image = image.reshape((image.shape[0] * image.shape[1], 3))

        # cluster and assign labels to the pixels
        clt = KMeans(n_clusters=k)
        labels = clt.fit_predict(image)

        # count labels to find most popular
        label_counts = Counter(labels)

        # subset out most popular centroid
        dominant_color = clt.cluster_centers_[label_counts.most_common(1)[0][0]]
        LOGGER.info(dominant_color)

        return list(dominant_color)

if __name__ == "__main__":
    if (len(sys.argv) != 2):                        # Checks if image was given as cli argument
        LOGGER.info("error: syntax is 'python main.py /example/image/location.jpg'")
    else:
        BackgroundColor = BackgroundColorDetector(sys.argv[1])
        BackgroundColor.detect()
        DominantColorDetector = DominantColorDetector()
        DominantColorDetector.get_dominant_color()
import numpy as np
from skimage.io import imread
from skimage import restoration
from skimage import measure
from skimage.measure import regionprops
from skimage.filters import threshold_otsu
from skimage.transform import resize

class PreProcess():
    
    def __init__(self, image_location):
     
        self.full_car_image = imread(image_location, as_grey=True)
        
        self.full_car_image = self.resize_if_necessary(self.full_car_image)

        self.binary_image = self.threshold(self.full_car_image)
        
    def denoise(sefl, imgDetails):
        return restoration.denoise_tv_chambolle(imgDetails)
        
    def threshold(self, gray_image):
        thresholdValue = threshold_otsu(gray_image)
        return gray_image > thresholdValue
        
    def get_plate_like_objects(self):

        self.label_image = measure.label(self.binary_image)
        self.plate_objects_cordinates = []
        threshold = self.binary_image
        plate_dimensions = (0.08*threshold.shape[0], 0.2*threshold.shape[0], 0.09*threshold.shape[1], 0.8*threshold.shape[1])
        minHeight, maxHeight, minWidth, maxWidth = plate_dimensions
        plate_like_objects = []
        for region in regionprops(self.label_image):
            if region.area < 10:
                continue
        
            minimumRow, minimumCol, maximumRow, maximumCol = region.bbox
            regionHeight = maximumRow - minimumRow
            regionWidth = maximumCol - minimumCol
            if regionHeight >= minHeight and regionHeight <= maxHeight and regionWidth >= minWidth and regionWidth <= maxWidth and regionWidth > regionHeight:
                plate_like_objects.append(self.full_car_image[minimumRow:maximumRow,
                    minimumCol:maximumCol])
                self.plate_objects_cordinates.append((minimumRow, minimumCol,
                    maximumRow, maximumCol))
                
        return plate_like_objects

    def validate_plate(self, candidates):
    
        for each_candidate in candidates:
            height, width = each_candidate.shape
            each_candidate = self.inverted_threshold(each_candidate)
            license_plate = []
            highest_average = 0
            total_white_pixels = 0
            for column in range(width):
                total_white_pixels += sum(each_candidate[:, column])
            
            average = float(total_white_pixels) / width
            if average >= highest_average:
                license_plate = each_candidate

        return license_plate

    def inverted_threshold(self, grayscale_image):
        threshold_value = threshold_otsu(grayscale_image) - 0.05
        return grayscale_image < threshold_value

    def resize_if_necessary(self, image_to_resize):
        height, width = image_to_resize.shape
        ratio = float(width) / height
        # resize l'image
        if width > 600:
            width = 600
            height = round(width / ratio)
            return resize(image_to_resize, (height, width))

        return image_to_resize
#!/usr/bin/python

import pyexiv2
import fractions
from PIL import Image
from PIL.ExifTags import TAGS

def get_exif_data(image_path):
	
	exiv_image = pyexiv2.ImageMetadata(image_path)
	exiv_image.read()
	print exiv_image.exif_keys
	exif_keys = exiv_image.exif_keys
	
	if ("Exif.GPSInfo.GPSLatitude" in exif_keys and "Exif.GPSInfo.GPSLongitude" in exif_keys and "Exif.GPSInfo.GPSLongitudeRef" in exif_keys and "Exif.GPSInfo.GPSLatitudeRef" in exif_keys):
		# convert rational values into decimal
		tag_lat = exiv_image["Exif.GPSInfo.GPSLatitude"]
		tag_lng = exiv_image["Exif.GPSInfo.GPSLongitude"]
		lat = float(tag_lat.value[0].numerator/tag_lat.value[0].denominator) + float(float(tag_lat.value[1].numerator/tag_lat.value[1].denominator)/ 60) + float(float(tag_lat.value[2].numerator/tag_lat.value[2].denominator)/ 3600)
		lng = float(tag_lng.value[0].numerator/tag_lng.value[0].denominator) + float(float(tag_lng.value[1].numerator/tag_lng.value[1].denominator)/ 60) + float(float(tag_lng.value[2].numerator/tag_lng.value[2].denominator)/ 3600)
		
	if exiv_image["Exif.GPSInfo.GPSLongitudeRef"].raw_value == "W":
		lng = lng * -1    # (W is -, E is +)
	if exiv_image["Exif.GPSInfo.GPSLatitudeRef"].raw_value == "S":
		lat = lat * -1
		
	print lat, lng
	
get_exif_data("sample.jpg")

#'Exif.Image.GPSTag'
#'Exif.GPSInfo.GPSVersionID'
#'Exif.GPSInfo.GPSLatitudeRef'
#'Exif.GPSInfo.GPSLatitude'
#'Exif.GPSInfo.GPSLongitudeRef'
#'Exif.GPSInfo.GPSLongitude'
#'Exif.GPSInfo.GPSAltitudeRef'
#'Exif.GPSInfo.GPSAltitude'
#'Exif.GPSInfo.GPSTimeStamp'
#'Exif.GPSInfo.GPSMapDatum' 
#'Exif.GPSInfo.GPSDateStamp'

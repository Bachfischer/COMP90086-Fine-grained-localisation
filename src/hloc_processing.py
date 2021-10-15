# Create query_list_with_intrinsics.txt

import csv

# Overview of Camera Type: https://github.com/colmap/colmap/blob/master/src/base/camera_models.h
# based on https://data.ciirc.cvut.cz/public/projects/2020VisualLocalization/Aachen-Day-Night/queries/night_time_queries_with_intrinsics.txt


# Structure: CAMERA_TYPE PIXEL_WIDTH PIXEL_HEIGHT f, cx, cy
# f: focal length
# cx, cy: principal point at pixel location (i.e. center of image)
# TODO: Try to calculate correct focal length
CAMERA_PARAMETERS = " SIMPLE_PINHOLE 680 490 1000 340 245"


with open('../data/COMP90086_2021_Project_test/imagenames.csv', newline='') as infile, open('query_list_with_intrinsics.txt', 'w') as outfile:
    reader = csv.reader(infile, delimiter=',')
    # skip the headers
    next(reader, None)  
    for row in reader:
        filename = "test/" + row[0]
        output_line = filename + CAMERA_PARAMETERS
        outfile.write(output_line + '\n')
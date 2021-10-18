# Create query_list_with_intrinsics.txt

import csv

def generate_query_list_with_intrinsics_file():
    
    # Overview of Camera Type: https://github.com/colmap/colmap/blob/master/src/base/camera_models.h
    # based on https://data.ciirc.cvut.cz/public/projects/2020VisualLocalization/Aachen-Day-Night/queries/night_time_queries_with_intrinsics.txt


    # Structure: CAMERA_TYPE PIXEL_WIDTH PIXEL_HEIGHT f, cx, cy
    # f: focal length
    # cx, cy: principal point at pixel location (i.e. center of image)
    # TODO: Try to calculate correct focal length
    CAMERA_PARAMETERS = " SIMPLE_PINHOLE 680 490 1000 340 245"

    input_filename = "../data/COMP90086_2021_Project_test/imagenames.csv"
    output_filename = "query_list_with_intrinsics.txt"

    with open(input_filename, newline='') as infile, open(output_filename, 'w') as outfile:
        reader = csv.reader(infile, delimiter=',')
        # skip the headers
        next(reader, None)  
        for row in reader:
            filename = "test/" + row[0] + ".jpg"
            output_line = filename + CAMERA_PARAMETERS
            outfile.write(output_line + '\n')


# TODO: Match top-20 pairs based on image coordinates
def generate_pairs_db_covis_file():

    # based on https://raw.githubusercontent.com/cvg/Hierarchical-Localization/master/pairs/aachen_v1.1/pairs-db-covis20.txt

    input_filename = "../data/COMP90086_2021_Project_train/train.csv"
    output_filename = "pairs-manual-db-covis5.txt"

    with open(input_filename, newline='') as infile, open(output_filename, 'w') as outfile:
        reader = csv.reader(infile, delimiter=',')
        # skip the headers
        next(reader, None)  

        for row in reader:
            #left_file_name = "train/" + row[0] + ".jpg"
            left_file_name = row[0] + ".jpg"

            # Remove last chars
            first_file_name = row[0][:-1]

            # Get last chars
            file_number = row[0][-1:]         
            
            for i in range(1, 6):
                if str(i) != file_number:
                    #right_file_name = " train/" + first_file_name + str(i) + ".jpg"
                    right_file_name = " " + first_file_name + str(i) + ".jpg"
                    output_line = left_file_name + right_file_name
                    outfile.write(output_line + '\n')



generate_query_list_with_intrinsics_file()
generate_pairs_db_covis_file()
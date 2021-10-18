import pandas as pd
import numpy as np
import csv

with open("comp90086_best_matches.txt") as f:
    best_matches_indexes = [int(x) for x in f.read().split()]

train_df = pd.read_csv("./data/COMP90086_2021_Project_train/train.csv")

preds = []

# Get the coordinates of the best-match image in the training datase
for match_index in best_matches_indexes:
    x = train_df.iloc[match_index,1]
    y = train_df.iloc[match_index,2]
    pred = (x, y)
    preds.append(pred)


test_filenames = []

# read in the filenames of the test dataset
with open("./data/COMP90086_2021_Project_test/imagenames.csv", newline='') as inputfile:
    reader = csv.reader(inputfile)
    # skip header
    header = next(reader)
    
    for row in reader:
        test_filenames.append(str(row[0]))

# write submission file
with open("submission.csv","w",newline="") as csvfile:
    writer=csv.writer(csvfile)
    writer.writerow(["id","x","y"])
    index = 0
    for prediction in preds:
        writer.writerow([test_filenames[index], preds[index][0], preds[index][1]])
        index+=1
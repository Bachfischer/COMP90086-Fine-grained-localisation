# SuperGlue

This folder contains an image matching and inference script based on the pre-trained [SuperGlue](https://github.com/magicleap/SuperGluePretrainedNetwork) model. It works by exhaustively matching the test images with all train images and outputs the best match candidate for every image.

**Note:**
*To reproduce the results reported in the paper, please first download the pre-trained SuperGlue model from this [link](https://github.com/magicleap/SuperGluePretrainedNetwork) and place it into the `model/` directory.*

## Evaluation

| Experiment                                  | Filename                                              | Score    |
|---------------------------------------------|-------------------------------------------------------|----------|
| SuperGlue                                   | `submission_SuperGlue.csv`                            | 6.37266  |


## Instructions

**Perform image matching:**

To perform the image matching process, run the command below. It will output a list of indexes corresponding to the best match in the training dataset in a text file called `comp90086_best_matches.txt`. 
```
python comp90086_batch_process.py --train_images  ./data/COMP90086_2021_Project_train/train/ --test_images ./data/COMP90086_2021_Project_test/test --resize -1 --output_dir  dump_demo_sequence
```

**Perform inference:**

To run the inference step on the predicted matches and generate the submission file, execute the following script. It uses the `comp90086_best_matches.txt` file to look-up the coordinates of the best matches in the training dataset and use these coordinates for the test images.
```
python comp90086_inference.py
```

### Visualization:

To output some visualizations during debugging, run the following commands:
```
python match_pairs.py --input_pairs input_pairs.txt --input_dir ./data/COMP90086_2021_Project_train/train/ --viz --resize -1

python demo_superglue.py --input  ./data/COMP90086_2021_Project_train/train/ --resize -1 --output_dir  dump_demo_sequence
```


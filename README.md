# COMP90086-Fine-grained-localisation

## Evaluation

| Experiment                                  | Filename                                              | Score    |
|---------------------------------------------|-------------------------------------------------------|----------|
| CNN_baseline (5 epochs)                     | `submission_CNN_baseline_5_epochs`                    | 52.35375 |
| CNN_baseline (25 epochs)                    | `submission_CNN_baseline_5_epochs`                    | 52.44292 |
| ImageSimilarity w/ Rescale (10 epochs)      | `submission_ImageSimilarity_w_Rescale_10_epochs.csv`  | 61.58458 |
| ImageSimilarity w/ Crop (20 epochs)         | `submission_ImageSimilarity_w_Crop_20_epochs.csv`     | 62.23774 |




## General setup instructions

pip install kaggle
mkdir .kaggle
chmod 600 ~/.kaggle/kaggle.json


### Download data
mkdir Hierarchical-Localization/datasets/COMP90086
cd Hierarchical-Localization/datasets/COMP90086
kaggle competitions download -c comp90086-2021
unzip comp90086-2021.zip
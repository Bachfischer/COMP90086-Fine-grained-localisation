# COMP90086-Fine-grained-localisation

This repository contains the source code for the *[Fine-grained localisation](https://www.kaggle.com/c/comp90086-2021/overview)* Project that was part of the COMP90086 Computer Vision course at the University of Melbourne.

## Project structure

* `data/` -- Raw datasets published by COMP90086 competition organizers
* `doc/` -- Documentation and project report (LaTeX source)
* `src/` -- Source code used in Kaggle competition task
    * `00_Experiments/` -- Folder containing various notebooks with explorative experiments and data analysis
    * `01_CNN_baseline/` -- Notebook with implementation of CNN model (Tensorflow) to predict image coordinates based on a classification setting
    * `02_SIFT/` -- Notebook with implementation of SIFT feature matching
    * `03_Hierachical-Localization/` -- Notebook based on [Hierachical-Localization](https://github.com/cvg/Hierarchical-Localization) model to perform 3D reconstruction of scene (not finished)
    * `04_Image-Similarity-Autoencoder/` -- Notebook with Autoencoder implementation (PyTorch) to match test images with train images based on feature embeddings
    * `05_SuperGlue/`-- Image processing script based on pre-trained [SuperGlue](https://github.com/magicleap/SuperGluePretrainedNetwork) model to match test images with train images
* `submissions/` -- Submissions to the COMP90086 Kaggle competition ([Link to competition](https://www.kaggle.com/c/comp90086-2021/overview))


For further information, please refer to the project report attached to this submission.


## Evaluation

Below is an overview of the scores for our different models as reported on the public Kaggle leaderboard:

| Experiment                                  | Filename                                              | Score    |
|---------------------------------------------|-------------------------------------------------------|----------|
| CNN_baseline (5 epochs)                     | `submission_CNN_baseline_5_epochs`                    | 52.35375 |
| CNN_baseline (25 epochs)                    | `submission_CNN_baseline_5_epochs`                    | 52.44292 |
| ImageSimilarity w/ Rescale (10 epochs)      | `submission_ImageSimilarity_w_Rescale_10_epochs.csv`  | 61.58458 |
| ImageSimilarity w/ Crop (20 epochs)         | `submission_ImageSimilarity_w_Crop_20_epochs.csv`     | 62.23774 |
| SuperGlue                                   | `submission_SuperGlue.csv`                            | 6.37266  |


## General setup instructions

Run the following commands to download the dataset that was part of the COMP90086 Kaggle competition (create `kaggle.json` by clicking on 'Create New API Token' on Kaggle website):

### Configure Kaggle client

```
pip install kaggle
mkdir .kaggle
chmod 600 ~/.kaggle/kaggle.json
```

### Download the dataset

```
mkdir Hierarchical-Localization/datasets/COMP90086
cd Hierarchical-Localization/datasets/COMP90086
kaggle competitions download -c comp90086-2021
unzip comp90086-2021.zip
```
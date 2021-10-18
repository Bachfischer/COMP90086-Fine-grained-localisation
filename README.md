# COMP90086-Fine-grained-localisation

## Connect via SSH

https://cloud.google.com/vertex-ai/docs/workbench/user-managed/ssh-access

JupyterLab:
gcloud compute ssh --project fastai-playground-2020 --zone us-west1-b computer-vision-project -- -L 8080:localhost:8080

pixloc Viewer:
gcloud compute ssh --project fastai-playground-2020 --zone us-west1-b computer-vision-project -- -L 8000:localhost:8000


pip install kaggle
mkdir .kaggle
chmod 600 ~/.kaggle/kaggle.json


### Download data
mkdir Hierarchical-Localization/datasets/COMP90086
cd Hierarchical-Localization/datasets/COMP90086
kaggle competitions download -c comp90086-2021
unzip comp90086-2021.zip

### Prepare folder structure
mkdir images
mkdir images/train
mkdir images/test

cp COMP90086_2021_Project_train/train/* images/train/
cp COMP90086_2021_Project_test/test/* images/test/

## hloc

git clone --recursive https://github.com/cvg/Hierarchical-Localization/
cd Hierarchical-Localization/
python -m pip install -e .

sudo apt-get install colmap
pip install pycolmap


### Inspect embedding files

import h5py

hfile = h5py.File('feats-superpoint-n4096-r1024_matches-superglue_pairs-manual-db-covis5.h5', 'r')
hfile = h5py.File('feats-superpoint-n4096-r1024.h5', 'r')


### Reconstruction

Geometric verification

colmap matches_importer --database_path outputs/COMP90086/sfm_superpoint+superglue/database.db --match_list_path outputs/COMP90086/pairs-manual-db-covis5.txt --match_type pairs --SiftMatching.max_num_trials 20000 --SiftMatching.min_inlier_ratio 0.1 --SiftMatching.use_gpu 0

colmap mapper --database_path outputs/COMP90086/sfm_superpoint+superglue/database.db --image_path datasets/COMP90086/images/train --output_path outputs/COMP90086/sfm_superpoint+superglue/models --Mapper.num_threads 16


```
Bundle adjustment report
------------------------
    Residuals : 160
   Parameters : 129
   Iterations : 101
         Time : 0.210723 [s]
 Initial cost : 3.62448 [px]
   Final cost : 0.431795 [px]
  Termination : No convergence

  => Filtered observations: 8
  => Filtered images: 0

Elapsed time: 4.034 [minutes]
```


## Triangulation (optional)

colmap point_triangulator --database_path outputs/COMP90086/sfm_superpoint+superglue/database.db --image_path datasets/COMP90086/images/train --input_path outputs/COMP90086/

--match_list_path outputs/COMP90086/pairs-manual-db-covis5.txt --match_type pairs --SiftMatching.max_num_trials 20000 --SiftMatching.min_inlier_ratio 0.1 --SiftMatching.use_gpu 0


## pixloc

git clone https://github.com/cvg/pixloc/
cd pixloc/
pip install -e .[extra]

python -m pixloc.download Aachen
python -m pixloc.download --select checkpoints 

python -m pixloc.run_Aachen






sudo apt-get install python3-opencv
sudo apt-get install libgl1-mesa-dev
sudo apt-get install libxss-dev
sudo apt-get install libasound2-dev
sudo apt-get install ffmpeg libsm6 libxext6
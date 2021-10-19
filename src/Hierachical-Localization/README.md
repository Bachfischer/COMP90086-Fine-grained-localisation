# Hierachical-Localization

## Preparation

### Prepare folder structure

```
mkdir images
mkdir images/train
mkdir images/test
```

```
cp COMP90086_2021_Project_train/train/* images/train/
cp COMP90086_2021_Project_test/test/* images/test/
```

### Install required dependencies

```
git clone --recursive https://github.com/cvg/Hierarchical-Localization/
cd Hierarchical-Localization/
python -m pip install -e .
```

```
sudo apt-get install colmap
pip install pycolmap
```

## Feature extraction and feature matching

Please refer to the notebook `pipeline_COMP90086.ipynb` for further details on the feature extraction and feature matching part.

### Inspect embedding files

Run the following commands to inspect the embedding files.

```
import h5py
hfile = h5py.File('feats-superpoint-n4096-r1024_matches-superglue_pairs-manual-db-covis5.h5', 'r')
hfile = h5py.File('feats-superpoint-n4096-r1024.h5', 'r')
```

## 3D-Reconstruction

Run the following commands to perform 3D reconstruction based on the extracted features and matches:

```
colmap matches_importer --database_path outputs/COMP90086/sfm_superpoint+superglue/database.db --match_list_path outputs/COMP90086/pairs-manual-db-covis5.txt --match_type pairs --SiftMatching.max_num_trials 20000 --SiftMatching.min_inlier_ratio 0.1 --SiftMatching.use_gpu 0

colmap mapper --database_path outputs/COMP90086/sfm_superpoint+superglue/database.db --image_path datasets/COMP90086/images/train --output_path outputs/COMP90086/sfm_superpoint+superglue/models --Mapper.num_threads 16
```

The output from the 3D reconstruction step looks as follows. Unfortunately the 3D reconstruction attempt was not successful (no convergence).

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


### Run Triangulation (optional)

```
colmap point_triangulator --database_path outputs/COMP90086/sfm_superpoint+superglue/database.db --image_path datasets/COMP90086/images/train --input_path outputs/COMP90086/
--match_list_path outputs/COMP90086/pairs-manual-db-covis5.txt --match_type pairs --SiftMatching.max_num_trials 20000 --SiftMatching.min_inlier_ratio 0.1 --SiftMatching.use_gpu 0
```
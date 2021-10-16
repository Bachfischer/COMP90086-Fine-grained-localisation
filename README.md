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
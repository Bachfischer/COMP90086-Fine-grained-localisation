# COMP90086-Fine-grained-localisation

## Connect via SSH

https://cloud.google.com/vertex-ai/docs/workbench/user-managed/ssh-access

JupyterLab:
gcloud compute ssh --project fastai-playground-2020 --zone us-west1-b computer-vision-project -- -L 8080:localhost:8080

pixloc Viewer:
gcloud compute ssh --project fastai-playground-2020 --zone us-west1-b computer-vision-project -- -L 8000:localhost:8000


## pixloc

git clone https://github.com/cvg/pixloc/
cd pixloc/
pip install -e .[extra]

python -m pixloc.download Aachen
python -m pixloc.download --select checkpoints 

python -m pixloc.run_Aachen

## hloc

git clone --recursive https://github.com/cvg/Hierarchical-Localization/
cd Hierarchical-Localization/
python -m pip install -e .

(optional: pip install pycolmap)

sudo apt-get install python3-opencv
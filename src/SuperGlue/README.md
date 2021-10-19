# SuperGlue

Visualization:

python match_pairs.py --input_pairs input_pairs.txt --input_dir ./data/COMP90086_2021_Project_train/train/ --viz --resize -1


python demo_superglue.py --input  ./data/COMP90086_2021_Project_train/train/ --resize -1 --output_dir  dump_demo_sequence


python comp90086_batch_process.py --train_images  ./data/COMP90086_2021_Project_train/train/ --test_images ./data/COMP90086_2021_Project_test/test --resize -1 --output_dir  dump_demo_sequence
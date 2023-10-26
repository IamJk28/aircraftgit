
#This script sorts each image file and corresponding xml file into a test/train partition based on a random seed

import os
import random
from sklearn.model_selection import train_test_split
from shutil import copyfile

# Set the paths to your image and XML directories 
image_directory ='Tensorflow/workspace/images/collectedimages'
xml_directory ='Tensorflow/workspaces/images/collectedimages'

# Create the train and test directories if they don't exist
train_directory = 'Tensorflow/workspace/images/train'
test_directory = 'Tensorflow/workspace/images/test'
os.makedirs(train_directory, exist_ok=True)
os.makedirs(test_directory, exist_ok=True)

# List all image files in the image directory
image_files = [file for file in os.listdir(image_directory) if file.endswith('.jpg')]

# Set the random seed so as to ensure reproducibility
random_seed = 42

# Perform the train/test split
train_files, test_files = train_test_split(image_files, test_size=0.2, random_state=random_seed)

# Move the selected images and their corresponding XML files to the train folder
for file in train_files:
    image_start = os.path.join(image_directory, file)
    xml_start = os.path.join(xml_directory, file.replace('.jpg', '.xml'))
    image_dest = os.path.join(train_directory, file)
    xml_dest = os.path.join(train_directory, file.replace('.jpg', '.xml'))
    copyfile(image_start, image_dest)
    copyfile(xml_start, xml_dest)

# Move the remaining images and their corresponding XML files to the test folder
for file in test_files:
    image_start = os.path.join(image_directory, file)
    xml_start = os.path.join(xml_directory, file.replace('.jpg', '.xml'))
    image_dest = os.path.join(test_directory, file)
    xml_dest = os.path.join(test_directory, file.replace('.jpg', '.xml'))
    copyfile(image_start, image_dest)
    copyfile(xml_start, xml_dest)

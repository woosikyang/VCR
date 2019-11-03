import os
USE_IMAGENET_PRETRAINED = True # otherwise use detectron, but that doesnt seem to work?!?


VCR_dir = '/media/woosik/4A2661AA26619829/Users/All Users/VCR_Data'


VCR_IMAGES_DIR = os.path.join(VCR_dir, 'vcr1images')
VCR_ANNOTS_DIR = VCR_dir

# Change these to match where your annotations and images are
#VCR_IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'data', 'vcr1images')
#VCR_ANNOTS_DIR = os.path.join(os.path.dirname(__file__), 'data')

if not os.path.exists(VCR_IMAGES_DIR):
    raise ValueError("Update config.py with where you saved VCR images to.")
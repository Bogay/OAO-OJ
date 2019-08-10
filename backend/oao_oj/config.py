import os

# /path/to/backend
BASE_PATH = os.getcwd()


# ##
# Absolute Path for Files

TMP_DIR = f'{BASE_PATH}/tmp'
PROB_DIR = f'{BASE_PATH}/data/prob'


# ##
# Relative Path for Files

# PROB_DIR/<pid>/TEST_DIR
TEST_DIR = '/testdatas'


# ##
# Path for DB

PROB_COL = 'problems'

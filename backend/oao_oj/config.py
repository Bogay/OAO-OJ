import os
import pymongo

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

# ##
# Const for Mongo

MONGO_CLIENT = pymongo.MongoClient('mongodb://localhost:27017/')
OJ_DB = MONGO_CLIENT['OAO-OJ']

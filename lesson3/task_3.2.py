import importlib
import sys

import argparse
import logging

ERROR_MESSAGE = 'Package not found'
no_version_message = 'No version defined'

parser = argparse.ArgumentParser()
parser.add_argument('-log', '--log_level', default='debug', help='For example run - python task_3.2.py -log info')
args = parser.parse_args()
levels = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR
}
level = levels.get(args.log_level.lower())

logging.basicConfig(level=level, filename='ERROR.log', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()

ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


def get_package_path(lib_name):
    try:
        type(importlib.import_module(lib_name))
        logger.warning(f'{logging.warning(sys.modules[lib_name].__doc__)}')
        logger.info(f'{logging.info(sys.modules[lib_name].__file__)}')
        try:
            logger.debug(f'Package version is - {logging.debug(sys.modules[lib_name].__version__)}')
        except AttributeError:
            logger.debug(f'{logging.debug(no_version_message)}')
            return print(f"Path to lib {lib_name} is : {sys.modules[lib_name].__file__}")

    except ModuleNotFoundError:
        print('Package not found')
        logger.error(f'{logging.error(ERROR_MESSAGE)}')


print((get_package_path("prettytable")))

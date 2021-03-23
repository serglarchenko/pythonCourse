import importlib
import sys

import argparse
import logging

ERROR_MESSAGE = 'Package not found'
no_version_message = 'No version defined'

parser = argparse.ArgumentParser()
parser.add_argument('--console_log', default='debug', type=str)
parser.add_argument('--file_log', default='debug', type=str)

args = parser.parse_args()

logger = logging.getLogger(__name__)
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler('file_logs.log')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

if args.console_log:
    console_handler.setLevel(args.console_log.upper())
if args.file_log:
    file_handler.setLevel(args.file_log.upper())
logger.addHandler(console_handler)
logger.addHandler(file_handler)


def get_package_path(lib_name):
    try:
        importlib.import_module(lib_name)
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


if __name__ == '__main__':
    if args.console_log:
        console_handler.setLevel('WARN')
    if args.file_log:
        file_handler.setLevel('INFO')

print((get_package_path("prettytable")))

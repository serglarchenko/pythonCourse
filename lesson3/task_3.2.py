import importlib
import sys

import argparse
import logging

ERROR_MESSAGE = 'Package not found'
no_version_message = 'No version defined'

# parser = argparse.ArgumentParser(description='Parser')
# parser.add_argument('-d', '-DEBUG', action='store_const', dest='loglevel', const=logging.DEBUG, default=logging.DEBUG, help='debug level')
# parser.add_argument('--w', '--WARNING', action='store_const', dest='loglevel', const=logging.WARNING, help='warning level')
# parser.add_argument('--i', '--INFO', action='store_const', dest='loglevel', const=logging.INFO, help='info level')
#
logging.basicConfig(level=logging.DEBUG, filename='ERROR.log', format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)


# parser = argparse.ArgumentParser()
# parser.add_argument(
#     '-d', '--debug',
#     action="store_const", dest="loglevel", const=logging.DEBUG,
#     default=logging.DEBUG,
# )
#
# args = parser.parse_args()
# logging.basicConfig(level=args.loglevel)

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

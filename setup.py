from setuptools import setup

# python setup.py sdist
# pip install my_python_project-1.0.tar.gz
# pip install .
# pip uninstall my_python_project

setup(
    name='my_python_project',
    version='1.0',
    author='Serhii Larchenko',
    packages=['lesson1', 'lesson2'],
    description='Creation own setup file',
    package_data={'': ['*.txt']},
    entry_points={'console_scripts': ['lessons = lesson2.foobar:main']},
)

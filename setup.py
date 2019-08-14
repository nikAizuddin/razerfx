# -*- coding: utf-8 -*-
from os import path
from setuptools import setup, find_packages

def get_version():
    versionfile = path.join(path.dirname(path.abspath(__file__)), 'VERSION.txt')
    with open(versionfile) as f:
        version = f.read().strip()
    return version

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

def setup_package():
    setup(
        name='razerfx',
        version=get_version(),
        description='OpenRazer client to set advanced effect on Razer BlackWidow 2019 (en_US)',
        author='Nik Mohamad Aizuddin bin Nik Azmi',
        author_email='nik-mohamad-aizuddin@yandex.com',
        maintainer='Nik Mohamad Aizuddin bin Nik Azmi',
        maintainer_email='nik-mohamad-aizuddin@yandex.com',
        url='https://github.com/nikAizuddin/razerfx.git',
        packages=find_packages(),
        install_requires=requirements,
        entry_points={
            'console_scripts': ['razerfx=main:main'],
        },
    )

def write_version_py():
    pyfile = path.join('razerfx', 'version.py')

    content = "# THIS FILE IS GENERATED FROM RAZERFX\n"
    content += "version = '{version}'\n"

    with open(pyfile, 'w') as f:
        f.write(content.format(version=get_version()))

if __name__ == '__main__':
    setup_package()
    write_version_py()

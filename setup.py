#!/usr/bin/env python3

from distutils.core import setup
import os

version_txt_path = os.path.join(
    os.path.dirname(__file__),
    'playground',
    'version.txt'
)
with open(version_txt_path, 'r') as version_file:
    pyqms_version = version_file.readline().strip()

setup(
    name             = 'playground',
    version          = pyqms_version,
    packages         = [ 'playground' ],
    package_dir      = { 'playground' : 'playground' },
    description      = 'playground ',
    package_data     = {
        'playground' : [
            'version.txt',
        ]
    },
    requires         = [],
    long_description = "",
    author           = '',
    author_email     = '',
    url              = '',
    license          = 'The MIT License (MIT)',
    platforms        = '',
    classifiers      = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Developers',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: SunOS/Solaris',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Atmospheric Science',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Topic :: Scientific/Engineering :: Chemistry',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Physics',
    ],
)

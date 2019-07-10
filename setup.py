import pathlib
import sys

import setuptools

__author__ = 'Tomasz Trębski'
__author_email__ = 'kornicameister@gmail.com'

if sys.version_info < (3, 7):
    raise RuntimeError('asyncpg-migrate requires Python 3.7  or greater')

setuptools.setup(
    name='asyncpg-migrate',
    setup_requires='setupmeta',
    # setupmeta options
    versioning='distance',
)

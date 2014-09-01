import os
from distutils.core import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = 'deep',
    version = '1.1.2',
    author = 'Mark R. Gollnick',
    author_email = 'mark.r.gollnick@gmail.com',
    description = ('Determine the maximum depth and path length within '
                   'the current (or a specified) directory tree.'),

    license = 'LICENSE.txt',
    keywords = 'deep directory structure depth file name path length',
    url = 'https://github.com/markgollnick/deep',
    packages = ['deep'],
    long_description=read('README.md'),
)

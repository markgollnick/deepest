"""Deep PyPI Package."""

import os
from distutils.core import setup


def read(filename):
    """Read file contents."""
    f = open(os.path.join(os.path.dirname(__file__), filename))
    contents = f.read()
    f.close()
    return contents


def get_version():
    """Return latest version noted in changefile."""
    lastline = [line for line in read('CHANGES.txt').split('\n') if line][-1]
    version = lastline.split(',')[0]
    return version[1:]


setup_args = dict(
    name='deep',
    version=get_version(),
    description=('Determine the maximum depth and path length within '
                 'the current (or a specified) directory tree.'),
    long_description=read('README.md'),
    author='Mark R. Gollnick &#10013;',
    author_email='mark.r.gollnick@gmail.com',
    url='https://github.com/markgollnick/deep',
    license='LICENSE.txt',
    keywords='deep directory structure depth file name path length',
    packages=['deep'],
)


if __name__ == '__main__':
    setup(**setup_args)

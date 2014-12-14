"""PyPI Package descriptor file."""

import os
from distutils.core import setup


def get_version(change_log):
    """Return the latest version as noted in a change log."""
    lastline = [ln.strip() for ln in read(change_log).split('\n') if ln][-1]
    version = lastline.split(',')[0]
    return version[1:]


def read(file_name):
    """Read file contents."""
    f = None
    data = ''
    try:
        f = open(file_name, 'rb')
        data = f.read().decode('utf-8')
    except:
        pass
    finally:
        if f:
            f.close()
        return data


setup_args = dict(
    name='deepest',
    version=get_version('CHANGES.txt'),
    description=('Determine the maximum depth and path length within '
                 'the current (or a specified) directory tree.'),
    long_description=read('README.md'),
    author='Mark R. Gollnick &#10013;',
    author_email='mark.r.gollnick@gmail.com',
    url='https://github.com/markgollnick/deepest',
    license='LICENSE.txt',
    keywords='deepest directory structure depth file name path length',
    packages=['deepest'],
    scripts=[os.path.join('scripts', 'deepest')]
)


if __name__ == '__main__':
    setup(**setup_args)

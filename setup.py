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


author_string = 'Mark R. Gollnick &#10013; <mark.r.gollnick@gmail.com>'
author, author_email = author_string.rsplit(' ', 1)

setup_args = {
    'name': 'deepest',
    'version': get_version('CHANGES.txt'),
    'author': author,
    'author_email': author_email,
    'maintainer': author,
    'maintainer_email': author_email,
    'url': 'https://github.com/markgollnick/deepest',
    'license': read('LICENSE.txt'),
    'description': (
        'Determine the maximum depth and path length within the current (or a '
        'specified) directory tree.'
    ),
    'long_description': read('README.rst'),
    'keywords': (
        'deep, deeper, deepest, directory, folder, structure, depth, file, '
        'name, filename, path, length'
    ),
    # 'platforms': None,
    # 'download_url': None,
    # 'requires': None,
    # 'provides': None,
    # 'obsoletes': None,
    # 'classifiers': None,
    'packages': ['deepest'],
    'scripts': [os.path.join('scripts', 'deepest')]
}


if __name__ == '__main__':
    setup(**setup_args)

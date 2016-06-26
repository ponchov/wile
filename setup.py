import os
from setuptools import setup

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name = "wile",
    version = "0.1",
    author = "Leo Antunes",
    author_email = "leo@costela.net",
    description = ("A stripped down Let's Encrypt (ACME) client"),
    license = "GPLv3",
    keywords = "letsencrypt acme ssl",
    url = "https://github.com/costela/wile",
    py_modules = ['wile'],
    install_requires = [
        'acme>=0.6',
        'click=>6.0',
        'pyOpenSSL',
        'cryptography',
    ],
    entry_points={
        'console_scripts': [
            'wile = wile:main',
        ],
    },
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
)

from setuptools import setup, find_packages

import discogs_wantlist

setup(
    name='discogs_wantlist',
    version=discogs_wantlist.__version__,
    packages=find_packages(),
    long_description=open('README.md').read(),
    url='http://github.com/waxisien/discogs-wantlist',
    install_requires=[
        'certifi==2017.7.27.1',
        'chardet==3.0.4',
        'discogs-client==2.2.1',
        'idna==2.6',
        'oauthlib==2.0.4',
        'requests==2.18.4',
        'six==1.11.0',
        'urllib3==1.24.2',
    ],
)

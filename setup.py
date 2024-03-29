#!/usr/bin/env python

import setuptools

pkg_info = {}
with open("NanoSSO/__version__.py", "r", encoding="utf-8") as f:
    for l in f.readlines():
        data = l.split('=')
        pkg_info[data[0].strip()] = (data[1].replace("'", "")).strip()

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(name=pkg_info['__title__'],
                 version=pkg_info['__version__'],
                 description=pkg_info['__description__'],
                 license=pkg_info['__license__'],
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 author_email=pkg_info['__author_email__'],
                 url=pkg_info['__url__'],
                 project_urls={
                     'Documentation': 'https://NanoSSO.nullsec.space',
                     'Source': pkg_info['__url__'],
                     'Tracker': 'https://github.com/NullsecSpace/NanoSSO/issues',
                 },
                 packages=setuptools.find_packages(include=["NanoSSO", "NanoSSO.*"]),
                 install_requires=[
                     'pytest~=7.2.0'
                 ],
                 python_requires=">=3.7",
                 entry_points={
                     'console_scripts': [
                         'nano-sso = NanoSSO:main'
                     ]
                 },
                 classifiers=[
                     'Development Status :: 2 - Pre-Alpha',
                     'Programming Language :: Python :: 3.10',
                     'Topic :: Games/Entertainment',
                     'License :: OSI Approved :: MIT License',
                 ],
                 keywords='eve online sso esi oauth2'
                 )

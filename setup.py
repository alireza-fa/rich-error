#!/usr/bin/env python3
from io import open

from setuptools import find_packages, setup


def read(f):
    with open(f, 'r', encoding='utf-8') as file:
        return file.read()


setup(
    name='rich_error',
    version="0.0.2",
    url='https://github.com/alireza-fa/rich-error',
    license='MIT',
    description='Implementation of rich error in Python.',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Alireza Feizi',
    author_email='alirezafeyze44@gmail.com',
    packages=find_packages(exclude=['tests*', 'docs*', 'examples*', 'note.txt']),
    include_package_data=True,
    python_requires=">=3.10",
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Internet :: WWW/HTTP',
    ],
    project_urls={
        'Source': 'https://github.com/alireza-fa/rich-error',
    },
)

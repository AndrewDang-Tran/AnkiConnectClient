from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(
    name='anki-helpers',
    version='0.1.0',
    author='Andrew Dang-Tran',
    author_email='andrewdt1506@gmail.com',
    description='A python library for interacting with anki currently only supports AnkiConnect.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/AndrewDang-Tran/AnkiHelpers',
    packages=[
        'anki_helpers',
        'anki_helpers.models',
    ],
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.9',
)

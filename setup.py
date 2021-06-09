import os

from setuptools import find_packages, setup

_HERE = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(_HERE, 'README.md'), 'r') as f:
    long_desc = f.read()

setup(
    name='sfreeze',
    use_scm_version=True,
    description='A python tool for freezing objects in AWS S3',
    long_description=long_desc,
    long_description_content_type='text/markdown',

    url='https://github.com/Jlrine2/sfreeze',

    license='BSD',
    include_package_data=True,

    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],

    python_requires='~=3.8',

    install_requires=[
        'boto3',
    ],

    extras_require={},

    packages=find_packages(),

    zip_safe=False,
)
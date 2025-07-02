from setuptools import setup, find_packages

setup(
    name='timeseries-prep',
    version='0.1.0',
    description='Time Series Preprocessing Utilities',
    author='Shashwat dev Hans',
    author_email='Shashwatdevhans@gmail.com',
    url='https://github.com/ShashwatDev-26/timeseries-prep.git',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.6',
)

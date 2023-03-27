from setuptools import setup, find_packages
from version import __version__
classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Intended Audience :: Science/Research',
    'Topic :: Scientific/Engineering :: Chemistry',
    'Operating System :: OS Independent' ,
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10'
]


setup(
    name='science',
    version=__version__,
    description='Use the properties of thermomechanics and set up simple chemical reactions',
    long_description=open('README.md').read(),
    url='https://github.com/MASTAR-LAST/Science',
    author='Mohammed Al_kohawaldeh',
    author_email='belalalkohawaldeh@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['science', 'atom', 'atoms', 'scientific', 'thermomechanics', 'atomic', 'chemicals'],
    packages=find_packages(where='src'),
    requires=['decimal', 'numpy', 'scipy']
)

if __name__ == '__main__':
    setup()
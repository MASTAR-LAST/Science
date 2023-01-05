from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/non-stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10 :: Linux :: Mac OS' ,
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10'
]

exec(open('version.py').read())
setup(
    name='science',
    version=__version__,
    description='Use the properties of thermomechanics and set up simple chemical reactions',
    long_description=open('README.md').read(),# الملف المذكور لم ينتهي بعد ...
    url='',
    author='Mohammed Al_kohawaldeh',
    author_email='belalalkohawaldeh@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['science', 'atom', 'atoms', 'scientific', 'thermomechanics', 'atomic', 'chemicals'],
    packages=find_packages(),
    requires=['decimal', '']# اكتب كل المكاتب الي استخدمتها في مكتبتك
)
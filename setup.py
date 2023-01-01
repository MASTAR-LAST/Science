from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/non-stable',
    'Intended Audience :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10 :: Linux :: Mac OS' ,
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10'
]

setup(
    name='science',
    version='0.1.0',
    description='A scientific package full of functions that help to do experiments and test the properties of atoms under some conditions',
    long_description=open('README.txt').read(),# الملف المذكور لم ينتهي بعد ...
    url='',
    author='Mohammed Al_kohawaldeh',
    author_email='belalalkohawaldeh@gmail.com',
    license='MIT',
    classifiers=classifiers,
    keywords=['science', 'atom', 'atoms', 'scientific', ''],
    packages=find_packages(),
    requires=['decimal', '']# اكتب كل المكاتب الي استخدمتها في مكتبتك
)
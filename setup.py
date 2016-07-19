from setuptools import find_packages
from distutils.core import setup


VERSION = '0.1'

setup(
    name='django-herald',
    version=VERSION,
    author='Worthwhile',
    author_email='devs@worthwhile.com',
    install_requires=['django>=1.8', 'six'],
    packages=find_packages(),
    include_package_data=True,  # declarations in MANIFEST.in
    license='LICENSE',
    url='https://github.com/worthwhile/django-herald/',
    download_url='https://github.com/worthwhile/django-herald/tarball/'+VERSION,
    description="Django library for separating the message content from transmission method",
    long_description=open('README.md').read(),
    keywords=['django', 'notifications', 'messaging'],
)

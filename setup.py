from setuptools import setup, find_packages

setup(
    name='django-herald',
    version='0.1b1',
    author='Worthwhile',
    author_email='devs@worthwhile.com',
    packages=find_packages(),
    include_package_data=True,  # declarations in MANIFEST.in
    license='LICENSE',
    description="Django library for separating the message content from transmission method",
    long_description=open('README.md').read(),
)

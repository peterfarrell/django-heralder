from setuptools import find_packages, setup


VERSION = '0.1.1'

setup(
    name='django-herald',
    version=VERSION,
    author='Worthwhile',
    author_email='devs@worthwhile.com',
    install_requires=['django>=1.8', 'six'],
    packages=find_packages(),
    include_package_data=True,  # declarations in MANIFEST.in
    license='MIT',
    url='https://github.com/worthwhile/django-herald/',
    download_url='https://github.com/worthwhile/django-herald/tarball/'+VERSION,
    description="Django library for separating the message content from transmission method",
    long_description=open('README.md').read(),
    keywords=['django', 'notifications', 'messaging'],
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
)

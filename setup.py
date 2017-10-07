from setuptools import setup
import os

setup(
    name='puttykeys',
    version='1.0.2',
    description='Library to convert Putty private keys to OpenSSH format',
    author='Matt Weeks',
    author_email='scriptjunkie@scriptjunkie.us',
    license='MIT',
    url='https://github.com/scriptjunkie/puttykeys.git',
    packages=['puttykeys'],
    install_requires=['cryptography'],
    platforms = ["POSIX", "Windows"],
    provides = ["puttykeys"],
    keywords='putty development',
    long_description = open(os.path.join(os.path.dirname(__file__), "README.rst"), "r").read(),
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License'
    ]
)

import os
from setuptools import setup

# Utility function to read the README file
# Easier than line wrapping a long string...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "autologin",
    version = "0.0.1",
    author = "Alejandro Caceres, Luke Maxwell",
    author_email = "lukemaxwellshouse@gmail.com",
    description = ("A utility for finding login links, forms and autologging "
                     "into websites with a set of valid credentials."),
    license = "BSD",
    keywords = "login, automated, spider",
    url = "https://github.com/TeamHG-Memex/autologin",
    packages=['autologin'],
    include_package_data = True,
    install_requires = [
        'six',
        'lxml',
    ],
    scripts = [
        'bin/autologin-server',
        'bin/autologin-http-api',
        'bin/autologin',
    ],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Web scraping, Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)

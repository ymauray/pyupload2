import setuptools

from distutils.core import setup

setup(name = "pyupload",
      version="0.1pre1",
      author="Yannick Mauray",
      author_email="yannick@frenchguy.ch",
      description="A tool to help upload files to auphonic and archive.org",
      packages = setuptools.find_packages(),
      python_requires = '>=3.6',
      scripts = ['bin/pyupload']
)

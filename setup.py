from setuptools import setup

setup(
   name='testpipenvproject',
   version='1.0',
   description='just try to make pipenv work',
   author='ME!',
   author_email='ME!@foo.com',
   packages=['testpipenvproject'],  #same as name
   install_requires=['pandas'], #external packages as dependencies
)
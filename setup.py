# coding=utf-8

from setuptools import setup, find_packages

setup(name="flask_scenegen",
      version="0.1.0",
      options={},
      description="A Flask scenegen for HA.",
      author="carlba",
      packages=find_packages(),
      install_requires=['click'],
      entry_points={
          'console_scripts': [
              'flask_scenegen = flask_scenegen.cli:main'
          ]
      }
      )

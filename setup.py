from setuptools import setup, find_packages

setup(name="oneflux",
      packages=find_packages(),
      install_requires=[
        'numpy>=1.11.0',
        'scipy>=0.17.0',
        'matplotlib>=1.5.1',
        'statsmodels>=0.8.0'
      ])

from setuptools import setup, find_packages


setup(
    name='short',
    version='0.0.1',
    license='MIT',
    author="Hero",
    packages=find_packages('source'),
    package_dir={'': 'source'},
    url='https://github.com/heromr/mini-url',
    keywords='shortener',
    install_requires=[
          'requests',
      ],

)

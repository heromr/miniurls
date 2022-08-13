from setuptools import setup, find_packages


setup(
    name='miniurl',
    version='0.0.1',
    license='MIT',
    author="Hero",
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/heromr/miniurl',
    keywords='shortener',
    install_requires=[
          'requests',
      ],

)

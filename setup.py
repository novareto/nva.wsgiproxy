from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='nva.wsgiproxy',
      version=version,
      description="",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Christian Klinger',
      author_email='ck@novareto.de',
      url='',
      license='GPL',
      namespace_packages=['nva'],
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'wsgiproxy',
          'setuptools',
      ],
      entry_points={
        'paste.filter_app_factory': [
            'unproxify = nva.wsgiproxy:unproxify',
         ],
      }
      )

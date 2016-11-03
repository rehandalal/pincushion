"""
Command line tool for generating random pin numbers.
"""
import os

from setuptools import find_packages, setup


DEPENDENCIES = [
    'click >= 6.6',
    'six >= 1.10.0',
]

ROOT = os.path.abspath(os.path.dirname(__file__))

version = __import__('pincushion').__version__


setup(
    name='pincushion',
    version=version,
    url='https://github.com/rehandalal/pincushion',
    license='Mozilla Public License Version 2.0',
    author='Rehan Dalal',
    author_email='rehan@meet-rehan.com',
    description='Command line tool for generating random pin numbers.',
    long_description=__doc__,
    packages=find_packages(exclude=['tests', 'docs']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=DEPENDENCIES,
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    py_modules=['pincushion'],
    entry_points={
        'console_scripts': [
            'pincushion = pincushion.cli:cli',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience'
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
    ]
)

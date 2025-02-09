from setuptools import setup

long_description = None

with open("README.md", 'r') as fp:
    long_description = fp.read()

setup(
    name = 'Vents_Breezy',
    packages = ['vents_breezy'],
    version='0.0.1',
    description='Python3 library for single-room energy recovery ventilators from Vents / Blauberg / Flexit / Vents',
    long_description=long_description,
    python_requires='>=3.6.7',
    author='borodamd',
    author_email='mail@example.com',
    url='https://github.com/borodamd/vents_breezy',
    license="MIT",
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Home Automation',
        'Topic :: Software Development :: Libraries :: Python Modules'
        ]
)

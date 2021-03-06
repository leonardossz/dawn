import setuptools

__copyright__ = 'Copyright 2020 See AUTHORS'
__license__ = 'See LICENSE'

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dawncli',
    version='0.0.1',
    url='https://github.com/leonardossz/mysql-dawn',
    author='See AUTHORS',
    author_email='leonardossz@gmail.com',
    maintainer_email='leonardossz@gmail.com',
    description='Unofficial AWS Aurora Serverless command line client.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['dawncli'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'boto3>=1.14, <1.15',
        'prompt_toolkit >=3.0, <4.0',
        'pygments >= 2.6, <3.0'
    ],
    entry_points={
        'console_scripts': [
            'dawncli = dawncli.client:main',
        ],
    }
)

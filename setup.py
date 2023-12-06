from setuptools import setup

setup(
    name='roid_search',
    version='1.0.0',
    author='Sascha Granberg',
    author_email='sascha.granberg@proton.me',
    description='Extracting text based on regex from any document type made simple',
    packages=['roid_search'],
    entry_points={
        'console_scripts': [
            'roid_search = roid_search.main:main'
        ]
    },
    install_requires=[
        'textract'
    ]
)
from setuptools import setup

with open('README.md') as f:
    long_descr = f.read().decode('utf-8')

setup(
    name = "enhance",
    packages = ["enhance"],
    entry_points = {
                "console_scripts": ['enhance = enhance.srcnn:main']
    },
    version = '1.0',
    description = "ENHANCE",
    long_description = long_descr,
    author = "Andrew Berger",
    author_email = "andbberger@gmail.co"
    )

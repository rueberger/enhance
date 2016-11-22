from setuptools import setup


setup(
    name = "enhance",
    packages = ["enhance"],
    entry_points = {
                "console_scripts": ['enhance = enhance.srcnn:main']
    },
    version = '1.2',
    description = "ENHANCE",
    long_description = """ command-line utility for enhancing images. seriously.

    See full readme at https://github.com/rueberger/enhance
    """,
    author = "Andrew Berger",
    author_email = "andbberger@gmail.co"
    )

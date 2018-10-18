import setuptools

with open("/Users/greg/Git/Github/pyjss/README.MD", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjss-test",
    version="1.1",
    author="Gregory Barillé",
    author_email="barille@gmail.com",
    description="A wrapper for Jamf Pro classic API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gregorybarille/pyjss",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
    ],
    install_requires=[
        'requests',
        'beautifulsoup4>=4.4.0',
        'lxml'
    ],

)

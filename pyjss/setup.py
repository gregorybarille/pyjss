import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyjss",
    version="1.0dev",
    author="Gregory Barillé",
    author_email="barille@gmail.com",
    description="A wrapper for Jamf Pro classic API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sillegue/pyjss",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status:: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: MacOS :: MacOS X",
    ],
)

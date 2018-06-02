import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="coin_falcon",
    version="0.0.1",
    author="Tony Rom",
    author_email="thetonyrom@gmail.com",
    description="Python package for the CoinFalcon API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/nick/folder",
    packages=setuptools.find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)
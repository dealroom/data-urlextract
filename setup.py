import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dealroom-urlextract",
    version="0.2.0",
    author="Dealroom.co",
    author_email="data@dealroom.co",
    description="Wrapper class for extracting only wanted parts from urls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dealroom/data-urlextract",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["tldextract>=5.0.0,<6.0.0"],
    python_requires=">=3.10",
)

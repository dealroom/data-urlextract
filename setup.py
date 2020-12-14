import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="urlextract",  # Replace with your own username
    version="0.0.1",
    author="Dealroom.co",
    author_email="data@dealroom.co",
    description="Wrapper class for extracting only wanted parts from urls.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dealroom/urlextract",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["tldextract"],
    python_requires=">=3.6",
)
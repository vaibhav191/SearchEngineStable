
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SearchEngineStable-pkg-VaibhavShri", # Replace with your own username
    version="0.0.1",
    author="Vaibhav",
    author_email="skychaser123@gmail.com",
    description="Search file using multi threading",
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
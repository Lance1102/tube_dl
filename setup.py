import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tube_dl",
    version="4.1.0",
    author="Shekhar Chander",
    author_email="shekhar1000.sc@gmail.com",
    description="Another Youtube Video Downloader for Python.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shekharchander/tube_dl",
    packages=setuptools.find_packages(),
    install_requires=["requests","js2py"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
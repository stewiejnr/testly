import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="testly",
    version="1.0.2",
    description="Perform SOAP and REST test",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/stewiejnr/testly",
    author="Stewartium, RPhipps",
    author_email="stewartium1@gmail.com,rhadjni@hotmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    packages=["testly"],
    include_package_data=True,
    install_requires=["requests", "zeep", "pyyaml"],
    entry_points={
        "console_scripts": [
            "testly-man=testly.__main__:main",
        ]
    },
)

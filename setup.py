from setuptools import setup, find_packages
from semversion import version

setup(
    name="dir-cli",
    version=version(),
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dir-cli=dir_cli.__main__:main",
        ],
    },
    install_requires=["click"],
    author="Gabriel Delgado",
    author_email="gadc1996@gmail.com",
    description="Pip module template",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/gadc1996/pip-module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

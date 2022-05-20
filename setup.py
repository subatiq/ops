from distutils.core import setup

from setuptools import find_packages

all_packages = find_packages()

setup(
    name="opservatory_cli",
    packages=all_packages,
    version="0.1.0",
    license="MIT",
    description="CLI for Opservatory server",
    author="Vladimir Semenov",
    author_email="subatiq@gmail.com",
    url="https://github.com/subatiq/ops",
    download_url="https://github.com/subatiq/ops/archive/refs/tags/0.1.0.tar.gz",
    keywords=["automation", "monitoring"],
    install_requires=[
        "requests",
        "pyyaml",
        "typer",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: System Administrators",
        "Topic :: System :: Systems Administration",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    entry_points={
        "console_scripts": [
            "ops=ops.__main__:run",
        ]
    },
)

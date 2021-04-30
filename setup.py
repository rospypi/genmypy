from setuptools import find_packages, setup

setup(
    name="genpyi",
    version="0.2.0",
    packages=find_packages(exclude=["tests"]),
    description="A Python stub generator from genmsg specs",
    long_description=open("README.rst").read(),
    author="Yuki Igarashi, Tamamki Nishino",
    author_email="me@bonprosoft.com, otamachan@gmail.com",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python",
    ],
    license="Apache License 2.0",
    url="https://github.com/rospypi/genpyi/",
    install_requires=[
        "genmsg",
        "genpy",
    ],
    extras_require={
        "dev": [
            # NOTE: pytest>=5.0 doesn't support py2
            "pytest>=4.6,<5.0",
            "typing; python_version=='2.7'",
        ],
        # NOTE: We don't support python2 for the lint environment
        "lint": [
            "black==20.8b1",
            "flake8-bugbear==21.4.3",
            "flake8==3.9.1",
            "isort==5.1.4",
            "mypy==0.790",
            "pysen>=0.9,<0.10",
        ],
    },
    package_data={"genpyi": ["py.typed"]},
    scripts=["scripts/genpyi"],
)

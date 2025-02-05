"""Package setup entrypoint."""
from typing import IO, Sequence
from setuptools import find_packages as __find_packages, setup as __compose_package
from uyaml import (
    __author__ as __author,
    __doc__ as __short_doc,
    __email__ as __email,
    __name__ as __name,
    __version__ as __version,
)
from uyaml.file import File


def __readme() -> str:
    """Returns project description."""
    with File("README.md") as readme:  # type: IO[str]
        return readme.read()


def __requirements() -> Sequence[str]:
    """Returns requirements sequence."""
    with File("requirements.txt") as requirements:  # type: IO[str]
        return tuple(map(str.strip, requirements.readlines()))


if __name__ == "__main__":
    __compose_package(
        name=__name,
        version=__version,
        author=__author,
        author_email=__email,
        description=__short_doc,
        long_description=__readme(),
        long_description_content_type="text/markdown",
        url="https://github.com/vyahello/uyaml",
        packages=__find_packages(exclude=("*.tests", "*.tests.*", "tests.*", "tests")),
        include_package_data=True,
        install_requires=__requirements(),
        classifiers=(
            "Programming Language :: Python :: 3.6",
            "Programming Language :: Python :: 3.7",
            "Programming Language :: Python :: 3.8",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
        ),
        python_requires=">=3.6",
    )

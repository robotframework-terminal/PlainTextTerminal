#  Copyright 2024-     Abhisit Sangjan
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import io
import os
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def read(*names, **kwargs):
    """Python 2 and Python 3 compatible text file reading.
    Required for single-sourcing the version string.
    """
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    """
    Search the file for a version string.
    file_path contain string path components.
    Reads the supplied Python module as text without importing it.
    """
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


setup(
    name="PlainTextTerminal",
    version=find_version("src/PlainTextTerminal", "__init__.py"),
    package_dir={"": "src"},
    packages=["PlainTextTerminal"],
    url="https://github.com/robotframework-terminal/PlainTextTerminal",
    author="Abhisit Sangjan",
    author_email="abhisit.sangjan@gmail.com",
    description="The Robot Framework Keywords for plain text terminal testing",
    license="Apache Software License",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Framework :: Robot Framework",
        "Framework :: Robot Framework :: Library",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Operating System :: MacOS",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX",
        "Operating System :: Unix",
        "OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: Implementation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Topic :: Terminals",
    ],
    install_requires=[
        "robotframework>=7.0.1",
        "robotframework-sshlibrary>=3.8.0",
    ],
    keywords="robotframework terminal testing telnet ssh",
    python_requires=">=3.10.12",
    platforms="any",
)

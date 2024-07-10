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


import re
import sys

from robot.api.deco import keyword
from robot.version import get_version

from .AbstractTerminal import AbstractTerminal
from .SSHBackend import SSHBackend
from .TelnetBackend import TelnetBackend


def create_terminal_backend(connection: str) -> AbstractTerminal:
    """
    Create a plain text terminal backend
    """
    backend = (
        re.match(
            re.compile(r"(?P<backend>\w+)\+(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"),
            connection,
        )
        .group("backend")
        .upper()
    )
    if backend == "SSH":
        return SSHBackend(connection)
    elif backend == "TELNET":
        return TelnetBackend(connection)
    else:
        return NotImplementedError("Not found your given backend name: " + str(backend))


class PlainTextTerminal:
    """A suite for plain text terminal testing"""

    ROBOT_LIBRARY_SCOPE = "SUITE"
    ROBOT_LIBRARY_VERSION = get_version()
    ROBOT_AUTO_KEYWORDS = False

    _terminal = None

    def __init__(self, connection: str = None):
        """Plain Text Terminal allows to typing on any consoles

        Create default connection, when is importing library:

        With Telnet:

        | Library | | PlainTextTerminal |
        | ... | | connection=Telnet+IPv4 |
        | ... | | prompt=$ |

        With SSH:

        | Library | | PlainTextTerminal |
        | ... | | connection=SSH+IPv4 |
        | ... | | prompt=$ |

        With prompt regular expression:

        | Library | | PlainTextTerminal |
        | ... | | connection=<Telnet or SSH>+IPv4 |
        | ... | | prompt=REGEXP:[$#] |

        Or import with leave default to be configured at `Open Connection`

        | Library | PlainTextTerminal |
        | Say Hi! |
        | | [Setup] | Open Connection |
        | | ... | connection=<Telnet or SSH>+IPv4 |
        | | ... | prompt=REGEXP:[$#] |
        | | Execute Command | echo "Hi" |
        | | [Teardown] | Close Connection |

        [https://github.com/robotframework-terminal/PlainTextTerminal/issues/new/choose|New Bug Report]
        """

        if connection:
            try:
                self._terminal = create_terminal_backend(connection)
            except RuntimeError as exc:
                sys.exit(str(exc))

    @keyword(name="Close All Connections")
    def close_all_connections(self):
        """Close all plain text terminals."""

        return self._terminal.close_all_connections()

    @keyword(name="Close Connection")
    def close_connection(self):
        """Close plain text terminal"""

        return self._terminal.close_connection()

    @keyword(name="Execute command", types=[str])
    def execute_command(self, command: str):
        """Execute command on plain text terminal"""

        return self._terminal.execute_command(command=command)

    @keyword(
        name="Login",
        types=[str, str],
    )
    def login(self, username: str, password: str):
        """Login on plain text terminal"""

        return self._terminal.login(username=username, password=password)

    @keyword(
        name="Open Connection",
        types=[str, str, int, str, str, str],
    )
    def open_connection(
        self,
        host: str = None,
        alias: str = None,
        port: int = None,
        timeout: str = None,
        newline: str = None,
        prompt: str = None,
        connection: str = None,
    ):
        """Open connection on plain text terminal"""

        if connection:
            try:
                self._terminal = create_terminal_backend(connection)
            except RuntimeError as exc:
                sys.exit(str(exc))

        return self._terminal.open_connection(
            host=host,
            alias=alias,
            port=port,
            timeout=timeout,
            newline=newline,
            prompt=prompt,
            connection=connection,
        )

    @keyword(name="Read", types=[str])
    def read(self, loglevel: str = None):
        """Read on plain text terminal"""

        return self._terminal.read(loglevel=loglevel)

    @keyword(name="Read Until", types=[str, str])
    def read_until(self, expected: str, loglevel: str = None):
        """Read until on plain text terminal"""

        return self._terminal.read_until(expected=expected, loglevel=loglevel)

    @keyword(name="Read Until Prompt", types=[str, bool])
    def read_until_prompt(self, loglevel: str = None, strip_prompt: bool = None):
        """Read until on prompt plain text terminal"""

        return self._terminal.read_until_prompt(loglevel=loglevel, strip_prompt=strip_prompt)

    @keyword(name="Read Until Regexp", types=[str])
    def read_until_regexp(self, regexp: str):
        """Read until on regexp plain text terminal"""

        return self._terminal.read_until_regexp(regexp=regexp)

    @keyword(name="Switch Connection", types=[int | str])
    def switch_connection(self, index_or_alias: int | str):
        """Switch connection over plain text terminal"""

        return self._terminal.switch_connection(index_or_alias=index_or_alias)

    @keyword(name="Write Bare", types=[str])
    def write_bare(self, text: str):
        """Write bare to plain text terminal"""

        return self._terminal.write_bare(text=text.replace("<ENTER>", "\r\n"))

    @keyword(
        name="Write Until Expected Output",
        types=[str, str, str, str, str],
    )
    def write_until_expected_output(
        self,
        text: str,
        expected: str = None,
        timeout: str = None,
        retry_interval: str = None,
        loglevel: str = None,
    ):
        """Write until expected output to plain text terminal"""

        return self._terminal.write_until_expected_output(
            text=text.replace("<ENTER>", "\r\n"),
            expected=expected,
            timeout=timeout,
            retry_interval=retry_interval,
            loglevel=loglevel,
        )

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

from robot.libraries.Telnet import Telnet

from .AbstractTerminal import AbstractTerminal


class TelnetBackend(AbstractTerminal):
    """Telnet backend"""

    def _connection_paser(self, connection: str):
        _terminal_params = {
            # Common
            "username": r"[ \t]*username[ \t]*=[ \t]*(?P<username>\w{4,})[ \t]*,?",
            "password": r"[ \t]*password[ \t]*=[ \t]*(?P<password>[A-Za-z0-9@#$%^&+=]{4,})[ \t]*,?",
            # Common Telnet and SSH
            "host": r"Telnet\+[ \t]*(?P<host>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[ \t]*),?",
            "alias": r"[ \t]*alias[ \t]*=(?P<alias>[-\w]*),?",
            "port": r"[ \t]*port[ \t]*=(?P<port>\d+)[ \t]*,?",
            "timeout": r"[ \t]*timeout[ \t]*=[ \t]*(?P<timeout>\d+[ \t]*seconds),?",
            "newline": r"[ \t]*newline[ \t]*=[ \t]*(?P<newline>\w+)[ \t]*,?",
            "prompt": r"[ \t]*prompt[ \t]*=[ \t]*(?P<prompt>\w+)[ \t]*,?",
        }

        self._terminal_host = None
        self._terminal_alias = None
        self._terminal_port = 23
        self._terminal_timeout = None
        self._terminal_newline = None
        self._terminal_prompt = None

        for _key in _terminal_params:

            _match = re.search(_terminal_params[_key], connection)

            if not _match:
                continue
            else:
                _value = _match.group(_key)

            if _key == "username":
                self._terminal_username = _value
            elif _key == "password":
                self._terminal_password = _value
            elif _key == "host":
                self._terminal_host = _value
            elif _key == "alias":
                self._terminal_alias = _value
            elif _key == "port":
                self._terminal_port = _value
            elif _key == "timeout":
                self._terminal_timeout = _value
            elif _key == "newline":
                self._terminal_newline = _value
            elif _key == "prompt":
                self._terminal_prompt = _value

    def __init__(self, connection: str):
        self._terminal = Telnet()

        if connection:
            self._connection_paser(connection)

    def close_all_connections(self):
        return self._terminal.close_all_connections()

    def close_connection(self):
        return self._terminal.close_connection()

    def execute_command(self, command: str):
        return self._terminal.execute_command(command=command)

    def login(self, username: str, password: str):
        return self._terminal.login(username=username, password=password)

    def open_connection(
        self,
        host: str,
        alias: str,
        port: int,
        timeout: str,
        newline: str,
        prompt: str,
        connection: str,
    ):
        if connection:
            self._connection_paser(connection)

        return self._terminal.open_connection(
            host=host if host else self._terminal_host,
            alias=alias if alias else self._terminal_alias,
            port=port if port else self._terminal_port,
            timeout=timeout if timeout else self._terminal_timeout,
            newline=newline if newline else self._terminal_newline,
            prompt=prompt if prompt else self._terminal_prompt,
        )

    def read(self, loglevel: str):
        return self._terminal.read(loglevel=loglevel)

    def read_until(self, expected: str, loglevel: str):
        return self._terminal.read_until(expected=expected, loglevel=loglevel)

    def read_until_prompt(self, loglevel: str, strip_prompt: bool):
        return self._terminal.read_until_prompt(loglevel=loglevel, strip_prompt=strip_prompt)

    def read_until_regexp(self, regexp: str):
        return self._terminal.read_until_regexp(regexp)

    def switch_connection(self, index_or_alias: int | str):
        return self._terminal.switch_connection(index_or_alias=index_or_alias)

    def write_bare(self, text: str):
        return self._terminal.write_bare(text=text)

    def write_until_expected_output(
        self, text: str, expected: str, timeout: str, retry_interval: str, loglevel: str
    ):
        return self._terminal.write_until_expected_output(
            text=text,
            expected=expected,
            timeout=timeout,
            retry_interval=retry_interval,
            loglevel=loglevel,
        )

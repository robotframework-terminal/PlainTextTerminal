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


from abc import ABCMeta, abstractmethod


class AbstractTerminal(metaclass=ABCMeta):
    """Minimal set of interfaces over plain text terminal"""

    @abstractmethod
    def close_all_connections(self):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    @abstractmethod
    def execute_command(self, command: str):
        pass

    @abstractmethod
    def login(self, username: str, password: str):
        pass

    @abstractmethod
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
        pass

    @abstractmethod
    def read(self, loglevel: str):
        pass

    @abstractmethod
    def read_until(self, expected: str, loglevel: str):
        pass

    @abstractmethod
    def read_until_prompt(self, loglevel: str, strip_prompt: bool):
        pass

    @abstractmethod
    def read_until_regexp(self, regexp: str):
        pass

    @abstractmethod
    def switch_connection(self, index_or_alias: int | str):
        pass

    @abstractmethod
    def write_bare(self, text: str):
        pass

    @abstractmethod
    def write_until_expected_output(
        self, text: str, expected: str, timeout: str, retry_interval: str, loglevel: str
    ):
        pass

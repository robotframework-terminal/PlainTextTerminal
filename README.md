# Introduction
The Plain Text Terminal works cross Telnet and SSH, without modification the Robot code

## How to install
* $ python3 -m pip install -e git+https://github.com/robotframework-terminal/PlainTextTerminal.git@v1.0.0#egg=PlainTextTerminal

## How to use it under a virtual environment
#### Active the virtual enviroment
* $ python3 -m venv .venv
* $ source .venv/bin/activate
* $ python3 -m pip install --upgrade -r requirements.txt

#### Deactive the virtual enviroment
* $ deactivate

## Example
#### With library import default configuration
```
*** Settings ***

Library             PlainTextTerminal
...                     connection=<Telnet or SSH>+IPv4
...                     prompt=REGEXP:[$#]

Suite Teardown      Close All Connections


*** Test Cases ***
How to say Hi!
    [Documentation]    Let say Hi!

    Login
    ...    username=USERNAME
    ...    password=PASSWORD

    Write Bare
    ...    text=echo "Hi!"<ENTER>

    Read Until Prompt

    [Teardown]    Close Connection
```

#### With empty library import configuration
```
*** Settings ***

Library             PlainTextTerminal

Suite Teardown      Close All Connections


*** Test Cases ***
How to say Hi!
    [Documentation]    Let say Hi!

    [Setup]    Open Connection
    ...            connection=<Telnet or SSH>+IPv4
    ...            prompt=REGEXP:[$#]

    Login
    ...    username=USERNAME
    ...    password=PASSWORD

    Write Bare
    ...    text=echo "Hi!"<ENTER>

    Read Until Prompt

    [Teardown]    Close Connection
```
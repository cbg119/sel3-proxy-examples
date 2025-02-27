*** Settings ***
| Resource | resource.robot

*** Test Cases ***
| Visit the website
| | Open login page
| | [Teardown] | End Session
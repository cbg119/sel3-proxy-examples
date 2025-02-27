| *** Settings ***
| Library | SeleniumLibrary

| *** Variables ***

| &{capabilities}
| ... | browserName=chrome
| ... | platform=windows 10
| ... | version=latest
| ... | username=%{SAUCE_USERNAME}
| ... | accessKey=%{SAUCE_ACCESS_KEY}
| ... | name=Robot Proxy Debug Test

| ${remote_url} | https://ondemand.us-west-1.saucelabs.com/wd/hub

| *** Keywords ***
| Open login page
| | Open browser | url=https://the-internet.herokuapp.com/login | browser=chrome | remote_url=${remote_url} | desired_capabilities=${capabilities}

| End Session
| | Run Keyword If | '${TEST STATUS}' == 'PASS' | Execute Javascript | sauce:job-result=passed
| ... | ELSE | Execute Javascript | sauce:job-result=failed
| | Close Browser
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Test Teardown     fn_Close Browser


*** Variables ***
${URL}            https://login.yahoo.com/
${BROWSER}        Chrome

*** Test Cases ***
Yahoo
    fn_Open Browser

*** Keywords ***
fn_Open Browser
    Open Browser    ${URL}      ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait      10s
    Input Text      //input[@name='username']       anusha.palemofficial@yahoo.com        clear=True
    Click Button    //input[@name='signin']
    Input Text      //input[@name='password']       Cherry@2018        clear=True
    Click Button    //button[@name='verifyPassword']
    sleep       5s

fn_Close Browser
    Close All Browsers

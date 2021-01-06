*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Test Open
    Open Browser    https://www.google.com/   Chrome
    Set Selenium Implicit Wait  15s
    Click on Gmail Link
    Close All Browsers

*** Keywords ***
Click on Gmail Link
    Element Should Be Visible   //a[text()='Gmail']
    Click Link  //a[text()='Gmail']
    ${title}=   Get Title
    Log To Console  ${title}
    Should Be Equal     ${title}     Gmail - Email from Google
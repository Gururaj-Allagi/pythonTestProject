*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Test Setup        fn_Open Browser
Test Teardown     fn_Close Browser
Library           HeadLessBrowser.py
Resource          TestRobot2.robot


*** Variables ***
${URL}            http://github.com/Gururaj-Allagi
${BROWSER}        Chrome

*** Test Cases ***
Git Hub
    Open Browser And Verify The Title
    Click On WhyGitHub? Mouse Over

*** Keywords ***
Open Browser And Verify The Title
    ${title}=        Get Title
    Should Be Equal     Gururaj-Allagi (Gururaj Allagi) · GitHub        ${title}    values=True
    Wait Until Element Is Visible	    xpath://span[text()='Gururaj Allagi']
    Element Should Contain  xpath://span[text()='Gururaj Allagi']   gururaj  ignore_case=True
    Run Keyword If   True     Log To Console   if run
    ...     ELSE    Log To Console      else
    Log To Console     Success

Click On WhyGitHub? Mouse Over
    Mouse Over	    xpath://summary[contains(text(),'Why GitHub?')]
    Set Focus To Element    xpath://summary[contains(text(),'Why GitHub?')]
    Click Link      xpath://a[contains(text(),'Code review')]

fn_Open Browser
    Open Browser    ${URL}      ${BROWSER}
    Maximize Browser Window
    Set Selenium Implicit Wait      10s

fn_Close Browser
    Close All Browsers
    LogGuru
    
*** Settings ***
Documentation     Simple example using SeleniumLibrary.
Library           SeleniumLibrary
Library           RequestsLibrary
Library           Collections

*** Test Cases ***
Test Request
    Create Session    google         https://reqres.in       disable_warnings=1
    ${reps}=          Get Request    google       /api/users/2
    ${str}=     Convert To String   ${reps.status_code}
    Should be Equal    ${str}      200
    Log To Console     \n${reps.content}
    ${eval_dict}=       evaluate    json.loads('''${reps.content}''')       json
    ${dict_Value}=      Convert To Dictionary     ${eval_dict}
    ${lst}=      Get From Dictionary      ${dict_Value}       data
    ${email}=      Get From Dictionary      ${lst}       email
    Log To Console     \n\n${email}
*** Settings ***
Library           MongoDBLibrary
Library           Collections
Library           JSONLibrary
Library           TestRE.testClass


*** Variables ***
${MDBHost}        mongodb+srv://root:root@cluster0.wxsvq.mongodb.net/test?retryWrites=true&w=majority
${MDBPort}        ${27017}

*** Test Cases ***
Get MongoDB Databases
    Connect To MongoDB    ${MDBHost}    ${MDBPort}
    ${res}=     Get Mongodb Collections    sample_analytics
    Log To Console      \n${res}
    ${res}=     Retrieve Some Mongodb Records    sample_analytics    accounts   {"account_id": 371138}  returnDocuments=False
    Log To Console      \n${res}
    Disconnect-MongoDB

Connect MongoDB usin python resource
    test_test

*** Keywords ***
Disconnect-MongoDB
    [Tags]    Dissconnect MongoDB connection
    Disconnect From MongoDB
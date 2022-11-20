*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Keywords ***
Input New command And Create User
    Create User  usernameee  passssword4321
    Input New Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  userna  password12345
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  usernameee  password1
    Output Should Contain  User with username usernameee already exists

Register With Too Short Username And Valid Password
    Input Credentials  u  password321
    Output Should Contain  Username is too short

Register With Valid Username And Too Short Password
    Input Credentials  username  pass1
    Output Should Contain  Password is too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  password
    Output Should Contain  Password is invalid
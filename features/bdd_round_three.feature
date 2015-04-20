Feature: Round Three features
    Scenario: Create route of cities
        Given I am researching speed
        When I create a list of cities
        Then I can get a more accurate picture

    Scenario: Input my city
        Given the application has been started
        When I enter my start city
        Then the application knows where I am

    Scenario: Account for network lag
        Given there is network latency
        When I research speeds
        Then network lag is accounted for

    Scenario: Input HD speed
        Givin I know my HD speed
        When I input the speed
        Then the latency is accounted for




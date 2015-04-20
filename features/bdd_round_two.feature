Feature: Round Two Features

    Scenario: Input preset speed values
        Given I know some relative speed
        When I input the driving speed
        Then I can specify a relative speed

    Scenario: Create new city
        Given I am selecting a city
        When I want to create a new city
        Then I am able to create a new city

    Scenario: Saving a city
        Givin I have input a new city
        When I input the city
        Then the new city is saved to the file


Feature: Speed Testing

    Scenario: Read data from a file
        Given A file is provided
        When the system is initialized
        Then The system reads the cities, distances and connection speeds from file

    Scenario: Speed estimate selection
        Given I want to know which route would be faster
        When I select a speed estimate
        Then the system will indicate whether the network or driving would be faster

    Scenario: HD Size selection
        Given I know my HD size
        When I select HD Size
        Then the system will allocate more space so I can have more data

    Scenario: City, speed, and size input
        Given I know the city, speed, and HD size
        When I input the city, speed, and HD size
        Then the system will determine and indicate which would be better
        Then the system can log the difference in times between the network and the HD



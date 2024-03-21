# Feature File 
Feature: OTT Playback Scenario

Scenario: User starts watching a movie
    Given the user is on the OTT platform
    When the user selects a movie to watch
    Then the movie starts playing

Scenario: User pauses the movie
    Given the user is watching a movie on the OTT platform
    When the user pauses the movie
    Then the movie stops playing

Scenario: User resumes the movie
    Given the user has paused a movie on the OTT platform
    When the user resumes the movie
    Then the movie continues playing from where it was paused

Scenario: User skips ahead in the movie
    Given the user is watching a movie on the OTT platform
    When the user skips ahead in the movie
    Then the movie starts playing from the skipped point

Scenario: User finishes watching the movie
    Given the user has watched a movie on the OTT platform
    When the movie ends
    Then the user is prompted to rate the movie

Scenario: User exits the movie
    Given the user is watching a movie on the OTT platform
    When the user exits the movie
    Then the movie stops playing and the user is taken back to the main menu
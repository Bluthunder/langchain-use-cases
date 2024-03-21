# Feature File 
Feature: OTT Playback Scenario

Scenario: User plays a video successfully
    Given the user is on the OTT platform
    When the user selects a video to play
    Then the video should start playing successfully

Scenario: User pauses a video
    Given the user is watching a video on the OTT platform
    When the user pauses the video
    Then the video should pause at the current timestamp

Scenario: User resumes a paused video
    Given the user is watching a paused video on the OTT platform
    When the user resumes the video
    Then the video should continue playing from where it was paused

Scenario: User skips forward in a video
    Given the user is watching a video on the OTT platform
    When the user skips forward in the video
    Then the video should continue playing from the new timestamp

Scenario: User skips backward in a video
    Given the user is watching a video on the OTT platform
    When the user skips backward in the video
    Then the video should continue playing from the new timestamp

Scenario: User changes the video quality
    Given the user is watching a video on the OTT platform
    When the user changes the video quality
    Then the video should continue playing in the new quality

Scenario: User exits the video player
    Given the user is watching a video on the OTT platform
    When the user exits the video player
    Then the video should stop playing and the user should be redirected to the home screen
# File 
Feature: OTT Playback Scenario

Scenario: User plays a video successfully
    Given the user is on the OTT platform
    When the user selects a video to play
    Then the video starts playing successfully

Scenario: User pauses a video
    Given the user is watching a video on the OTT platform
    When the user pauses the video
    Then the video stops playing temporarily

Scenario: User resumes a paused video
    Given the user has paused a video on the OTT platform
    When the user resumes the video
    Then the video continues playing from where it was paused

Scenario: User skips forward in a video
    Given the user is watching a video on the OTT platform
    When the user skips forward in the video
    Then the video jumps ahead to the specified time

Scenario: User skips backward in a video
    Given the user is watching a video on the OTT platform
    When the user skips backward in the video
    Then the video jumps back to the specified time

Scenario: User adjusts the volume of a video
    Given the user is watching a video on the OTT platform
    When the user adjusts the volume
    Then the volume of the video changes accordingly

Scenario: User changes the video quality
    Given the user is watching a video on the OTT platform
    When the user changes the video quality settings
    Then the video quality is adjusted as per the user's preference

Scenario: User exits the video playback
    Given the user is watching a video on the OTT platform
    When the user exits the video playback
    Then the video stops playing and the user is taken back to the main screen
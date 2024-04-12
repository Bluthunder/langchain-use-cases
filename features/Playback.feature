# File 
Feature: OTT Playback Scenario

Scenario: User plays a video from the beginning
    Given the user is on the OTT platform
    When the user selects a video to play
    Then the video starts playing from the beginning

Scenario: User pauses a video
    Given the user is watching a video on the OTT platform
    When the user pauses the video
    Then the video stops playing

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

Scenario: User changes the video quality
    Given the user is watching a video on the OTT platform
    When the user changes the video quality settings
    Then the video quality adjusts accordingly

Scenario: User turns on subtitles
    Given the user is watching a video on the OTT platform
    When the user turns on subtitles
    Then subtitles are displayed on the video

Scenario: User turns off subtitles
    Given the user is watching a video with subtitles on the OTT platform
    When the user turns off subtitles
    Then subtitles are no longer displayed on the video
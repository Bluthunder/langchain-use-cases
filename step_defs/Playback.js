# File 
const { Given, When, Then } = require('cucumber');
const { expect } = require('chai');

const OTTPlaybackPage = require('../pageObjects/OTTPlaybackPage');

Given('the user is on the OTT platform', async () => {
    // Add code to navigate to the OTT platform
});

When('the user selects a video to play', async () => {
    await OTTPlaybackPage.selectVideo();
});

Then('the video starts playing from the beginning', async () => {
    expect(await OTTPlaybackPage.isVideoPlaying()).to.be.true;
});

When('the user pauses the video', async () => {
    await OTTPlaybackPage.pauseVideo();
});

Then('the video stops playing', async () => {
    expect(await OTTPlaybackPage.isVideoPlaying()).to.be.false;
});

When('the user resumes the video', async () => {
    await OTTPlaybackPage.resumeVideo();
});

Then('the video continues playing from where it was paused', async () => {
    expect(await OTTPlaybackPage.isVideoPlaying()).to.be.true;
});

When('the user skips forward in the video', async () => {
    await OTTPlaybackPage.skipForward();
});

Then('the video jumps ahead to the specified time', async () => {
    // Add code to verify video has jumped ahead
});

// Repeat the above steps for the remaining scenarios

module.exports = {
    Given,
    When,
    Then
};
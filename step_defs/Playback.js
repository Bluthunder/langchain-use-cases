# Feature File 
const { Given, When, Then } = require('cucumber');
const { expect } = require('chai');

const OTTPage = require('../pageObjects/OTTPage');

Given('the user is on the OTT platform', async () => {
    // Code to navigate to the OTT platform
});

When('the user selects a movie to watch', async () => {
    await OTTPage.selectMovie();
});

Then('the movie starts playing', async () => {
    expect(await OTTPage.isMoviePlaying()).to.be.true;
});

When('the user pauses the movie', async () => {
    await OTTPage.pauseMovie();
});

Then('the movie stops playing', async () => {
    expect(await OTTPage.isMoviePlaying()).to.be.false;
});

Given('the user has paused a movie on the OTT platform', async () => {
    await OTTPage.pauseMovie();
});

When('the user resumes the movie', async () => {
    await OTTPage.resumeMovie();
});

Then('the movie continues playing from where it was paused', async () => {
    expect(await OTTPage.isMoviePlaying()).to.be.true;
});

When('the user skips ahead in the movie', async () => {
    await OTTPage.skipAhead();
});

Then('the movie starts playing from the skipped point', async () => {
    expect(await OTTPage.getCurrentTime()).to.be.above(0);
});

Given('the user has watched a movie on the OTT platform', async () => {
    // Code to mark the movie as watched
});

When('the movie ends', async () => {
    await OTTPage.endMovie();
});

Then('the user is prompted to rate the movie', async () => {
    expect(await OTTPage.isRatingPromptDisplayed()).to.be.true;
});

When('the user exits the movie', async () => {
    await OTTPage.exitMovie();
});

Then('the movie stops playing and the user is taken back to the main menu', async () => {
    expect(await OTTPage.isMoviePlaying()).to.be.false;
    expect(await OTTPage.isMainMenuDisplayed()).to.be.true;
});
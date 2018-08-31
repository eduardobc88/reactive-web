var documentReady = function() {
    console.log('home.js');
}


var windowLoad = function() {
    initSlider();
}


var initSlider = function() {
    var miliseccondsBeforeNextSlide = 10000;
    $('#slides').superslides({
        play: miliseccondsBeforeNextSlide
    });
}


$(document).ready(documentReady);
$(window).on('load', windowLoad);

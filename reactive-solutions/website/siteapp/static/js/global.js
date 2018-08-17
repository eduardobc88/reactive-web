var mobileMenuElement = null;

var documentReady = function() {
    console.log('global.js');
    mobileMenuElement = $('.mobile-menu-wrapper');
}


var windowLoad = function() {

}


var openMenuMobile = function(element) {
    if( mobileMenuElement.hasClass('visible') )
        mobileMenuElement.removeClass('visible');
    else
        mobileMenuElement.addClass('visible');
}


$(document).ready(documentReady);
$(window).on('load', windowLoad);

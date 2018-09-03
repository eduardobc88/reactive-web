var mobileMenuElement = null;
var menuWapperElement = null;

var documentReady = function() {
    mobileMenuElement = $('.mobile-menu-wrapper');
    menuWapperElement = $('.menu-wrapper');
}


var windowLoad = function() {

}


var openMenuMobile = function(element) {
    if( mobileMenuElement.hasClass('visible') )
        mobileMenuElement.removeClass('visible');
    else
        mobileMenuElement.addClass('visible');
}

var onScroll = function(element) {
    if( $(element).scrollTop() > 80 ) {
        menuWapperElement.addClass('page-scroll');
    } else {
        menuWapperElement.removeClass('page-scroll');
    }
}


$(document).ready(documentReady);
$(window).on('load', windowLoad);

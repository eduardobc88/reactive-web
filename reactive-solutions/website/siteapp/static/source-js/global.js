var mobileMenuElement = null;
var menuWapperElement = null;
var windowElement = null;

var documentReady = function() {

}

var windowLoad = function() {
    mobileMenuElement = $('.mobile-menu-wrapper');
    menuWapperElement = $('.menu-wrapper');
    windowElement = $(window);
    setMenuBkgColor();
    windowOnScroll();
}

var openMenuMobile = function(element) {
    if( mobileMenuElement.hasClass('visible') )
        mobileMenuElement.removeClass('visible');
    else
        mobileMenuElement.addClass('visible');
}

var windowOnScroll = function() {
    $(windowElement).scroll(setMenuBkgColor);
}

var setMenuBkgColor = function() {
    if(menuWapperElement == null) {
        return false;
    }
    if($(windowElement).scrollTop() > 80) {
        menuWapperElement.addClass('page-scroll');
    } else {
        menuWapperElement.removeClass('page-scroll');
    }
}


$(document).ready(documentReady);
$(window).on('load', windowLoad);

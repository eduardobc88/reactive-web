var mobileMenuElement=null,menuWapperElement=null,documentReady=function(){mobileMenuElement=$(".mobile-menu-wrapper"),menuWapperElement=$(".menu-wrapper")},windowLoad=function(){},openMenuMobile=function(e){mobileMenuElement.hasClass("visible")?mobileMenuElement.removeClass("visible"):mobileMenuElement.addClass("visible")},onScroll=function(e){80<$(e).scrollTop()?menuWapperElement.addClass("page-scroll"):menuWapperElement.removeClass("page-scroll")};$(document).ready(documentReady),$(window).on("load",windowLoad);
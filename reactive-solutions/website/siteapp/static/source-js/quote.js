var EMAIL_REGEX = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/, '');
var PHONE_NUMBER = new RegExp(/^\d{3}\d{3}\d{4}$/, '');
var URL_REGEX = new RegExp(/^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/, '');
var formElement = null;


var openContent = function(element) {
    parentElement = $(element).parent();
    isOpen = parentElement.hasClass('open');
    $('.item').removeClass('open');
    if(!isOpen) {
        parentElement.addClass('open');
    }
}

var initForm = function() {
    formElement.find('.input-text').on('blur', function() {
        if(!$(this).val())
            $(this).parent().removeClass('active');
    });

    formElement.find('.input-text').on('focus', function() {
        $(this).parent().addClass('active');
    });
}

var formValidation = function(element) {
    pass = true;
    var name = $(element.target).find('.input-text.name');
    var email = $(element.target).find('.input-text.email');
    var phone = $(element.target).find('.input-text.phone');
    var url = $(element.target).find('.input-text.url');
    var message = $(element.target).find('.input-text.message');
    $(element.target).find('.required').removeClass('required');

    if(!name.val()) {
        pass = false;
        name.parent().addClass('required');
    }
    if(!email.val() || !EMAIL_REGEX.test(email.val())) {
        pass = false;
        email.parent().addClass('required');
    }
    if(!phone.val() || !PHONE_NUMBER.test(phone.val())) {
        pass = false;
        phone.parent().addClass('required');
    }
    if(url.val() && !URL_REGEX.test(url.val())) {
        pass = false;
        url.parent().addClass('required');
    }
    if(!message.val()) {
        pass = false;
        message.parent().addClass('required');
    }

    return pass;
}


var documentReady = function() {

}


var windowLoad = function() {
    formElement = $('.form-wrapper');
    initForm();
    $('.validate-support').submit(formValidation);
    $('.validate-static-web').submit(formValidation);
    $('.validate-dynamic-web').submit(formValidation);
}

$(document).ready(documentReady);
$(window).on('load', windowLoad);

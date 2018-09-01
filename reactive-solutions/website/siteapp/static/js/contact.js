var EMAIL_REGEX = new RegExp(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/, 'gm')
var PHONE_NUMBER = new RegExp(/^\d{3}\d{3}\d{4}$/, 'gm');
var URL_REGEX = new RegExp(/^(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,5}(:[0-9]{1,5})?(\/.*)?$/, 'gm');
var formElement = null;


var initForm = function() {
    formElement.find('.input-text').on('blur', function() {
        if(!$(this).val())
            $(this).parent().removeClass('active');
    });

    formElement.find('.input-text').on('focus', function() {
        $(this).parent().addClass('active');
    });
}

var formValidation = function(event) {
    pass = true;
    var name = $('.input-text.name');
    var lastName = $('.input-text.lastname');
    var email = $('.input-text.email');
    var phone = $('.input-text.phone');
    var url = $('.input-text.url');
    var message = $('.input-text.message');
    $('.required').removeClass('required');

    if(!name.val()) {
        pass = false;
        name.parent().addClass('required');
    }
    if(!lastName.val()) {
        pass = false;
        lastName.parent().addClass('required');
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
    formElement = $('.form-wrapper');
    initForm();
    $('.form-wrapper').submit(formValidation)
}


var windowLoad = function() {

}

$(document).ready(documentReady);
$(window).on('load', windowLoad);

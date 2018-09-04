var shareThis = function() {
    if($('.share-fb').length) {
        var shareFB = $('.share-fb');
        shareFB.on('click', function(){
            var permalink = shareFB.attr('attr-permalink');
            var facebookWindow = window.open('https://www.facebook.com/sharer/sharer.php?u=' + permalink, 'facebook-popup', 'height=350,width=600');
            if(facebookWindow.focus) {
                facebookWindow.focus();
            }
            return false;
        });
    }
    if($('.share-tw').length) {
        var shareTW = $('.share-tw');
        shareTW.on('click', function(){
            var permalink = shareTW.attr('attr-permalink');
            var twitterWindow = window.open('https://twitter.com/share?url=' + permalink, 'twitter-popup', 'height=350,width=600');
            if(twitterWindow.focus) {
                twitterWindow.focus();
            }
            return false;
        });
    }
    if($('.share-gp').length) {
        var shareGP = $('.share-gp');
        shareGP.on('click', function(){
            var permalink = shareGP.attr('attr-permalink');
            var googlePlusWindow = window.open("https://plus.google.com/share?url='"+permalink+"'", 'google-plus-popup', 'height=350,width=600');
            if(googlePlusWindow.focus) {
                googlePlusWindow.focus();
            }
            return false;
        });
    }
    if($('.share-wa').length) {
        var sahreWA = $('.share-wa');
        sahreWA.on('click', function(){
            var permalink = sahreWA.attr('attr-permalink');
            var url = 'whatsapp://send?text=';
            var text = 'Hey checa esto, puede que te interese: '+permalink;
            var encodedText = encodeURIComponent(text);
            window.location.href = url + encodedText;
            return false;
        });
    }
    if($('.share-t').length) {
        var shareT = $('.share-t');
        shareT.on('click', function(){
            var permalink = shareT.attr('attr-permalink');
            var url = 'tg://msg_url?url=';
            var text = 'Hey checa esto, puede que te interese: '+permalink;
            var encodedText = encodeURIComponent(text);
            window.location.href = url + encodedText;
            return false;
        });
    }
}

var windowLoad = function() {
    shareThis()
}


$(window).on('load', windowLoad);

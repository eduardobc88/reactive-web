var shareThis=function(){if($(".share-fb").length){var r=$(".share-fb");r.on("click",function(){var e=r.attr("attr-permalink"),t=window.open("https://www.facebook.com/sharer/sharer.php?u="+e,"facebook-popup","height=350,width=600");return t.focus&&t.focus(),!1})}if($(".share-tw").length){var o=$(".share-tw");o.on("click",function(){var e=o.attr("attr-permalink"),t=window.open("https://twitter.com/share?url="+e,"twitter-popup","height=350,width=600");return t.focus&&t.focus(),!1})}if($(".share-gp").length){var n=$(".share-gp");n.on("click",function(){var e=n.attr("attr-permalink"),t=window.open("https://plus.google.com/share?url='"+e+"'","google-plus-popup","height=350,width=600");return t.focus&&t.focus(),!1})}if($(".share-wa").length){var a=$(".share-wa");a.on("click",function(){var e=a.attr("attr-permalink"),t=encodeURIComponent("Hey checa esto, puede que te interese: "+e);return window.location.href="whatsapp://send?text="+t,!1})}if($(".share-t").length){var i=$(".share-t");i.on("click",function(){var e=i.attr("attr-permalink"),t=encodeURIComponent("Hey checa esto, puede que te interese: "+e);return window.location.href="tg://msg_url?url="+t,!1})}},windowLoad=function(){shareThis()};$(window).on("load",windowLoad);
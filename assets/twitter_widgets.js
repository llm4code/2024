window.twttr = (function(d, s, id) {
    var js, fjs = d.getElementsByTagName(s)[0],
        t = window.twttr || {};
    if (d.getElementById(id)) return;
    js = d.createElement(s);
    js.id = id;
    js.src = "https://platform.twitter.com/widgets.js";
    fjs.parentNode.insertBefore(js, fjs);

    t._e = [];
    t.ready = function(f) {
        t._e.push(f);
    };

    return t;
}(document, "script", "twitter-wjs"));

twttr.ready(function (twttr) {
    twttr.events.bind(
        'rendered',
        function (event) {
            var width = (window.innerWidth > 0) ? window.innerWidth : screen.width;
            if (width > 600) {
                if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
                    document.getElementById("dark-twitter-timeline").style.display = "block";
                }
                else {
                    document.getElementById("light-twitter-timeline").style.display = "block";
                }
            }
        }
    );
});

$(document).ready(function () {
    function l() {
        function u(e) {
            for (var n = "", t = 1; 17 > t; t++) n += '<a href="#" class="thumbnail box-inline"><img class="img-responsive" src="./premium/boxed-bg/' + e + "/thumbs/" + t + '.jpg" alt="Background Image"></a>';
            return n
        }

        function h() {
            c.append(u("blurred")), f.append(u("polygon")), d.append(u("abstract"));
            var e = l.find(".thumbnail");
            e.on("click", function () {
                e.removeClass("selected");
                var n = $(this).children("img").prop("src").replace("thumbs", "bg");
                $(this).addClass("selected"), a.css({
                    "background-image": "url(" + n + ")",
                    "background-repeat": "no-repeat",
                    "background-size": "cover"
                })
            })
        }

        var n = document.getElementById("demo-box-lay"), t = document.getElementById("demo-box-img"),
            l = $("#demo-bg-boxed"), r = document.getElementById("demo-close-boxed-img"), c = $("#demo-blurred-bg"),
            f = $("#demo-polygon-bg"), d = $("#demo-abstract-bg");
        a.hasClass("boxed-layout") ? (n.checked = !0, t.disabled = !1) : (n.checked = !1, t.disabled = !0), n.onchange = function () {
            n.checked ? (a.addClass("boxed-layout"), t.disabled = !1) : (a.removeClass("boxed-layout").removeAttr("style"), t.disabled = !0, l.removeClass("open").find(".thumbnail").removeClass("selected")), $(window).trigger("resize")
        }, t.onclick = function () {
            l.hasClass("open") ? l.removeClass("open") : (l.addClass("open"), e.hasClass("hasbgthumbs") || (h(), e.addClass("hasbgthumbs")))
        }, r.onclick = function () {
            l.removeClass("open")
        };
        var p = "easeInQuart easeOutQuart easeInBack easeOutBack easeInOutBack steps jumping rubber",
            v = document.getElementById("demo-anim"), g = document.getElementById("demo-ease");
        a.hasClass("effect") ? (v.checked = !0, g.disabled = !1) : (v.checked = !1, g.disabled = !0), v.onchange = function () {
            v.checked ? (a.addClass("effect"), g.disabled = !1, g.value = "effect") : (a.removeClass("effect " + p), g.disabled = !0)
        };
        var m = p.split(" ");
        for (i = 0; i < m.length; i++) if (a.hasClass(m[i])) {
            g.value = m[i];
            break
        }
        g.onchange = function () {
            var n = ($("option:selected", this), this.options[this.selectedIndex].value);
            n && a.removeClass(p).addClass(n)
        };
        var y = document.getElementById("demo-navbar-fixed");
        y.checked = a.hasClass("navbar-fixed") ? !0 : !1, y.onchange = function () {
            y.checked ? a.addClass("navbar-fixed") : a.removeClass("navbar-fixed"), s.niftyAffix("update"), o.niftyAffix("update")
        };
        var C = document.getElementById("demo-footer-fixed");
        C.checked = a.hasClass("footer-fixed") ? !0 : !1, C.onchange = function () {
            C.checked ? a.addClass("footer-fixed") : a.removeClass("footer-fixed")
        };
        var b = document.getElementById("demo-nav-coll"), T = document.getElementById("demo-nav-fixed"),
            x = document.getElementById("demo-nav-profile"), S = document.getElementById("demo-nav-shortcut"),
            w = document.getElementById("demo-nav-offcanvas"), k = $("#mainnav-profile"), E = $("#mainnav-shortcut");
        T.checked = a.hasClass("mainnav-fixed") ? !0 : !1, T.checked = a.hasClass("mainnav-fixed") ? !0 : !1, T.onchange = function () {
            $.niftyNav(T.checked ? "fixedPosition" : "staticPosition")
        }, x.checked = k.hasClass("hidden") ? !1 : !0, x.onchange = function () {
            k.toggleClass("hidden")
        }, S.checked = E.hasClass("hidden") ? !1 : !0, S.onchange = function () {
            E.toggleClass("hidden")
        }, b.checked = a.hasClass("mainnav-sm") ? !0 : !1, b.onchange = function () {
            b.checked ? ("none" != w.value && (w.value = "none", location.href = location.protocol + "//" + location.host + location.pathname), $.niftyNav("collapse")) : $.niftyNav("expand")
        }, w.onchange = function () {
            b.checked && (b.checked = !1), e.removeClass("open"), location.href = location.protocol + "//" + location.host + location.pathname + "?&offcanvas=" + this.options[this.selectedIndex].value
        };
        var I = function () {
            for (var e = window.location.search.substring(1), n = e.split("&"), t = 0; t < n.length; t++) {
                var i = n[t].split("=");
                if ("offcanvas" == i[0]) return i[1]
            }
            return !1
        }();
        "push" == I || "slide" == I || "reveal" == I ? ($(".mainnav-toggle").removeClass("push slide reveal").addClass(I), w.value = I) : b.checked = a.hasClass("mainnav-sm") ? !0 : !1;
        var _ = document.getElementById("demo-asd-vis"), N = document.getElementById("demo-asd-fixed"),
            A = document.getElementById("demo-asd-float"), H = document.getElementById("demo-asd-align"),
            O = document.getElementById("demo-asd-themes");
        _.checked = a.hasClass("aside-in") ? !0 : !1, _.onchange = function () {
            $.niftyAside(_.checked ? "show" : "hide")
        }, N.checked = a.hasClass("aside-fixed") ? !0 : !1, N.onchange = function () {
            $.niftyAside(N.checked ? "fixedPosition" : "staticPosition")
        }, A.checked = a.hasClass("aside-float") ? !0 : !1, A.onchange = function () {
            A.checked ? a.addClass("aside-float") : a.removeClass("aside-float"), $(window).trigger("resize")
        }, H.checked = a.hasClass("aside-left") ? !0 : !1, H.onchange = function () {
            $.niftyAside(H.checked ? "alignLeft" : "alignRight")
        }, O.checked = a.hasClass("aside-bright") ? !1 : !0, O.onchange = function () {
            $.niftyAside(O.checked ? "darkTheme" : "brightTheme")
        };
        var D = $(".demo-theme"), M = function (e, n) {
            var t = $("#theme"), i = ".min.css", a = "css/themes/type-" + n + "/" + e + i;
            t.length ? t.prop("href", a) : (t = '<link id="theme" href="' + a + '" rel="stylesheet">', $("head").append(t))
        };
        $("#demo-theme").on("click", ".demo-theme", function (e) {
            e.preventDefault();
            var n = $(this);
            return n.hasClass("disabled") ? !1 : (M(n.attr("data-theme"), n.attr("data-type")), D.removeClass("disabled"), n.addClass("disabled"), !1)
        })
    }

    var e = $("#demo-set"), a = ($("#demo-set-icon"), $("#demo-set-btngo"), $("#container")),
        s = $("#mainnav-container"), o = $("#aside-container");
    if (e.length) {
        var r = function () {
            for (var e = window.location.search.substring(1), n = e.split("&"), t = 0; t < n.length; t++) {
                var i = n[t].split("=");
                if ("offcanvas" == i[0]) return i[1]
            }
            return !1
        }();
        ("push" == r || "slide" == r || "reveal" == r) && ($(".mainnav-toggle").removeClass("push slide reveal").addClass(r), a.removeClass("mainnav-lg mainnav-sm").addClass("mainnav-out " + r));
        var e = $("#demo-set-body"), c = $("#demo-set-btn");
        $("html").on("click", function (n) {
            e.hasClass("in") && ($(n.target).closest("#demo-set").length || c.trigger("click"))
        }), c.one("click", l), $("#demo-btn-close-settings").on("click", function () {
            c.trigger("click")
        })
    }
});
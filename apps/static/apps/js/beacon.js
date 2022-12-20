!function (e) {
    function n(r) {
        if (t[r]) return t[r].exports;
        var i = t[r] = {i: r, l: !1, exports: {}};
        return e[r].call(i.exports, i, i.exports, n), i.l = !0, i.exports
    }

    var t = {};
    n.m = e, n.c = t, n.d = function (e, t, r) {
        n.o(e, t) || Object.defineProperty(e, t, {configurable: !1, enumerable: !0, get: r})
    }, n.n = function (e) {
        var t = e && e.__esModule ? function () {
            return e.default
        } : function () {
            return e
        };
        return n.d(t, "a", t), t
    }, n.o = function (e, n) {
        return Object.prototype.hasOwnProperty.call(e, n)
    }, n.p = "", n(n.s = 0)
}([function (e, n, t) {
    "use strict";
    var r = this && this.__assign || function () {
        return r = Object.assign || function (e) {
            for (var n, t = 1, r = arguments.length; t < r; t++) {
                n = arguments[t];
                for (var i in n) Object.prototype.hasOwnProperty.call(n, i) && (e[i] = n[i])
            }
            return e
        }, r.apply(this, arguments)
    };
    n.__esModule = !0;
    var i = t(1), o = t(2), a = t(3), c = t(4);
    !function () {
        function e(e) {
            var n = "";
            if (n = window.location.origin ? window.location.origin : window.location.protocol + "://" + window.location.host, e && "string" == typeof e) if (0 === e.indexOf("/")) n += e; else try {
                var t = new URL(e);
                return t.protocol + "://" + t.host + t.pathname
            } catch (e) {
            } else {
                var r = window.location.pathname;
                r && r.length > 0 && (n += r)
            }
            return n
        }

        function n() {
            var e = navigator.userAgent.match(/Chrom(e|ium)\/([0-9]+)\./);
            if (!e) return !1;
            var n = parseInt(e[2], 10), t = navigator.connection;
            return n >= 55 && !!t && "cellular" === t.type && t.downlinkMax <= .115
        }

        function t(e) {
            return null == e ? void 0 : Math.round(1e3 * e) / 1e3
        }

        function u(e, n) {
            for (var t in e) {
                var r = e[t];
                void 0 !== n && ("number" == typeof r || "string" == typeof r ? n[t] = r : Array.isArray(r) && (n[t] = JSON.parse(JSON.stringify(r))))
            }
        }

        !function () {
            function s() {
                return g.timeOrigin
            }

            function f() {
                var e = document.referrer || "", n = w[w.length - 1];
                return x && B && n ? n.url : e
            }

            function d() {
                return navigator.webdriver
            }

            function l(e) {
                if ("function" == typeof g.getEntriesByType) {
                    var n = g.getEntriesByType("navigation"), t = {};
                    e.timingsV2 = {}, n && n[0] && (n[0].serverTiming && (t.serverTiming = n[0].serverTiming), n[0].nextHopProtocol && (t.nextHopProtocol = n[0].nextHopProtocol)), u(t, e.timingsV2)
                }
            }

            function p() {
                var n = g.getEntriesByType("navigation")[0], t = "";
                try {
                    t = "function" == typeof g.getEntriesByType ? new URL(null === n || void 0 === n ? void 0 : n.name).pathname : R ? new URL(R).pathname : window.location.pathname
                } catch (e) {
                }
                var r = {
                    referrer: document.referrer || "",
                    eventType: i.EventType.WebVitalsV2,
                    si: T ? T.si : 0,
                    versions: {js: "2022.10.1"},
                    pageloadId: h,
                    location: e(),
                    landingPath: t,
                    startTime: s(),
                    wd: d()
                };
                return T && (T.version && (r.versions.fl = T.version), T.icTag && (r.icTag = T.icTag), r.siteToken = T.token), A && ["lcp", "fid", "cls", "fcp", "ttfb", "inp"].forEach(function (e) {
                    r[e] = {value: -1, path: void 0}, A[e] && void 0 !== A[e].value && (r[e] = A[e])
                }), l(r), r
            }

            function v(r) {
                var o, a = g.timing, c = g.memory, p = r || e(), v = {
                    memory: {},
                    timings: {},
                    resources: [],
                    tempResources: [],
                    referrer: f(),
                    documentWriteIntervention: !1,
                    errorCount: 0,
                    eventType: i.EventType.Load,
                    firstPaint: 0,
                    firstContentfulPaint: 0,
                    si: T ? T.si : 0,
                    startTime: s(),
                    versions: {fl: T ? T.version : "", js: "2022.10.1", timings: 1},
                    pageloadId: h,
                    location: p,
                    wd: d()
                };
                if (void 0 == P) {
                    if ("function" == typeof g.getEntriesByType) {
                        var y = g.getEntriesByType("navigation");
                        y && Array.isArray(y) && y.length > 0 && (v.timingsV2 = {}, v.versions.timings = 2, delete v.timings, u(y[0], v.timingsV2))
                    }
                    1 === v.versions.timings && u(a, v.timings), u(c, v.memory)
                } else l(v);
                if (v.documentWriteIntervention = n(), v.firstPaint = m("first-paint"), v.firstContentfulPaint = m("first-contentful-paint"), v.errorCount = window.__cfErrCount || 0, T && (T.icTag && (v.icTag = T.icTag), v.siteToken = T.token), "function" == typeof g.getEntriesByType) {
                    var w = null !== (o = g.getEntriesByType("resource")) && void 0 !== o ? o : [], E = 0, S = 0;
                    w.forEach(function (e) {
                        var n = {
                            n: e.name,
                            s: t(e.startTime),
                            d: t(e.duration),
                            i: e.initiatorType,
                            p: e.nextHopProtocol,
                            rs: t(e.redirectStart),
                            re: t(e.redirectEnd),
                            fs: t(e.fetchStart),
                            ds: t(e.domainLookupStart),
                            de: t(e.domainLookupEnd),
                            cs: t(e.connectStart),
                            ce: t(e.connectEnd),
                            qs: t(e.requestStart),
                            ps: t(e.responseStart),
                            pe: t(e.responseEnd),
                            ws: t(e.workerStart),
                            ss: t(e.secureConnectionStart),
                            ts: e.transferSize,
                            ec: e.encodedBodySize,
                            dc: e.decodedBodySize
                        };
                        v.tempResources && void 0 === v.tempResources[S] && (v.tempResources[S] = []);
                        var r = JSON.stringify(n).length;
                        E + r < 62e3 && v.tempResources ? (E += r, v.tempResources[S].push(n)) : (S++, E = 0)
                    })
                }
                return JSON.stringify(v).length >= 64e3 && (v.resources = []), void 0 !== P && (delete v.timings, delete v.memory, delete v.errorCount, delete v.documentWriteIntervention), v
            }

            function m(e) {
                var n;
                if ("first-contentful-paint" === e && A.fcp && A.fcp.value) return A.fcp.value;
                if ("function" == typeof g.getEntriesByType) {
                    var t = null === (n = g.getEntriesByType("paint")) || void 0 === n ? void 0 : n.filter(function (n) {
                        return n.name === e
                    })[0];
                    return t ? t.startTime : 0
                }
                return 0
            }

            var g = window.performance || window.webkitPerformance || window.msPerformance || window.mozPerformance,
                y = document.currentScript || ("function" == typeof document.querySelector ? document.querySelector("script[data-cf-beacon]") : void 0),
                h = c(), w = [], T = window.__cfBeacon ? window.__cfBeacon : {};
            if (!T || "single" !== T.load) {
                if (y) {
                    var E = y.getAttribute("data-cf-beacon");
                    if (E) try {
                        T = r(r({}, T), JSON.parse(E))
                    } catch (e) {
                    } else {
                        var S = y.getAttribute("src");
                        if (S && "function" == typeof URLSearchParams) {
                            var b = new URLSearchParams(S.replace(/^[^\?]+\??/, "")), C = b.get("token");
                            C && (T.token = C);
                            var L = b.get("spa");
                            T.spa = null === L || "true" === L
                        }
                    }
                    T && "multi" !== T.load && (T.load = "single"), window.__cfBeacon = T
                }
                if (g && T && T.token) {
                    var P, R, B, O = !1, _ = 0;
                    document.addEventListener("visibilitychange", function () {
                        if ("hidden" === document.visibilityState) {
                            if (x && q()) {
                                var n = e();
                                (null === B || void 0 === B ? void 0 : B.url) == n && null !== B && void 0 !== B && B.triggered || M(), H(n)
                            }
                            !O && B && (O = !0, V())
                        } else "visible" === document.visibilityState && (_ = (new Date).getTime())
                    });
                    var A = {}, I = function (e) {
                        if (!e || 0 === e.length) return null;
                        var n = e.reduce(function (e, n) {
                            return e && e.value > n.value ? e : n
                        });
                        if (n && n.sources && n.sources.length) {
                            var t = n.sources.reduce(function (e, n) {
                                return e.node && e.previousRect.width * e.previousRect.height > n.previousRect.width * n.previousRect.height ? e : n
                            });
                            if (t) return t
                        }
                    }, F = function (e) {
                        return e && 0 !== e.length ? e[e.length - 1] : null
                    }, N = function (e) {
                        if (!e) return "";
                        var n = e.localName;
                        return e.id && e.id.length > 0 && (n += "#" + e.id), e.className && e.className.length > 0 && (n += "." + e.className.split(" ").join(".")), n
                    }, k = function (e) {
                        var n = window.location.pathname, t = F(e.entries);
                        switch (A[e.name.toLowerCase()] = {value: e.value, path: n}, e.name) {
                            case"CLS":
                                (t = I(e.entries)) && A.cls && (A.cls.element = N(t.node), A.cls.currentRect = t.currentRect, A.cls.previousRect = t.previousRect);
                                break;
                            case"FID":
                                t && A.fid && (A.fid.element = N(t.target), A.fid.name = t.name);
                                break;
                            case"LCP":
                                t && A.lcp && (A.lcp.element = N(t.element), A.lcp.size = t.size, A.lcp.url = t.url)
                        }
                    };
                    "function" == typeof PerformanceObserver && ((0, a.onLCP)(k), (0, a.onFID)(k), (0, a.onFCP)(k), (0, a.onINP)(k), (0, a.onTTFB)(k), PerformanceObserver.supportedEntryTypes && PerformanceObserver.supportedEntryTypes.includes("layout-shift") && (0, a.onCLS)(k));
                    var x = T && (void 0 === T.spa || !0 === T.spa),
                        j = T.send && T.send.to ? T.send.to : void 0 === T.version ? "https://cloudflareinsights.com/cdn-cgi/rum" : null,
                        M = function (e) {
                            var n = function (e, n) {
                                t.resources = e, 0 != n && (t.bypassTiming = !0), T && (1 === T.r && (t.resources = []), (0, o.sendObjectBeacon)("", t, function () {
                                }, !1, j), void 0 !== T.forward && void 0 !== T.forward.url && (0, o.sendObjectBeacon)("", t, function () {
                                }, !1, T.forward.url))
                            }, t = v(e);
                            if (t && T) {
                                var r = t.tempResources;
                                if (delete t.tempResources, x && r && 0 === r.length && n([], 0), !r) return;
                                r.forEach(function (e, t) {
                                    n(e, t)
                                })
                            }
                        }, V = function () {
                            var e = p();
                            x || (e.resources = [], delete e.tempResources), T && (0, o.sendObjectBeacon)("", e, function () {
                            }, !0, j)
                        }, D = function () {
                            var n = window.__cfRl && window.__cfRl.done || window.__cfQR && window.__cfQR.done;
                            n ? n.then(M) : M(), B = {id: h, url: e(), ts: (new Date).getTime(), triggered: !0}
                        };
                    "complete" === window.document.readyState ? D() : window.addEventListener("load", function () {
                        window.setTimeout(D)
                    });
                    var q = function () {
                        return x && 0 === w.filter(function (e) {
                            return e.id === h
                        }).length
                    }, H = function (e) {
                        w.push({id: h, url: e, ts: (new Date).getTime()}), w.length > 3 && w.shift()
                    };
                    x && (R = e(), function (n) {
                        var t = n.pushState;
                        if (t) {
                            var r = function () {
                                h = c(), "function" == typeof g.clearResourceTimings && g.clearResourceTimings(), _ = 0
                            };
                            n.pushState = function (i, o, a) {
                                P = e(a);
                                var c = e(), u = !0;
                                return P == c && (u = !1), u && (q() && ((null === B || void 0 === B ? void 0 : B.url) == c && null !== B && void 0 !== B && B.triggered || M(c), H(c)), r()), t.apply(n, [i, o, a])
                            }, window.addEventListener("popstate", function (n) {
                                q() && ((null === B || void 0 === B ? void 0 : B.url) == P && null !== B && void 0 !== B && B.triggered || M(P), H(P)), P = e(), r()
                            })
                        }
                    }(window.history))
                }
            }
        }()
    }()
}, function (e, n, t) {
    "use strict";
    n.__esModule = !0, n.EventType = void 0;
    !function (e) {
        e[e.Load = 1] = "Load", e[e.Additional = 2] = "Additional", e[e.WebVitalsV2 = 3] = "WebVitalsV2"
    }(n.EventType || (n.EventType = {}))
}, function (e, n, t) {
    "use strict";

    function r(e, n, t, r, i) {
        void 0 === r && (r = !1), void 0 === i && (i = null);
        var o = i || (n.siteToken && n.versions.fl ? "/cdn-cgi/rum?" + e : "/cdn-cgi/beacon/performance?" + e), a = !0;
        if (navigator && "string" == typeof navigator.userAgent) try {
            var c = navigator.userAgent.match(/Chrome\/([0-9]+)/);
            c && c[0].toLowerCase().indexOf("chrome") > -1 && parseInt(c[1]) < 81 && (a = !1)
        } catch (e) {
        }
        if (navigator && "function" == typeof navigator.sendBeacon && a && r) {
            n.st = 1;
            var u = JSON.stringify(n), s = {type: "application/json"};
            navigator.sendBeacon(o, new Blob([u], s))
        } else {
            n.st = 2;
            var u = JSON.stringify(n), f = new XMLHttpRequest;
            t && (f.onreadystatechange = function () {
                4 == this.readyState && 204 == this.status && t()
            }), f.open("POST", o, !0), f.setRequestHeader("content-type", "application/json"), f.send(u)
        }
    }

    n.__esModule = !0, n.sendObjectBeacon = void 0, n.sendObjectBeacon = r
}, function (e, n, t) {
    "use strict";
    n.__esModule = !0, n.onTTFB = n.onLCP = n.onINP = n.onFID = n.onFCP = n.onCLS = n.getTTFB = n.getLCP = n.getINP = n.getFID = n.getFCP = n.getCLS = void 0;
    var r, i, o, a, c, u = -1, s = function (e) {
        addEventListener("pageshow", function (n) {
            n.persisted && (u = n.timeStamp, e(n))
        }, !0)
    }, f = function () {
        return window.performance && performance.getEntriesByType && performance.getEntriesByType("navigation")[0]
    }, d = function () {
        var e = f();
        return e && e.activationStart || 0
    }, l = function (e, n) {
        var t = f(), r = "navigate";
        return u >= 0 ? r = "back-forward-cache" : t && (r = document.prerendering || d() > 0 ? "prerender" : t.type.replace(/_/g, "-")), {
            name: e,
            value: void 0 === n ? -1 : n,
            rating: "good",
            delta: 0,
            entries: [],
            id: "v3-".concat(Date.now(), "-").concat(Math.floor(8999999999999 * Math.random()) + 1e12),
            navigationType: r
        }
    }, p = function (e, n, t) {
        try {
            if (PerformanceObserver.supportedEntryTypes.includes(e)) {
                var r = new PerformanceObserver(function (e) {
                    n(e.getEntries())
                });
                return r.observe(Object.assign({type: e, buffered: !0}, t || {})), r
            }
        } catch (e) {
        }
    }, v = function (e, n) {
        var t = function t(r) {
            "pagehide" !== r.type && "hidden" !== document.visibilityState || (e(r), n && (removeEventListener("visibilitychange", t, !0), removeEventListener("pagehide", t, !0)))
        };
        addEventListener("visibilitychange", t, !0), addEventListener("pagehide", t, !0)
    }, m = function (e, n, t, r) {
        var i, o;
        return function (a) {
            n.value >= 0 && (a || r) && ((o = n.value - (i || 0)) || void 0 === i) && (i = n.value, n.delta = o, n.rating = function (e, n) {
                return e > n[1] ? "poor" : e > n[0] ? "needs-improvement" : "good"
            }(n.value, t), e(n))
        }
    }, g = -1, y = function () {
        return "hidden" !== document.visibilityState || document.prerendering ? 1 / 0 : 0
    }, h = function () {
        v(function (e) {
            var n = e.timeStamp;
            g = n
        }, !0)
    }, w = function () {
        return g < 0 && (g = y(), h(), s(function () {
            setTimeout(function () {
                g = y(), h()
            }, 0)
        })), {
            get firstHiddenTime() {
                return g
            }
        }
    }, T = function (e, n) {
        n = n || {};
        var t, r = [1800, 3e3], i = w(), o = l("FCP"), a = function (e) {
                e.forEach(function (e) {
                    "first-contentful-paint" === e.name && (u && u.disconnect(), e.startTime < i.firstHiddenTime && (o.value = e.startTime - d(), o.entries.push(e), t(!0)))
                })
            },
            c = window.performance && window.performance.getEntriesByName && window.performance.getEntriesByName("first-contentful-paint")[0],
            u = c ? null : p("paint", a);
        (c || u) && (t = m(e, o, r, n.reportAllChanges), c && a([c]), s(function (i) {
            o = l("FCP"), t = m(e, o, r, n.reportAllChanges), requestAnimationFrame(function () {
                requestAnimationFrame(function () {
                    o.value = performance.now() - i.timeStamp, t(!0)
                })
            })
        }))
    }, E = !1, S = -1, b = function (e, n) {
        n = n || {};
        var t = [.1, .25];
        E || (T(function (e) {
            S = e.value
        }), E = !0);
        var r, i = function (n) {
            S > -1 && e(n)
        }, o = l("CLS", 0), a = 0, c = [], u = function (e) {
            e.forEach(function (e) {
                if (!e.hadRecentInput) {
                    var n = c[0], t = c[c.length - 1];
                    a && e.startTime - t.startTime < 1e3 && e.startTime - n.startTime < 5e3 ? (a += e.value, c.push(e)) : (a = e.value, c = [e]), a > o.value && (o.value = a, o.entries = c, r())
                }
            })
        }, f = p("layout-shift", u);
        f && (r = m(i, o, t, n.reportAllChanges), v(function () {
            u(f.takeRecords()), r(!0)
        }), s(function () {
            a = 0, S = -1, o = l("CLS", 0), r = m(i, o, t, n.reportAllChanges)
        }))
    }, C = {passive: !0, capture: !0}, L = new Date, P = function (e, n) {
        r || (r = n, i = e, o = new Date, O(removeEventListener), R())
    }, R = function () {
        if (i >= 0 && i < o - L) {
            var e = {
                entryType: "first-input",
                name: r.type,
                target: r.target,
                cancelable: r.cancelable,
                startTime: r.timeStamp,
                processingStart: r.timeStamp + i
            };
            a.forEach(function (n) {
                n(e)
            }), a = []
        }
    }, B = function (e) {
        if (e.cancelable) {
            var n = (e.timeStamp > 1e12 ? new Date : performance.now()) - e.timeStamp;
            "pointerdown" == e.type ? function (e, n) {
                var t = function () {
                    P(e, n), i()
                }, r = function () {
                    i()
                }, i = function () {
                    removeEventListener("pointerup", t, C), removeEventListener("pointercancel", r, C)
                };
                addEventListener("pointerup", t, C), addEventListener("pointercancel", r, C)
            }(n, e) : P(n, e)
        }
    }, O = function (e) {
        ["mousedown", "keydown", "touchstart", "pointerdown"].forEach(function (n) {
            return e(n, B, C)
        })
    }, _ = function (e, n) {
        n = n || {};
        var t, o = [100, 300], c = w(), u = l("FID"), f = function (e) {
            e.startTime < c.firstHiddenTime && (u.value = e.processingStart - e.startTime, u.entries.push(e), t(!0))
        }, d = function (e) {
            e.forEach(f)
        }, g = p("first-input", d);
        t = m(e, u, o, n.reportAllChanges), g && v(function () {
            d(g.takeRecords()), g.disconnect()
        }, !0), g && s(function () {
            var c;
            u = l("FID"), t = m(e, u, o, n.reportAllChanges), a = [], i = -1, r = null, O(addEventListener), c = f, a.push(c), R()
        })
    }, A = 0, I = 1 / 0, F = 0, N = function (e) {
        e.forEach(function (e) {
            e.interactionId && (I = Math.min(I, e.interactionId), F = Math.max(F, e.interactionId), A = F ? (F - I) / 7 + 1 : 0)
        })
    }, k = function () {
        return c ? A : performance.interactionCount || 0
    }, x = function () {
        "interactionCount" in performance || c || (c = p("event", N, {
            type: "event",
            buffered: !0,
            durationThreshold: 0
        }))
    }, j = 0, M = function () {
        return k() - j
    }, V = [], D = {}, q = function (e) {
        var n = V[V.length - 1], t = D[e.interactionId];
        if (t || V.length < 10 || e.duration > n.latency) {
            if (t) t.entries.push(e), t.latency = Math.max(t.latency, e.duration); else {
                var r = {id: e.interactionId, latency: e.duration, entries: [e]};
                D[r.id] = r, V.push(r)
            }
            V.sort(function (e, n) {
                return n.latency - e.latency
            }), V.splice(10).forEach(function (e) {
                delete D[e.id]
            })
        }
    }, H = function (e, n) {
        n = n || {};
        var t = [200, 500];
        x();
        var r, i = l("INP"), o = function (e) {
            e.forEach(function (e) {
                e.interactionId && q(e), "first-input" === e.entryType && !V.some(function (n) {
                    return n.entries.some(function (n) {
                        return e.duration === n.duration && e.startTime === n.startTime
                    })
                }) && q(e)
            });
            var n, t = (n = Math.min(V.length - 1, Math.floor(M() / 50)), V[n]);
            t && t.latency !== i.value && (i.value = t.latency, i.entries = t.entries, r())
        }, a = p("event", o, {durationThreshold: n.durationThreshold || 40});
        r = m(e, i, t, n.reportAllChanges), a && (a.observe({type: "first-input", buffered: !0}), v(function () {
            o(a.takeRecords()), i.value < 0 && M() > 0 && (i.value = 0, i.entries = []), r(!0)
        }), s(function () {
            V = [], j = k(), i = l("INP"), r = m(e, i, t, n.reportAllChanges)
        }))
    }, J = {}, z = function (e, n) {
        n = n || {};
        var t, r = [2500, 4e3], i = w(), o = l("LCP"), a = function (e) {
            var n = e[e.length - 1];
            if (n) {
                var r = n.startTime - d();
                r < i.firstHiddenTime && (o.value = r, o.entries = [n], t())
            }
        }, c = p("largest-contentful-paint", a);
        if (c) {
            t = m(e, o, r, n.reportAllChanges);
            var u = function () {
                J[o.id] || (a(c.takeRecords()), c.disconnect(), J[o.id] = !0, t(!0))
            };
            ["keydown", "click"].forEach(function (e) {
                addEventListener(e, u, {once: !0, capture: !0})
            }), v(u, !0), s(function (i) {
                o = l("LCP"), t = m(e, o, r, n.reportAllChanges), requestAnimationFrame(function () {
                    requestAnimationFrame(function () {
                        o.value = performance.now() - i.timeStamp, J[o.id] = !0, t(!0)
                    })
                })
            })
        }
    }, U = function e(n) {
        document.prerendering ? addEventListener("prerenderingchange", function () {
            return e(n)
        }, !0) : "complete" !== document.readyState ? addEventListener("load", function () {
            return e(n)
        }, !0) : setTimeout(n, 0)
    }, W = function (e, n) {
        n = n || {};
        var t = [800, 1800], r = l("TTFB"), i = m(e, r, t, n.reportAllChanges);
        U(function () {
            var o = f();
            if (o) {
                if (r.value = Math.max(o.responseStart - d(), 0), r.value < 0 || r.value > performance.now()) return;
                r.entries = [o], i(!0), s(function () {
                    r = l("TTFB", 0), (i = m(e, r, t, n.reportAllChanges))(!0)
                })
            }
        })
    };
    n.getFCP = T, n.onFCP = T, n.getCLS = b, n.onCLS = b, n.getFID = _, n.onFID = _, n.getINP = H, n.onINP = H, n.getLCP = z, n.onLCP = z, n.getTTFB = W, n.onTTFB = W
}, function (e, n, t) {
    "use strict";

    function r(e, n, t) {
        var r = n && t || 0;
        "string" == typeof e && (n = "binary" === e ? new Array(16) : null, e = null), e = e || {};
        var a = e.random || (e.rng || i)();
        if (a[6] = 15 & a[6] | 64, a[8] = 63 & a[8] | 128, n) for (var c = 0; c < 16; ++c) n[r + c] = a[c];
        return n || o(a)
    }

    var i = t(5), o = t(6);
    e.exports = r
}, function (e, n, t) {
    "use strict";
    var r = "undefined" != typeof crypto && crypto.getRandomValues && crypto.getRandomValues.bind(crypto) || "undefined" != typeof msCrypto && "function" == typeof window.msCrypto.getRandomValues && msCrypto.getRandomValues.bind(msCrypto);
    if (r) {
        var i = new Uint8Array(16);
        e.exports = function () {
            return r(i), i
        }
    } else {
        var o = new Array(16);
        e.exports = function () {
            for (var e, n = 0; n < 16; n++) 0 == (3 & n) && (e = 4294967296 * Math.random()), o[n] = e >>> ((3 & n) << 3) & 255;
            return o
        }
    }
}, function (e, n, t) {
    "use strict";

    function r(e, n) {
        var t = n || 0, r = i;
        return [r[e[t++]], r[e[t++]], r[e[t++]], r[e[t++]], "-", r[e[t++]], r[e[t++]], "-", r[e[t++]], r[e[t++]], "-", r[e[t++]], r[e[t++]], "-", r[e[t++]], r[e[t++]], r[e[t++]], r[e[t++]], r[e[t++]], r[e[t++]]].join("")
    }

    for (var i = [], o = 0; o < 256; ++o) i[o] = (o + 256).toString(16).substr(1);
    e.exports = r
}]);
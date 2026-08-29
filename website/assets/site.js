/* OnyxAutomate — page behaviour. No dependencies. */
(function () {
  "use strict";

  var reduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ---- current year ---------------------------------------------------- */
  var yr = document.getElementById("yr");
  if (yr) yr.textContent = String(new Date().getFullYear());

  /* ---- mobile menu ----------------------------------------------------- */
  var toggle = document.querySelector(".nav__toggle");
  var links = document.getElementById("navlinks");

  function isCompact() {
    return window.matchMedia("(max-width: 940px)").matches;
  }
  function setMenu(open) {
    if (!links || !toggle) return;
    links.hidden = !open;
    toggle.setAttribute("aria-expanded", String(open));
    toggle.textContent = open ? "Close" : "Menu";
  }
  function syncMenu() {
    if (!links) return;
    if (isCompact()) {
      if (toggle.getAttribute("aria-expanded") !== "true") setMenu(false);
    } else {
      links.hidden = false;
    }
  }
  if (toggle && links) {
    toggle.addEventListener("click", function () {
      setMenu(links.hidden);
    });
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A" && isCompact()) setMenu(false);
    });
    window.addEventListener("resize", syncMenu);
    syncMenu();
  }

  /* ---- hero log: one orchestrated reveal on load ------------------------ */
  var rows = Array.prototype.slice.call(
    document.querySelectorAll("#logbody .log__row")
  );
  if (reduced) {
    rows.forEach(function (r) { r.classList.add("lit"); });
  } else {
    rows.forEach(function (row, i) {
      window.setTimeout(function () { row.classList.add("lit"); }, 380 + i * 140);
    });
  }

  /* ---- scroll reveal --------------------------------------------------- */
  var reveals = Array.prototype.slice.call(document.querySelectorAll(".rv"));
  if (reduced || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("in"); });
  } else {
    var ro = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (!entry.isIntersecting) return;
          entry.target.classList.add("in");
          ro.unobserve(entry.target);
        });
      },
      { rootMargin: "0px 0px -12% 0px", threshold: 0.08 }
    );
    reveals.forEach(function (el) { ro.observe(el); });
  }

  /* ---- gauge: mark the section currently in view ------------------------ */
  var marks = Array.prototype.slice.call(document.querySelectorAll(".gauge a"));
  var sections = marks
    .map(function (a) { return document.getElementById(a.dataset.g); })
    .filter(Boolean);

  if (sections.length && "IntersectionObserver" in window) {
    var visible = Object.create(null);
    var so = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          visible[entry.target.id] = entry.isIntersecting
            ? entry.intersectionRatio
            : 0;
        });
        var best = "";
        var bestRatio = 0;
        sections.forEach(function (s) {
          var r = visible[s.id] || 0;
          if (r > bestRatio) { bestRatio = r; best = s.id; }
        });
        marks.forEach(function (a) {
          a.classList.toggle("on", a.dataset.g === best);
        });
      },
      { threshold: [0, 0.15, 0.35, 0.6, 0.85] }
    );
    sections.forEach(function (s) { so.observe(s); });
  }

  /* Tell the head-script failsafe that everything wired up successfully. */
  window.__onyxReady = true;
})();

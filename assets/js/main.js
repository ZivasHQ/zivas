(function () {
  'use strict';
  var EMAIL = 'olaniyanolaonipekun321@gmail.com';
  var WHATSAPP = '2348106265136';
  var $ = function (s, c) { return (c || document).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || document).querySelectorAll(s)); };

  /* current page link */
  var here = location.pathname.split('/').pop() || 'index.html';
  $$('.nav a, .menu a').forEach(function (a) {
    if (a.getAttribute('href') === here) {
      a.setAttribute('aria-current', 'page');
      var dd = a.closest('.has-dd');
      if (dd) $('button.dd', dd).style.boxShadow = '0 2px 0 #0f8ba8';
    }
  });

  /* mobile menu */
  var burger = $('.burger'), nav = $('#nav');
  if (burger) burger.addEventListener('click', function () {
    var open = nav.classList.toggle('open');
    burger.setAttribute('aria-expanded', open);
  });

  /* solutions dropdown */
  $$('.has-dd').forEach(function (dd) {
    var btn = $('button.dd', dd);
    function set(o) { dd.classList.toggle('open', o); btn.setAttribute('aria-expanded', o); }
    btn.addEventListener('click', function (e) { e.stopPropagation(); set(!dd.classList.contains('open')); });
    document.addEventListener('click', function (e) { if (!dd.contains(e.target)) set(false); });
    dd.addEventListener('keydown', function (e) { if (e.key === 'Escape') { set(false); btn.focus(); } });
  });

  /* FAQ accordion */
  $$('.faq button').forEach(function (b) {
    b.addEventListener('click', function () {
      var open = b.getAttribute('aria-expanded') === 'true';
      b.setAttribute('aria-expanded', !open);
      document.getElementById(b.getAttribute('aria-controls')).hidden = open;
    });
  });

  /* tabs */
  $$('[role=tablist]').forEach(function (list) {
    var tabs = $$('[role=tab]', list);
    function pick(t) {
      tabs.forEach(function (x) {
        var on = x === t;
        x.setAttribute('aria-selected', on);
        x.tabIndex = on ? 0 : -1;
        document.getElementById(x.getAttribute('aria-controls')).hidden = !on;
      });
    }
    tabs.forEach(function (t, i) {
      t.addEventListener('click', function () { pick(t); });
      t.addEventListener('keydown', function (e) {
        var n = e.key === 'ArrowRight' ? i + 1 : e.key === 'ArrowLeft' ? i - 1 : null;
        if (n === null) return;
        var next = tabs[(n + tabs.length) % tabs.length];
        pick(next); next.focus();
      });
    });
  });

  /* plan finder (limits match the live plans) */
  var finder = $('#finder');
  if (finder) {
    var out = $('#finder-result');
    var plans = [
      { name: 'Free', price: '\u20a60', per: 'per month', c: 20, s: 100, l: 10 },
      { name: 'Standard', price: '\u20a620,000', per: 'per month', c: 100, s: 500, l: 50 },
      { name: 'Enterprise', price: '\u20a6240,000', per: 'per year', c: 1000, s: 50000, l: 5000 }
    ];
    finder.addEventListener('submit', function (e) {
      e.preventDefault();
      var c = +finder.courses.value || 0, s = +finder.students.value || 0, l = +finder.lecturers.value || 0;
      var plan = plans.filter(function (p) { return c <= p.c && s <= p.s && l <= p.l; })[0];
      if (plan) {
        out.innerHTML = '<strong>' + plan.name + '</strong> fits: ' + plan.price + ' ' + plan.per + '. Limits: ' +
          plan.c + ' courses, ' + plan.s.toLocaleString() + ' students, ' + plan.l.toLocaleString() + ' lecturers. ' +
          '<a href="book-demo.html">Book a demo</a>';
      } else {
        out.innerHTML = 'That is beyond the Enterprise limits. <a href="book-demo.html">Talk to us</a> and we will size a plan for you.';
      }
    });
  }

  /* demo form: opens an email draft with the message preloaded */
  var form = $('#demo-form');
  if (form) {
    var params = new URLSearchParams(location.search);
    if (params.get('plan') && form.plan) form.plan.value = params.get('plan');

    function body() {
      var v = function (n) { return (form[n].value || '').trim() || 'Not provided'; };
      return [
        'Hello Zivas team,', '',
        'I would like to book a demo.', '',
        'Name: ' + v('name'), 'Email: ' + v('email'), 'Organisation: ' + v('org'),
        'I am a: ' + v('role'), 'Approx. number of students: ' + v('size'),
        'Plan of interest: ' + v('plan'), 'Preferred date and time: ' + v('when'), '',
        'Message:', v('msg'), '', 'Thank you.'
      ].join('\n');
    }
    function validate() {
      var ok = true;
      ['name', 'email', 'role'].forEach(function (n) {
        var f = form[n], e = document.getElementById(n + '-err'), bad = !f.value.trim();
        if (n === 'email' && !bad) bad = !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.value.trim());
        f.setAttribute('aria-invalid', bad);
        e.textContent = bad ? (n === 'email' ? 'Enter a valid email address.' : n === 'name' ? 'Enter your name.' : 'Choose the option that fits you best.') : '';
        if (bad && ok) { f.focus(); ok = false; }
      });
      return ok;
    }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      if (!validate()) return;
      var subject = 'Zivas demo request - ' + (form.org.value.trim() || form.name.value.trim());
      location.href = 'mailto:' + EMAIL + '?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body());
      $('#sent').hidden = false;
    });
    $('#wa').addEventListener('click', function (e) {
      e.preventDefault();
      if (!validate()) return;
      window.open('https://wa.me/' + WHATSAPP + '?text=' + encodeURIComponent(body()), '_blank', 'noopener');
    });
  }

  $$('.yr').forEach(function (n) { n.textContent = new Date().getFullYear(); });
})();

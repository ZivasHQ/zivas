#!/usr/bin/env python3
"""Regenerates every .html page from the content below.
Edit text here, run `python3 build.py`, and upload the folder. Plain static output, no dependencies."""
import os
OUT = os.path.dirname(os.path.abspath(__file__))
BASE = 'https://zivashq.github.io/zivas_corporate_website/'
EMAIL = 'olaniyanolaonipekun321@gmail.com'
WA = '2348106265136'
DEMO = 'book-demo.html'

def head(title, desc, page):
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta property="og:title" content="{title}"><meta property="og:description" content="{desc}">
<meta property="og:type" content="website"><meta property="og:url" content="{BASE}{page}">
<meta property="og:image" content="{BASE}assets/img/shot-dashboard.png"><meta name="theme-color" content="#0a1730">
<link rel="canonical" href="{BASE}{page}">
<link rel="icon" href="assets/img/favicon.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700&family=Instrument+Sans:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="hdr"><div class="wrap">
<a class="logo" href="index.html" aria-label="Zivas home"><img src="assets/img/logo.png" alt="Zivas"></a>
<button class="burger" aria-label="Menu" aria-expanded="false" aria-controls="nav"><span></span><span></span><span></span></button>
<nav class="nav" id="nav" aria-label="Main">
<a href="features.html">Features</a><a href="how-it-works.html">How it works</a>
<div class="has-dd"><button class="dd" aria-expanded="false" aria-haspopup="true">Solutions &#9662;</button>
<div class="menu"><a href="lecturers.html">For lecturers</a><a href="students.html">For students</a><a href="institutions.html">For institutions</a></div></div>
<a href="pricing.html">Pricing</a><a href="about.html">About</a>
<a class="btn sm" href="{DEMO}">Book a demo</a>
</nav></div></header>
<main id="main">
'''

FOOT = f'''</main>
<footer class="ftr"><div class="wrap">
<div class="grid">
<div><img src="assets/img/logo-light.png" alt="Zivas"><p>The classroom companion that takes work off teachers instead of adding to it.</p>
<p><a href="mailto:{EMAIL}">{EMAIL}</a><br><a href="https://wa.me/{WA}">WhatsApp +{WA[:3]} {WA[3:6]} {WA[6:9]} {WA[9:]}</a><br>Remote-first team</p></div>
<div><h4>Product</h4><ul><li><a href="features.html">Features</a></li><li><a href="how-it-works.html">How it works</a></li><li><a href="pricing.html">Pricing</a></li></ul></div>
<div><h4>Solutions</h4><ul><li><a href="lecturers.html">For lecturers</a></li><li><a href="students.html">For students</a></li><li><a href="institutions.html">For institutions</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="about.html">About</a></li><li><a href="faq.html">FAQ</a></li><li><a href="{DEMO}">Book a demo</a></li><li><a href="privacy.html">Privacy</a></li><li><a href="terms.html">Terms</a></li></ul></div>
</div>
<div class="legal"><span>&copy; <span class="yr">2026</span> Zivas. All rights reserved.</span><span>zivashq.github.io</span></div>
</div></footer>
<script src="assets/js/main.js"></script>
</body></html>'''

def cta(h='See Zivas on your own course', p='Book a demo and we will walk you through it with your real teaching load in mind.'):
    return f'''<section class="sec dark"><div class="wrap"><h2>{h}</h2><p class="lead">{p}</p>
<div class="cta-row"><a class="btn teal" href="{DEMO}">Book a demo</a><a class="btn ghost" style="color:#fff;border-color:#5b6c96" href="pricing.html">See pricing</a></div></div></section>'''

def pagehead(h, p):
    return f'<section class="pagehead"><div class="wrap"><h1>{h}</h1><p class="lead">{p}</p><div class="cta-row"><a class="btn" href="{DEMO}">Book a demo</a></div></div></section>'

def img(n, alt, cls='shot full'):
    return f'<img class="{cls}" src="assets/img/shot-{n}.png" alt="{alt}" width="1366" height="681" loading="lazy">'

def split(h, p, n, alt, rev=False, extra=''):
    return f'<div class="split{" rev" if rev else ""}"><div><h2>{h}</h2>{p}{extra}</div><div>{img(n, alt)}</div></div>'

def rows(items):
    return '<div class="rows">' + ''.join(f'<div><h3>{t}</h3><p>{d}</p></div>' for t, d in items) + '</div>'

def faq_items(items, pre='q'):
    s = '<div class="faq">'
    for i, (q, a) in enumerate(items):
        s += f'<h3><button aria-expanded="false" aria-controls="{pre}{i}">{q}</button></h3><div class="ans" id="{pre}{i}" hidden><p>{a}</p></div>'
    return s + '</div>'

FAQ = [
 ('Is Zivas a learning management system?', 'Not in the traditional sense. Zivas covers the work around teaching: weekly course structure, assignments, attendance, quizzes, progress tracking and notifications. It leaves out the administrative layers that make older LMS tools heavy to learn and slow to use.'),
 ('Who is Zivas for?', 'Independent tutors, lecturers at universities and colleges, and the institutions that employ them. Students use it to see coursework, submit work and follow their own progress.'),
 ('What does it cost?', 'There is a free plan, a Standard plan at \u20a620,000 per month and an Enterprise plan at \u20a6240,000 per year. See the <a href="pricing.html">pricing page</a> for limits.'),
 ('Do lecturers at an institution have to pay?', 'No. When a lecturer is tied to an institution, the institution\u2019s plan covers them and they do not pay individually.'),
 ('Who pays for AI grading?', 'AI grading is not live yet. When it launches, it will be paid for by individual tutors; lecturers tied to an institution are covered by their institution\u2019s plan. Exact terms will be published before launch.'),
 ('Which features are available today?', 'Everything described on the <a href="features.html">features page</a> is live, except AI grading, which is coming soon.'),
 ('How does attendance work?', 'The lecturer starts a live session and shows a QR code. Students scan it on their phones. A six-digit fallback code is available for any student who cannot scan.'),
 ('Can I export student scores?', 'Yes. Lecturers can download scores as an Excel file from the course page.'),
 ('How do I book a demo?', 'Use the <a href="book-demo.html">demo form</a>. It opens an email draft addressed to our team with your details already filled in, or you can send the same message on WhatsApp.'),
 ('Where is the team based?', 'We are a remote-first team.'),
 ('How does a school add its lecturers and students?', 'The school admin dashboard lets an administrator create accounts inside the school\u2019s workspace with a temporary password, and organise people into departments and courses. See <a href="institutions.html">For institutions</a>.'),
 ('How do schools pay?', 'Schools pick Standard or Enterprise in the school admin dashboard and pay online in naira. Every payment appears in the dashboard\u2019s payment history. The Zivas team approves Enterprise before you can pay for it.'),
]

PAGES = {}

PAGES['index.html'] = ('Zivas | Classroom work, handled', 'Zivas takes assignments, attendance, quizzes and progress tracking off teachers\u2019 plates, without the weight of a traditional LMS.', f'''
<section class="hero"><div class="wrap">
<div class="copy"><h1>Teach the class. Zivas handles the rest.</h1>
<p class="lead">Assignments, attendance, quizzes and progress tracking, set up once and running every week, without the weight of a traditional LMS.</p>
<div class="cta-row"><a class="btn" href="{DEMO}">Book a demo</a><a class="btn ghost" href="features.html">Explore features</a></div></div>
<div class="bleed"><img class="shot" src="assets/img/shot-dashboard.png" alt="A Zivas course page with week-by-week navigation" width="1366" height="681"></div>
</div></section>

<section class="sec"><div class="wrap split">
<div><h2>Most LMS software was built to manage institutions. Zivas was built to lighten the lecturer\u2019s week.</h2>
<p class="lead">Teachers do not need forty menus. They need coursework out on time, attendance taken in seconds and a clear view of who is falling behind.</p></div>
<div class="scroll"><table class="tbl"><thead><tr><th></th><th>Typical LMS</th><th class="hl">Zivas</th></tr></thead><tbody>
<tr><th>Course setup</th><td>Many screens before a first lesson</td><td class="hl">Guided sign-up, then a week-by-week course</td></tr>
<tr><th>Attendance</th><td>Paper or separate spreadsheets</td><td class="hl">One QR scan</td></tr>
<tr><th>Quizzes</th><td>Extra tools and logins</td><td class="hl">Built into the course</td></tr>
<tr><th>Student progress</th><td>Export and calculate by hand</td><td class="hl">Live charts, streaks and Excel export</td></tr>
</tbody></table></div></div></section>

<section class="sec tint"><div class="wrap">
<h2>What Zivas takes off your plate</h2>
{rows([
('Course by week','Assignments, resources, students, quizzes, discussion and analytics for every week, in one view.'),
('Assignments and grading','Publish coursework, collect submissions on time or late, grade and release scores. Students are notified immediately.'),
('Attendance','Show a QR code in class. Students scan to check in; a fallback code covers everyone else.'),
('Quizzes and polls','Run low-stakes quizzes and polls during a lecture. Students join from their course page.'),
('Student insight','Scores, submissions, attendance and on-time streaks for each student, with Excel export.'),
('Notifications','Grades, updates and attendance reach students the moment they change.')])}
<p style="margin-top:28px"><a href="features.html">See every feature</a></p></div></section>

<section class="sec"><div class="wrap" style="display:grid;gap:96px">
{split('Attendance in one scan','<p class="lead">Start a live session, display the code and let students check in from their phones. Every check-in lands in the student\u2019s record automatically.</p>','attendance','Zivas QR attendance screen with a live session code')}
{split('Check understanding while you teach','<p class="lead">Build a quiz or poll once, attach it to a week and go live when you are ready. Results appear as students answer.</p>','quiz','Zivas quizzes and polls list for a course',rev=True)}
{split('Run the whole school from one dashboard','<p class="lead">School admins add lecturers and students, organise departments and courses, and manage the school\u2019s plan.</p><p><a href="institutions.html">See the school admin dashboard</a></p>','school-departments','School admin dashboard showing departments')}
</div></section>

<section class="sec tint"><div class="wrap"><h2>Built for every seat in the classroom</h2>
<div class="cols3" style="margin-top:32px">
<div><h3>Lecturers</h3><p>Spend less time on administration and more on teaching.</p><a href="lecturers.html">For lecturers</a></div>
<div><h3>Students</h3><p>See what is due, how you are doing and what to improve.</p><a href="students.html">For students</a></div>
<div><h3>Institutions</h3><p>Add your lecturers and students, organise courses and manage one plan for the whole school.</p><a href="institutions.html">For institutions</a></div>
</div></div></section>

<section class="sec"><div class="wrap"><h2>Simple pricing in naira</h2>
<p class="lead">Start free. Move up when your classes grow.</p>
<div class="cols3" style="margin-top:28px">
<div><h3>Free</h3><span class="price">\u20a60 <small>per month</small></span><p>Up to 20 courses and 100 students.</p></div>
<div><h3>Standard</h3><span class="price">\u20a620,000 <small>per month</small></span><p>Up to 100 courses and 500 students.</p></div>
<div><h3>Enterprise</h3><span class="price">\u20a6240,000 <small>per year</small></span><p>Up to 1,000 courses and 50,000 students.</p></div>
</div><p style="margin-top:28px"><a href="pricing.html">Compare plans in full</a></p></div></section>
{cta()}''')

PAGES['features.html'] = ('Features | Zivas', 'Weekly courses, assignments, QR attendance, quizzes and polls, student insight and notifications. Everything a lecturer needs and nothing they do not.', f'''
{pagehead('Everything a lecturer needs, nothing they do not','Zivas covers the weekly rhythm of teaching. Every feature below is live today unless it says coming soon.')}
<section class="sec"><div class="wrap"><h2>For lecturers</h2>
{rows([
('Week-by-week courses','Every course is laid out by week. Switch weeks and see that week\u2019s assignments, resources and activity.'),
('Assignments','Publish coursework for a given week, collect submissions, flag late work and grade with a score out of the total.'),
('Resources','Keep learning materials with the week they belong to.'),
('Quizzes and polls','Create quizzes and polls, attach them to a week and take them live in class.'),
('QR attendance','Start a live session and show a QR code. Students scan to check in; a fallback code is always available.'),
('Student insight','Open any student to see average score, submissions, late work, attendance and on-time streak.'),
('Excel export','Download course scores as an Excel file in one click.'),
('Discussion','A discussion space for each course so questions stay with the class.'),
('Notifications','Grade changes and class updates are delivered to students automatically.')])}
</div></section>
<section class="sec tint"><div class="wrap">
{split('Know every student at a glance','<p class="lead">Scores, submissions, attendance and streaks sit on one screen, so you can spot who needs help before the exam.</p>','insight','Student profile showing average score, submissions, attendance and weekly trend')}
</div></section>
<section class="sec"><div class="wrap"><h2>For students</h2>
{rows([
('My courses','Join a class and see all your courses with the current week.'),
('Weekly view','See assignments week by week and submit work in the same place.'),
('Progress and targets','Set a target grade and see how far you are from it as scores are published.'),
('Performance charts','Weekly averages, on-time streak and attendance rate, with a clear change from last week.'),
('Notifications','Every published or updated grade arrives as a notification you can review later.')])}
</div></section>
<section class="sec tint"><div class="wrap"><h2>For school administrators</h2>
{rows([
('Accounts for everyone','Create student and lecturer accounts in your school\u2019s workspace and manage them later.'),
('Departments and courses','Organise departments, then create courses and assign them to lecturers.'),
('School settings','Maintain your school profile, academic year and timezone.'),
('Plan and payments','Renew your plan online and review your payment history.')])}
<p style="margin-top:24px"><a href="institutions.html">More for institutions</a></p></div></section>
<section class="sec"><div class="wrap"><h2>Coming soon</h2>
{rows([('AI grading','AI-assisted grading to cut marking time further. It is not live yet. Terms and plan availability will be confirmed before launch.')])}
</div></section>
{cta()}''')

PAGES['how-it-works.html'] = ('How it works | Zivas', 'From sign-up to first graded assignment: how lecturers and students use Zivas.', f'''
{pagehead('From sign-up to graded work, without the setup project','Zivas is designed so a lecturer can go from nothing to a running course in one sitting.')}
<section class="sec"><div class="wrap">
<div class="tabs" role="tablist" aria-label="Choose a role">
<button role="tab" id="t1" aria-selected="true" aria-controls="p1">As a lecturer</button>
<button role="tab" id="t2" aria-selected="false" aria-controls="p2" tabindex="-1">As a student</button>
<button role="tab" id="t3" aria-selected="false" aria-controls="p3" tabindex="-1">As a school admin</button></div>
<div role="tabpanel" id="p1" aria-labelledby="t1"><ol class="steps">
<li><div><h3>Create your account</h3><p>Choose lecturer, then whether you teach independently or through an institution. Registration takes four short steps.</p></div></li>
<li><div><h3>Build your course</h3><p>Add a course and its weeks. Each week gets its own assignments, resources and quizzes.</p></div></li>
<li><div><h3>Invite students</h3><p>Students join your class from their own portal.</p></div></li>
<li><div><h3>Teach and collect</h3><p>Take attendance with a QR code, run a live quiz and publish assignments.</p></div></li>
<li><div><h3>Grade and review</h3><p>Release scores, watch class trends and export results to Excel.</p></div></li></ol></div>
<div role="tabpanel" id="p2" aria-labelledby="t2" hidden><ol class="steps">
<li><div><h3>Create your account</h3><p>Choose the student portal and add your details.</p></div></li>
<li><div><h3>Join a class</h3><p>Join your lecturer\u2019s course and see it under My Courses.</p></div></li>
<li><div><h3>Follow the week</h3><p>See what is due, join live quizzes and scan the attendance code in class.</p></div></li>
<li><div><h3>Submit your work</h3><p>Hand in assignments before the deadline.</p></div></li>
<li><div><h3>Track your progress</h3><p>Set a target grade and watch your average, streak and attendance change week by week.</p></div></li></ol></div>
<div role="tabpanel" id="p3" aria-labelledby="t3" hidden><ol class="steps">
<li><div><h3>Set up your school</h3><p>Add your school\u2019s name, contact details, academic year and timezone.</p></div></li>
<li><div><h3>Add departments</h3><p>Create departments with codes so everything stays organised.</p></div></li>
<li><div><h3>Add lecturers and students</h3><p>Create accounts in your school\u2019s workspace with temporary passwords. They sign in and get to work.</p></div></li>
<li><div><h3>Create courses</h3><p>Choose the lecturer, department, start date and number of weeks for each course.</p></div></li>
<li><div><h3>Manage your plan</h3><p>Renew Standard online, or request Enterprise. The Zivas team approves Enterprise before you pay.</p></div></li></ol></div>
</div></section>
<section class="sec tint"><div class="wrap">
{split('One course page, every week','<p class="lead">Weeks run along the top. Assignments, resources, students, quizzes, discussion and analytics sit one click away.</p>','dashboard','Zivas lecturer course page with weeks W1 to W15')}</div></section>
{cta()}''')

def audience(title, h, lead, items, n, alt, tail=''):
    return (title, lead, f'''{pagehead(h, lead)}
<section class="sec"><div class="wrap">{rows(items)}{tail}</div></section>
<section class="sec tint"><div class="wrap">{img(n, alt)}</div></section>{cta()}''')

PAGES['lecturers.html'] = audience('For lecturers | Zivas', 'Spend your week teaching, not administering', 'Zivas handles the repetitive parts of running a class so your time goes to students.', [
 ('Less admin','Attendance, quizzes and coursework live in one place instead of four.'),
 ('Always know who is behind','Per-student scores, late work and attendance are one click away.'),
 ('Marking help is coming','AI-assisted grading is on the way for lecturers who want to mark faster.'),
 ('Added by your school','If you teach at an institution, your school admin can create your account and assign your courses.'),
 ('Free if your institution is on Zivas','Lecturers tied to an institution do not pay; the institution\u2019s plan covers them.')], 'lecturer-home', 'Zivas lecturer dashboard')
PAGES['students.html'] = audience('For students | Zivas', 'Know where you stand, every week', 'Zivas gives students a clear picture of coursework, grades and attendance.', [
 ('Your courses in one list','Join a class and see everything due this week.'),
 ('Target grades','Set a goal and see how many points you are above or below it.'),
 ('Progress you can read','Weekly performance charts, on-time streak and attendance rate.'),
 ('Joined through your school','If your school uses Zivas, your admin can create your account in the school\u2019s workspace.'),
 ('Never miss an update','Notifications arrive when grades are published or changed.')], 'progress', 'Zivas student progress page with weekly performance chart')
PAGES['institutions.html'] = ('For institutions | Zivas', 'The Zivas school admin dashboard: add lecturers and students, organise departments and courses, and manage your plan and payments in one place.', f'''
{pagehead('Run your whole school from one dashboard','Add lecturers and students, organise departments and courses, and manage your plan. Everyone you add gets the same lightweight tools.')}
<section class="sec"><div class="wrap">{rows([
('Students and lecturers','Create accounts inside your school\u2019s workspace with a temporary password, then edit or remove people as they join and leave.'),
('Departments','Set up departments with a name, code and status, then keep courses and people organised under them.'),
('Courses','Create a course with its title, code, lecturer, department, start date and length in weeks, and switch it on when it is ready.'),
('School settings','Keep your school\u2019s name, contact email, address, phone, website, academic year and timezone up to date.'),
('Plan and payments','See your current plan and subscription status, renew online and review every payment you have made.'),
('Lecturers do not pay individually','Lecturers tied to your school are covered by your school\u2019s plan.')])}</div></section>
<section class="sec tint"><div class="wrap" style="display:grid;gap:96px">
{split('Departments, ready in minutes','<p class="lead">Add a department once and use it everywhere: when you create students, assign lecturers and set up courses.</p>','school-departments','School admin departments page with an add department form and a table of departments')}
{split('Courses with the right lecturer','<p class="lead">Pick the lecturer and department, set the start date and number of weeks, and the course appears in that lecturer\u2019s dashboard.</p>','school-courses','School admin create course form',rev=True)}
{split('One place for your school profile','<p class="lead">Your workspace, current plan and subscription status sit alongside your school details, so nothing is scattered.</p>','school-settings','School settings page showing workspace, current plan and subscription status')}
</div></section>
<section class="sec"><div class="wrap split"><div><h2>Plans for schools</h2><p class="lead">Schools choose Standard or Enterprise from the dashboard and pay online in naira.</p>
<p>Standard is \u20a620,000 per month. Enterprise is \u20a6240,000 per year and includes AI grading when it launches. The Zivas team approves Enterprise before you can pay for it.</p>
<div class="cta-row"><a class="btn" href="book-demo.html?plan=Enterprise">Talk to us about Enterprise</a><a class="btn ghost" href="pricing.html">Compare plans</a></div></div>
<div>{img('school-plans','School admin plans page showing Standard and Enterprise')}</div></div></section>
{cta()}''')

PAGES['pricing.html'] = ('Pricing | Zivas', 'Zivas plans in naira: Free, Standard at \u20a620,000 per month and Enterprise at \u20a6240,000 per year.', f'''
{pagehead('Simple pricing in naira','Start free. Move up when your classes outgrow the limits.')}
<section class="sec"><div class="wrap"><div class="scroll"><table class="tbl">
<thead><tr><th></th><th>Free</th><th class="hl">Standard</th><th>Enterprise</th></tr></thead><tbody>
<tr><th>Price</th><td><span class="price">\u20a60 <small>per month</small></span></td><td class="hl"><span class="price">\u20a620,000 <small>per month</small></span></td><td><span class="price">\u20a6240,000 <small>per year</small></span></td></tr>
<tr><th>Courses</th><td>20</td><td class="hl">100</td><td>1,000</td></tr>
<tr><th>Students</th><td>100</td><td class="hl">500</td><td>50,000</td></tr>
<tr><th>Lecturers</th><td>10</td><td class="hl">50</td><td>5,000</td></tr>
<tr><th>Live classroom features</th><td>Included</td><td class="hl">Included</td><td>Included</td></tr>
<tr><th>AI grading</th><td>Not included</td><td class="hl">Not included</td><td>Included when it launches</td></tr>
<tr><th></th><td><a class="btn sm ghost" href="book-demo.html?plan=Free">Ask about Free</a></td><td class="hl"><a class="btn sm" href="book-demo.html?plan=Standard">Book a demo</a></td><td><a class="btn sm ghost" href="book-demo.html?plan=Enterprise">Talk to us</a></td></tr>
</tbody></table></div>
<p class="note" style="margin-top:20px">Lecturers tied to an institution do not pay individually; the institution\u2019s plan covers them. Individual tutors pay for AI grading access once it launches. Schools subscribe to Standard or Enterprise from the school admin dashboard, and the Zivas team approves Enterprise before payment. Prices are in Nigerian naira.</p></div></section>
<section class="sec tint"><div class="wrap split"><div><h2>Which plan fits?</h2><p class="lead">Enter your numbers and we will point you to the smallest plan that covers them.</p></div>
<form class="box form" id="finder" novalidate><div class="two"><div><label for="f1">Courses</label><input id="f1" name="courses" type="number" min="0" value="5"></div><div><label for="f2">Lecturers</label><input id="f2" name="lecturers" type="number" min="0" value="1"></div></div>
<div><label for="f3">Students</label><input id="f3" name="students" type="number" min="0" value="80"></div>
<div><button class="btn" type="submit">Find my plan</button></div><div id="finder-result" class="result" role="status" aria-live="polite">Your recommendation appears here.</div></form></div></section>
<section class="sec"><div class="wrap"><h2>Pricing questions</h2>{faq_items([FAQ[3],FAQ[4],FAQ[2]],'pq')}</div></section>
{cta()}''')

PAGES['about.html'] = ('About | Zivas', 'Zivas is a remote-first team building the classroom companion that lightens teachers\u2019 workloads.', f'''
{pagehead('We build tools that take work off teachers','Zivas is a remote-first team focused on one thing: giving lecturers their time back.')}
<section class="sec"><div class="wrap split"><div><h2>Why we built Zivas</h2></div><div>
<p class="lead">Learning platforms kept getting bigger while teachers\u2019 days kept getting longer. Zivas starts from the opposite end: automate the repetitive classroom exercises and keep everything else out of the way.</p>
<p>We are not trying to be another bloated LMS. We are building the weekly toolkit a lecturer actually reaches for: coursework, attendance, quizzes, progress and clear communication with students.</p></div></div></section>
<section class="sec tint"><div class="wrap"><h2>How we work</h2>{rows([
('Teacher time comes first','If a feature does not save a lecturer time, it does not ship.'),
('Plain over clever','Clear screens and simple setup beat configuration options.'),
('Honest about the roadmap','Live means live. Anything else is labelled coming soon.'),
('Remote-first','Our team works remotely.')])}</div></section>
<section class="sec"><div class="wrap"><h2>Team</h2>
<p class="note"><span class="ph">Add your team here:</span> name, role, a one-line bio and a photo for each person.</p>
<div class="cols3" style="margin-top:20px"><div><h3><span class="ph">[Name]</span></h3><p><span class="ph">[Role]</span></p></div><div><h3><span class="ph">[Name]</span></h3><p><span class="ph">[Role]</span></p></div><div><h3><span class="ph">[Name]</span></h3><p><span class="ph">[Role]</span></p></div></div></div></section>
<section class="sec tint"><div class="wrap"><h2>Contact</h2><p>Email <a href="mailto:{EMAIL}">{EMAIL}</a><br>WhatsApp <a href="https://wa.me/{WA}">+{WA}</a><br>Location: remote-first team</p></div></section>
{cta('Talk to the team','Tell us about your classes and we will show you how Zivas fits.')}''')

PAGES['faq.html'] = ('FAQ | Zivas', 'Answers about Zivas pricing, features, attendance, AI grading and demos.', f'''
{pagehead('Frequently asked questions','Cannot find your answer? Email us or book a demo.')}
<section class="sec"><div class="wrap">{faq_items(FAQ)}</div></section>{cta('Still have questions?','We reply by email and WhatsApp.')}''')

PAGES['book-demo.html'] = ('Book a demo | Zivas', 'Book a Zivas demo. The form opens an email draft with your details ready to send.', f'''
<section class="pagehead"><div class="wrap"><h1>Book a demo</h1><p class="lead">Tell us a little about your classes. We will open an email draft with everything filled in; press send and we will reply to arrange a time.</p></div></section>
<section class="sec"><div class="wrap split" style="align-items:start">
<form class="form" id="demo-form" novalidate>
<div class="two"><div><label for="name">Full name</label><input id="name" name="name" autocomplete="name"><div class="err" id="name-err"></div></div>
<div><label for="email">Email</label><input id="email" name="email" type="email" autocomplete="email"><div class="err" id="email-err"></div></div></div>
<div class="two"><div><label for="org">School or organisation</label><input id="org" name="org" autocomplete="organization"></div>
<div><label for="role">I am a</label><select id="role" name="role"><option value="">Choose one</option><option>Independent tutor</option><option>Lecturer at an institution</option><option>Institution administrator</option><option>Other</option></select><div class="err" id="role-err"></div></div></div>
<div class="two"><div><label for="size">Approx. number of students</label><input id="size" name="size" inputmode="numeric"></div>
<div><label for="plan">Plan of interest</label><select id="plan" name="plan"><option>Not sure yet</option><option>Free</option><option>Standard</option><option>Enterprise</option></select></div></div>
<div><label for="when">Preferred date and time</label><input id="when" name="when" placeholder="For example, Thursday afternoon"></div>
<div><label for="msg">Anything we should know?</label><textarea id="msg" name="msg"></textarea></div>
<div class="cta-row" style="margin:0"><button class="btn" type="submit">Open email draft</button><a class="btn ghost" id="wa" href="#">Send on WhatsApp instead</a></div>
<p id="sent" class="result" role="status" hidden>Your email app should have opened with the message ready. If it did not, write to <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
</form>
<aside class="box"><h3>Prefer to write directly?</h3><p>Email<br><a href="mailto:{EMAIL}">{EMAIL}</a></p><p>WhatsApp<br><a href="https://wa.me/{WA}">+{WA}</a></p><p>We are a remote-first team, so demos happen online.</p></aside>
</div></section>''')

PAGES['privacy.html'] = ('Privacy | Zivas', 'How Zivas handles personal information.', f'''
{pagehead('Privacy policy','Draft for review. Have this checked against your legal obligations (for example the Nigeria Data Protection Act) before relying on it.').replace('<div class="cta-row"><a class="btn" href="'+DEMO+'">Book a demo</a></div>','')}
<section class="sec"><div class="wrap prose">
<h2>What we collect</h2><p>Account details you provide (name, email, role, institution), course activity such as submissions, scores and attendance, and messages you send us.</p>
<h2>How we use it</h2><p>To run Zivas, show students and lecturers their own information, send notifications and respond to enquiries.</p>
<h2>Sharing</h2><p>Student records are visible to the lecturers and institution responsible for the course. We do not sell personal information.</p>
<h2>Your choices</h2><p>You can ask us to access, correct or delete your information by emailing <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
<h2>Demo requests</h2><p>The demo form opens an email draft on your device. Nothing is sent until you press send.</p></div></section>''')

PAGES['terms.html'] = ('Terms | Zivas', 'Terms of use for Zivas.', f'''
{pagehead('Terms of use','Draft for review. Have this checked by a legal professional before publishing as final.').replace('<div class="cta-row"><a class="btn" href="'+DEMO+'">Book a demo</a></div>','')}
<section class="sec"><div class="wrap prose">
<h2>Using Zivas</h2><p>You agree to provide accurate information, keep your password secure and use Zivas only for teaching and learning.</p>
<h2>Plans and payment</h2><p>Plans, limits and prices are listed on the pricing page and may change with notice. Lecturers tied to an institution are covered by the institution\u2019s plan.</p>
<h2>Your content</h2><p>You keep ownership of the materials and work you upload. You give us permission to store and display them to run the service.</p>
<h2>Availability</h2><p>Features marked coming soon are not guaranteed to launch on any date.</p>
<h2>Contact</h2><p>Questions about these terms: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p></div></section>''')

for page, (t, d, body) in PAGES.items():
    with open(os.path.join(OUT, page), 'w', encoding='utf-8') as f:
        f.write(head(t, d, page) + body + FOOT)

with open(os.path.join(OUT, '404.html'), 'w', encoding='utf-8') as f:
    f.write(head('Page not found | Zivas', 'This page does not exist.', '404.html') +
            f'<section class="sec"><div class="wrap"><h1>That page does not exist</h1><p class="lead">Check the address, or go back to the <a href="index.html">home page</a>.</p></div></section>' + FOOT)

urls = ''.join(f'<url><loc>{BASE}{p}</loc></url>' for p in PAGES)
open(os.path.join(OUT, 'sitemap.xml'), 'w').write(f'<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">{urls}</urlset>')
open(os.path.join(OUT, 'robots.txt'), 'w').write(f'User-agent: *\nAllow: /\nSitemap: {BASE}sitemap.xml\n')
print('built', len(PAGES) + 1, 'pages')

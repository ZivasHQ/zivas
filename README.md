# Zivas public website

The public marketing website for Zivas. This repository is separate from the production application repositories.

## Positioning

Zivas is an academic operations platform for schools, colleges and universities. Its mission:

> Make academic activity visible, measurable and manageable — giving educators and institutions the clarity to improve learning outcomes.

The site leads with institutional administration, academic participation, attendance, assessment workflows and performance visibility. It deliberately does not position Zivas as a bloated all-in-one LMS or a live-class/video-conferencing product.

## Product accuracy

- Describe only capabilities verified in the production frontend/backend.
- Clearly distinguish current capabilities from in-development work.
- Institutional CBT examinations are in development and are not yet available end to end.
- AI-assisted grading endpoints are currently disabled; manual grading remains available.
- Full offline learning is not currently available.
- Do not publish public pricing on this website.
- Do not imply that this static site's demo request form transmits data to a server. It prepares an email for the visitor to review and send.

## Contact

- Email: zivashq@gmail.com
- Phone: +234 810 626 5136

## Local preview

Open `index.html` in a browser or run a static server from the repository root:

```bash
python -m http.server 8000
```

Then visit http://localhost:8000.

## Deployment

The site is published from the `/zivas` GitHub Pages path. Keep canonical URLs, Open Graph URLs, sitemap URLs and asset paths aligned with `https://zivashq.github.io/zivas/`.

## Repositories

- Public website: https://github.com/ZivasHQ/zivas
- Production frontend: https://github.com/ZivasHQ/zivas_production_frontend
- Production backend: https://github.com/ZivasHQ/zivas_production_backend
- Application: https://zivas.onrender.com/

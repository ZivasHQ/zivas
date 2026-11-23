# Zivas public website

This repository contains the public marketing website for Zivas. It is separate from the production application repositories.

## Local preview
Open `index.html` in a browser or run a static server from the repository root:

```bash
python -m http.server 8000
```

Then visit http://localhost:8000.

## Deployment
The site is published from the `/zivas` GitHub Pages path. Keep canonical URLs, Open Graph URLs, sitemap URLs and asset paths aligned with `https://zivashq.github.io/zivas/`.

## Product accuracy
The public site describes the production workflows conservatively. Capabilities that are still under development or disabled in the application must not be marketed as generally available. Confirm feature readiness in the production frontend and backend repositories before changing product claims.

## Repositories
- Public website: https://github.com/ZivasHQ/zivas
- Production frontend: https://github.com/ZivasHQ/zivas_production_frontend
- Production backend: https://github.com/ZivasHQ/zivas_production_backend
- Application: https://zivas.onrender.com/

# ZIVAS public website

The public marketing website for ZIVAS, published with GitHub Pages from this repository.

## Brand and positioning

ZIVAS is a focused academic operations platform for schools, colleges and universities. It helps institutions coordinate academic activity and understand what is happening across their learning environment.

**Brand promise:** Make academic activity visible, measurable and manageable.

The site should communicate clarity over clutter, connected academic operations rather than another bloated all-in-one LMS, educator-led decisions and institutional oversight, and honest distinction between available production capabilities and work in development.

Live video classes are intentionally outside the product scope. Do not invent features, customer logos, testimonials, integrations, certifications, performance claims or public pricing.

## Product accuracy

- Describe only capabilities verified in the production frontend/backend.
- Institutional CBT examinations are in development and are not yet available end to end.
- AI-assisted grading endpoints are currently disabled; manual grading remains available.
- Uploaded learning resources can be saved locally for offline access after the user downloads them while online. This is not full offline application functionality; external YouTube and Google Drive links still require internet.
- Do not publish public pricing on this website.
- The demo request form prepares an email for the visitor to review and send. It does not submit data to a website server.

## Design system

- One type family: DM Sans.
- Brand palette: deep navy, restrained teal, white and soft neutral surfaces.
- Use the existing ZIVAS logo and product screenshots in assets/img/.
- Keep layouts responsive, accessible, readable and restrained. Avoid decorative font stacks, unnecessary gradients, excessive animation and visual clutter.
- Shared styles live in assets/css/global.css; shared navigation and demo-form behaviour live in assets/js/global.js.

## Contact

- Email: support.zivas@gmail.com
- Phone / WhatsApp: +234 811 180 1272

## Local preview

Run `python -m http.server 8000` from the repository root and open http://localhost:8000.

This is a static HTML/CSS/JavaScript site; edit the HTML pages directly. Do not regenerate the website using the retired legacy build script.

## Deployment and SEO

The GitHub Pages site uses the custom domain configured in CNAME: https://zivas.online/. The GitHub Pages project URL may redirect to the custom domain. Keep canonical URLs, Open Graph URLs, sitemap URLs and asset paths aligned with that base URL.

## Repositories

- Public website: https://github.com/ZivasHQ/zivas
- Production frontend: https://github.com/ZivasHQ/zivas_production_frontend
- Production backend: https://github.com/ZivasHQ/zivas_production_backend
- Application: https://zivas.app/

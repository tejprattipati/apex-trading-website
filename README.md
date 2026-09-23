# Apex Trading Group

ATG’s responsive website for GitHub Pages. Navy and silver branding, original club photography and headshots, and new Manhattan stock photography.

## Preview

Run `python3 -m http.server 4173` in this folder and visit `http://localhost:4173`.

## Publish with GitHub Pages

In this repository, open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, branch **main**, folder **/ (root)**, and save.

Project URL: https://tejprattipati.github.io/apex-trading-website/

The site works at a project URL or a custom domain. No application server, package installation, API keys, or paid services are required. `.nojekyll` serves the checked-in files directly. The existing `atgumich.com` domain has not been changed.

## Editing

- `data/content.json`: names, roles, emails, placement entries, image mappings, original application and interest form links, and recruitment dates.
- `scripts/build.py`: page copy, shared navigation and footer, and HTML templates.
- `assets/style.css`: responsive design, typography, navy/silver palette.
- `assets/main.js`: mobile navigation, keyboard-accessible placement year tabs, photo carousel/lightbox, and scroll reveals.
- `assets/images/`: self-hosted optimized original ATG imagery and licensed stock photography.
- `assets/fonts/`: self-hosted Cormorant Garamond and Inter.

After editing content or templates, run `python3 scripts/build.py` and commit the generated HTML with the changed source. Editing CSS or JavaScript takes effect directly.

The four primary pages are Home, About, Placement, and Prospective Members. Legacy `/team-1`, `/placement`, and `/prospective-members` paths are retained. All text is in HTML and remains readable with JavaScript disabled. Reduced-motion preferences are respected.

## Content

Content and image inventory audited against https://www.atgumich.com/ on September 22, 2026. The member count is 60+; alumni 120+; assets under management $25,000; full-time placement 100%. Founding year remains 2014, matching the source website. The stale $10k portfolio reference was updated to $25,000. All 22 leadership profiles, 45 firm logos, 55 recent-placement rows, and 12 gallery images were carried over.

The Fall 2026 dates are historical source dates (September 9–21), not a claim that applications are currently open. Existing Google Form links are preserved. Board profiles use email links; LinkedIn links are omitted. Instagram retrieval was unavailable, so the supplied Instagram visual reference guides the typography and palette while the original ATG gallery supplies the club photos.

See [CREDITS.md](CREDITS.md) for image and font provenance. Club photos and firm marks remain the property of their respective owners.

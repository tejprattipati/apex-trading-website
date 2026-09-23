# Apex Trading Group

ATG’s responsive website for GitHub Pages. Navy and silver branding, original club photography and headshots, and new Manhattan stock photography.

## Preview

Run `python3 -m http.server 4173` in this folder and visit `http://localhost:4173`.

## Publish with GitHub Pages

In this repository, open **Settings → Pages**. Under **Build and deployment**, choose **Deploy from a branch**, branch **main**, folder **/ (root)**, and save.

Project URL: https://tejprattipati.github.io/apex-trading-website/

The site works at a project URL or a custom domain. No application server, package installation, API keys, or paid services are required. `.nojekyll` serves the checked-in files directly. The existing `atgumich.com` domain has not been changed.

## Editing

- `data/content.json`: names, roles, emails, placement entries, homepage firm selection, image mappings, original application and interest form links, and recruitment dates.
- `scripts/build.py`: page copy, shared navigation and footer, and HTML templates.
- `assets/style.css`: responsive design, typography, navy/silver palette.
- `assets/main.js`: mobile navigation, keyboard-accessible placement year filters, photo carousel/lightbox, and scroll reveals.
- `assets/images/`: self-hosted optimized original ATG imagery and licensed stock photography.
- `assets/fonts/`: self-hosted Cormorant Garamond and IBM Plex Sans.

After editing content or templates, run `python3 scripts/build.py` and commit the generated HTML with the changed source. Editing CSS or JavaScript takes effect directly.

The four primary pages are Home, About, Placement, and Prospective Members. Legacy `/team-1`, `/placement`, and `/prospective-members` paths are retained. All text is in HTML and remains readable with JavaScript disabled. Reduced-motion preferences are respected.

## Content

Content and image inventory audited against https://www.atgumich.com/ on September 22, 2026. The member count is 60+; alumni 120+; assets under management $25,000; full-time placement 100%. Founding year remains 2014, matching the source website. The stale $10k portfolio reference was updated to $25,000. All 22 leadership profiles, 45 original employers, 55 recent-placement rows, and 12 gallery images were carried over. The placement directory now also includes firm names from the supplied alumni list, covering current and prior employment; only aggregate employer names are published. All recent classes are visible by default, with optional year filters.

The Fall 2026 dates are historical source dates (September 9–21), not a claim that applications are currently open. Existing Google Form links are preserved. Board profiles use email links; LinkedIn links are omitted. Instagram retrieval was unavailable, so the supplied Instagram visual reference guides the typography and palette while the original ATG gallery supplies the club photos.

Selected pitch highlights show stock-price changes from the original pitch price through the September 21, 2026 close, labeled “Returns as of September 2026.” These are selected examples, not actual fund returns. The source data records the pitch and closing prices, cutoff dates, and public price sources. Update the prices, cutoff copy, and date label together when refreshing this section.

Leadership is grouped into Executive Board, Sector Heads, Chairs, and Senior Advisor. Placement entries use the requested curated order and IBD labels for confirmed banking roles. Sector photography follows the original six-image grid with a navy and silver treatment.

See [CREDITS.md](CREDITS.md) for image and font provenance. Club photos and firm marks remain the property of their respective owners.

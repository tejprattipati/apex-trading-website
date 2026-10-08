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
- `assets/fonts/`: self-hosted Cormorant Garamond, Raleway, and IBM Plex Sans.

After editing content or templates, run `python3 scripts/build.py` and commit the generated HTML with the changed source. Editing CSS or JavaScript takes effect directly.

The four primary pages are Home, About, Placement, and Prospective Members. Legacy `/team-1`, `/placement`, and `/prospective-members` paths are retained. All text is in HTML and remains readable with JavaScript disabled. Reduced-motion preferences are respected.

## Content

Content and image inventory audited against https://www.atgumich.com/ on September 22, 2026. The member count is 60+; alumni 150+; assets under management $25,000; full-time placement 100%. Founding year remains 2014, matching the source website. The stale $10k portfolio reference was updated to $25,000. The initial migration carried over all 22 leadership profiles, 45 original employers, 55 recent-placement rows, and 12 gallery images. The current placement directory follows the club’s September 23 curation: 52 finance/advisory firms after the requested employer removals and consolidation of the TD/TD Cowen logo cards, with 44 recent-placement rows remaining. It includes current and prior employment from the supplied alumni list; only aggregate employer names are published. Class of 2026 is selected by default, with toggles for 2027 and 2028.

The Fall 2026 dates are historical source dates (September 9–21), not a claim that applications are currently open. Existing Google Form links are preserved. Board profiles use email links; LinkedIn links are omitted. Instagram retrieval was unavailable, so the supplied Instagram visual reference guides the typography and palette while the original ATG gallery supplies the club photos.

Selected pitch highlights show stock-price changes through the October 8, 2026 close. At the club's request, each baseline is the lowest reported daily intraday low in its displayed pitch month: VRT $172.35 on February 5, GKOS $95.87 on March 13, TTMI $81.80 on February 5, and GO $5.66 on March 9, all in 2026. Each visible label identifies the month-low basis. These are hypothetical price changes from retrospectively selected monthly lows, not verified pitch-entry or actual fund returns. Original `pitch_price` fields are retained as provenance and are not used when `baseline_price` is present. The source data records baseline and closing prices, dates, and public market-data URLs.

A monthly Codex task refreshes and publishes these figures on the first of each month at 9 a.m. America/Detroit. Keep the historical month-low baselines fixed, verify the latest completed regular-session closing prices with a common cutoff date, and account consistently for stock splits. Update closing prices, closing dates, sources, and `pitch_returns_note` together, rebuild the pages, verify the calculations and labels, and publish the relevant changes. If a price cannot be verified, preserve its previous value and actual date rather than marking stale data as current.

Leadership is grouped into Executive Board, Sector Heads, Chairs, and Senior Advisor. Placement entries use the requested curated order and IBD labels for confirmed banking roles. Sector photography follows the original six-image grid with a navy and silver treatment.

See [CREDITS.md](CREDITS.md) for image and font provenance. Club photos and firm marks remain the property of their respective owners.

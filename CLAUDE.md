# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static personal academic website for Alamin Sarker, a prospective PhD student in NLP. It is a single-page site deployed on GitHub Pages at `https://alaminsarkerfrii.github.io/`.

## Deployment

Push to `main` branch to deploy. GitHub Pages serves directly from the root of `main`.

To update the git remote (e.g. after a repository rename):
```bash
bash update-remote.sh
git push -u origin main
```

## Architecture

The site is a single HTML file with no build step, no JavaScript framework, and no package manager.

- `index.html` — all content and inline JS (only a `copyEmail()` function for clipboard)
- `style.css` — all styling; uses CSS custom properties defined in `:root`
- `assets/images/MyImage.jpg` — profile photo
- `assets/Alamin_Sarker_CV_PhD_NLP.pdf` — linked CV

## Layout

Three-column layout (desktop):
- **Left column (25%)** — profile photo, contact info, social links, research interests
- **Middle column (25%)** — technical skills and languages
- **Right column (50%)** — about, research experience, education, professional experience

On mobile (`≤768px`) columns stack vertically. Print styles collapse to single column.

## CSS Conventions

Colors and spacing use CSS variables from `:root` (e.g. `var(--primary-color)`, `var(--text-secondary)`). Do not use hardcoded hex values — reference the existing variables.

## Previewing Locally

Open `index.html` directly in a browser, or serve with any static file server:
```bash
python3 -m http.server 8000
```

# Brightside Collective — "Just Breathe" Lakehouse & Cabin

Your one-page Airbnb showcase site, reorganized into clean, separate files.

## Folder structure

```
Airbnb_Property_Website/
├── index.html              ← page structure/content only
├── css/
│   └── style.css           ← all styling (colors, layout, fonts)
├── js/
│   └── main.js              ← booking form → Airbnb redirect logic
├── assets/
│   └── images/
│       ├── hero-bg.png                    ← hero dusk photo (your original)
│       ├── logo/
│       │   ├── brightside-logo-original.png   ← full-color logo (light backgrounds)
│       │   └── brightside-logo-onDark.png     ← recolored logo (dark plum backgrounds)
│       ├── gallery/         ← exterior/interior photos
│       ├── bedrooms/        ← bedroom + cabin photos
│       └── host/            ← host photo
├── generate_placeholders.py ← optional script that made the placeholder images
└── README.md                ← this file
```

Now if you want to change a color, you edit `css/style.css`. If you want to
change the booking redirect behavior, you edit `js/main.js`. If you want to
swap a photo, you just replace the file in `assets/images/...` — the filename
stays the same, so you never have to touch the HTML.

## About your logo

I used the logo file you attached (`BC-Logo.png`) exactly as provided —
nothing was stretched or redrawn. It already had a transparent background,
so I dropped it straight into the nav bar at a fixed height (auto width),
so its proportions are locked.

I also made **one recolored variant** for the dark plum sections (the hero
motif, the "Ready to just breathe?" band, and the footer): the purple
wordmark becomes cream/off-white so it's legible against the dark
background, while the gold sun icon stays exactly as you supplied it. Same
artwork, same shape — just a color swap for contrast, per your instructions.

- `brightside-logo-original.png` → used on light/cream backgrounds (nav bar)
- `brightside-logo-onDark.png` → used on dark plum backgrounds (hero, booking band, footer)

## About the property photos — action needed

I was **not able to download the real photos from your Airbnb listing**,
because `airbnb.com` / `a0.muscache.com` aren't reachable from this
environment (they're not on the allowed network list here). So every photo
slot currently shows a placeholder graphic labeled with what belongs there,
e.g. "Living Space — Replace with Airbnb photo."

To finish the site, just save each real photo from your Airbnb listing and
drop it into the matching path below, **using the exact filename** — the
page will pick it up automatically:

| Where it's used                     | Save your photo as...                          |
|--------------------------------------|-------------------------------------------------|
| Intro section (large exterior)       | `assets/images/gallery/exterior-full.jpg`       |
| Gallery — main exterior              | `assets/images/gallery/exterior-main.jpg`       |
| Gallery + Space section — living room| `assets/images/gallery/living-space.jpg`        |
| Gallery — kitchen                    | `assets/images/gallery/kitchen.jpg`             |
| Gallery + Space section — outdoor    | `assets/images/gallery/outdoor-area.jpg`        |
| Space section — cabin exterior       | `assets/images/gallery/cabin.jpg`               |
| Gallery + Sleep section — bedroom 1  | `assets/images/bedrooms/bedroom-1.jpg`          |
| Sleep section — bedroom 2            | `assets/images/bedrooms/bedroom-2.jpg`          |
| Sleep section — bedroom 3            | `assets/images/bedrooms/bedroom-3.jpg`          |
| Sleep section — cabin bedroom        | `assets/images/bedrooms/cabin-bedroom.jpg`      |
| Host section — Claudine's photo      | `assets/images/host/claudine.jpg`               |

Tip: right-click each photo on your Airbnb listing page → "Save image as…"
→ rename it to match the table above → drop it into the matching folder.
The layout, cropping, and aspect ratios are already set up in the CSS, so
any reasonably-sized photo will drop right in and look correct.

## Opening the site

Just double-click `index.html` to preview it locally, or upload the whole
folder to any static host (Netlify, GitHub Pages, etc.) — no build step
needed.

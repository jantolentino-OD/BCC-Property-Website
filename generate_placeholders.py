from PIL import Image, ImageDraw, ImageFont
import os

CREAM = (245, 240, 234)
PLUM = (94, 45, 107)
PLUM_DEEP = (58, 29, 68)
GOLD = (206, 165, 101)
MAUVE = (176, 120, 152)

SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"

def make_placeholder(path, w, h, label, sublabel="Replace with Airbnb photo"):
    img = Image.new("RGB", (w, h), CREAM)
    d = ImageDraw.Draw(img)

    # soft border
    border = max(3, w // 200)
    d.rectangle([border, border, w - border, h - border], outline=GOLD, width=border)

    # inner icon: simple camera glyph made of shapes
    icon_size = min(w, h) * 0.18
    cx, cy = w / 2, h / 2 - icon_size * 0.55
    body_w, body_h = icon_size * 1.5, icon_size
    d.rounded_rectangle(
        [cx - body_w/2, cy - body_h/2, cx + body_w/2, cy + body_h/2],
        radius=icon_size*0.12, outline=PLUM, width=max(2, int(icon_size*0.06))
    )
    lens_r = icon_size * 0.28
    d.ellipse([cx - lens_r, cy - lens_r, cx + lens_r, cy + lens_r],
              outline=PLUM, width=max(2, int(icon_size*0.06)))
    d.rectangle([cx - body_w*0.18, cy - body_h/2 - icon_size*0.14,
                 cx + body_w*0.05, cy - body_h/2],
                fill=CREAM, outline=PLUM, width=max(2, int(icon_size*0.05)))

    # label text
    try:
        font_label = ImageFont.truetype(SERIF, int(min(w, h) * 0.075))
        font_sub = ImageFont.truetype(SANS, int(min(w, h) * 0.038))
    except Exception:
        font_label = ImageFont.load_default()
        font_sub = ImageFont.load_default()

    text = label
    bbox = d.textbbox((0, 0), text, font=font_label)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text((w/2 - tw/2, cy + icon_size * 0.9), text, font=font_label, fill=PLUM_DEEP)

    sub = sublabel
    bbox2 = d.textbbox((0, 0), sub, font=font_sub)
    sw, sh = bbox2[2] - bbox2[0], bbox2[3] - bbox2[1]
    d.text((w/2 - sw/2, cy + icon_size * 0.9 + th + int(min(w,h)*0.035)), sub, font=font_sub, fill=MAUVE)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    img.save(path, quality=88)
    print("wrote", path)


# Gallery / space photos (4:3 landscape)
make_placeholder("assets/images/gallery/exterior-full.jpg", 1200, 1500, "Lakehouse Exterior")  # 4:5 intro photo
make_placeholder("assets/images/gallery/exterior-main.jpg", 1200, 900, "Main Exterior View")
make_placeholder("assets/images/gallery/living-space.jpg", 1200, 900, "Living Space")
make_placeholder("assets/images/gallery/kitchen.jpg", 1200, 900, "Kitchen")
make_placeholder("assets/images/gallery/outdoor-area.jpg", 1200, 900, "Outdoor Area")
make_placeholder("assets/images/gallery/cabin.jpg", 1200, 900, "Private Cabin")

# Bedrooms (3:4 portrait)
make_placeholder("assets/images/bedrooms/bedroom-1.jpg", 900, 1200, "Bedroom 1")
make_placeholder("assets/images/bedrooms/bedroom-2.jpg", 900, 1200, "Bedroom 2")
make_placeholder("assets/images/bedrooms/bedroom-3.jpg", 900, 1200, "Bedroom 3")
make_placeholder("assets/images/bedrooms/cabin-bedroom.jpg", 900, 1200, "Cabin Bedroom")

# Host photo (square)
make_placeholder("assets/images/host/claudine.jpg", 480, 480, "Host Photo", "Replace with host photo")

print("done")

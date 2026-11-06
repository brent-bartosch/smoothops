from PIL import Image

pairs = [("home", 1280), ("about", 1280), ("home", 400)]
for p, w in pairs:
    a = Image.open(f"/tmp/ui-before-{p}-{w}.png")
    b = Image.open(f"/tmp/ui-after-{p}-{w}.png")
    h = min(a.height, b.height, 2400)
    a = a.crop((0, 0, a.width, h))
    b = b.crop((0, 0, b.width, h))
    out = Image.new("RGB", (a.width + b.width + 24, h), "white")
    out.paste(a, (0, 0))
    out.paste(b, (a.width + 24, 0))
    path = f"/Users/brentbartosch/Downloads/smoothed-ui-before-after-{p}-{w}.png"
    out.save(path)
    print(path, out.size)

import os
import random
from PIL import Image, ImageDraw, ImageFont
import arabic_reshaper
from bidi.algorithm import get_display

# Arabic words (you can expand this list or use a dictionary file)
arabic_words = [
    "مرحبا", "مدرسة", "سيارة", "كمبيوتر", "هاتف", "قلم", "شجرة", "سماء", "أهلاً", "عالم"
]

# Parameters
output_dir = "/Users/ajit/deep-text-recognition-benchmark/t_data"
image_dir = os.path.join(output_dir, "images")
label_file = os.path.join(output_dir, "labels.txt")
num_samples = 50
img_size = (160, 48)
font_path = "Amiri-Regular.ttf"  # Make sure this font supports Arabic

# Create directories
os.makedirs(image_dir, exist_ok=True)

# Load font
try:
    font = ImageFont.truetype(font_path, 28)
except IOError:
    raise Exception("Arabic font not found. Make sure to download 'Amiri-Regular.ttf' or another Arabic font.")

with open(label_file, "w", encoding="utf-8") as f:
    for i in range(1, num_samples + 1):
        text = random.choice(arabic_words)
        reshaped_text = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped_text)

        img = Image.new('L', img_size, color=255)
        draw = ImageDraw.Draw(img)
        b= draw.textbbox((0,0),bidi_text, font=font)
        h=b[2]-b[0]
        w=b[3]-b[1]
        draw.text(((img_size[0] - w) / 2, (img_size[1] - h) / 2), bidi_text, font=font, fill=0)

        filename = f"{i:06d}.png"
        filepath = os.path.join(image_dir, filename)
        img.save(filepath)

        f.write(f"{filepath} {text}\n")

print(f"Arabic synthetic dataset created at: {output_dir}")
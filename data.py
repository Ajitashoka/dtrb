import os
import glob

# Set your image folder here
image_dir = "/Users/ajit/deep-text-recognition-benchmark/out"
output_file = os.path.join(image_dir, "label.txt")

with open(output_file, "w", encoding="utf-8") as f:
    for img_path in glob.glob(os.path.join(image_dir, "*.jpg")):
        img_name = os.path.basename(img_path)
        if "_" in img_name:
            label = "_".join(img_name.split("_")[:-1])  # Remove trailing _#.jpg
        else:
            label = os.path.splitext(img_name)[0]

        full_path = os.path.abspath(img_path)
        f.write(f"{full_path} {label}\n")

print(f"✅ Labels extracted and saved to: {output_file}")

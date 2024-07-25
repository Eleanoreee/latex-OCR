import os
from PIL import Image
from pix2tex.cli import LatexOCR
from concurrent.futures import ThreadPoolExecutor, as_completed

imgs_dir = '/Users/eleanorewu/Latex-OCR/data/val/val-images'
seq_file = '/Users/eleanorewu/Latex-OCR/data/val/val-formulas.txt'
output_file = '/Users/eleanorewu/Latex-OCR/test/latexocr_output_parallel.txt'

model = LatexOCR()

def process_image(image_name):
    try:
        img_path = os.path.join(imgs_dir, image_name)
        img = Image.open(img_path)
        result = model(img)
        return result
    except Exception as e:
        print(f"Error processing {image_name}: {e}")
        return ""

image_files = sorted([f for f in os.listdir(imgs_dir) if f.endswith('.png')])

counter = 0

# Process images in parallel
with ThreadPoolExecutor(max_workers=8) as executor:
    results = []
    for i, result in enumerate(executor.map(process_image, image_files), 1):
        results.append(result)
        if i % 100 == 0:
            print(f"Finished processing {i} files.")

with open(output_file, 'w', encoding='utf-8') as f_out:
    for result in results:
        f_out.write(result + '\n')

print("Processing completed. Results saved to:", output_file)
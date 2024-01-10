import os
from PIL import Image
from pix2tex.cli import LatexOCR
from concurrent.futures import ThreadPoolExecutor

imgs_dir = '/Users/eleanorewu/formula_images'
seq_file = '/Users/eleanorewu/im2latex_formulas.lst'
output_file = '/Users/eleanorewu/czb/testing/latexocr_output_parallel.txt'

model = LatexOCR()

# from list file extract img name
with open(seq_file, 'r') as f_lst:
    lines = f_lst.readlines()
image_filenames = [line.split()[1] + ".png" for line in lines]

def process_image(filename):
    img_path = os.path.join(imgs_dir, filename)
    print(f"Processing {img_path}")
    try:
        img = Image.open(img_path)
        result = model(img)
        return result
    except Exception as e:
        print(f"Error processing {img_path}: {e}")
        return None

total_images = len(image_filenames)
processed_count = 0

with open(output_file, 'w') as f_out:
    with ThreadPoolExecutor() as executor:
        results = executor.map(process_image, image_filenames)
        for result in results:
            processed_count += 1
            if result:
                f_out.write(result + '\n')
            else:
                f_out.write('\n')  # placeholder

            completion_percentage = (processed_count / total_images) * 100
            print(f"Processed: {processed_count}/{total_images} ({completion_percentage:.2f}%)")
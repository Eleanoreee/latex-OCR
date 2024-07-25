import os
import shutil

def clean_and_convert_data(current_directory, target_directory):
    # Create target directory
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Create images directory
    images_directory = os.path.join(target_directory, 'images')
    if not os.path.exists(images_directory):
        os.makedirs(images_directory)

    # Load formulas from im2latex_formulas.lst
    with open(os.path.join(current_directory, 'im2latex_formulas.lst'), 'r') as lst_file:
        formulas = lst_file.read().splitlines()

    # Load image mappings from im2latex.lst
    image_formula_mapping = {}
    with open(os.path.join(current_directory, 'im2latex.lst'), 'r') as txt_file:
        for line in txt_file:
            parts = line.split()
            idx = int(parts[0])
            image_name = parts[1]
            image_formula_mapping[image_name] = idx

    # Validate and clean data
    valid_formulas = []
    valid_image_names = set()
    formula_images_path = os.path.join(current_directory, 'formula_images')

    for image_name, idx in image_formula_mapping.items():
        image_path = os.path.join(formula_images_path, f"{image_name}.png")
        if os.path.exists(image_path) and idx < len(formulas):
            valid_formulas.append(formulas[idx])
            valid_image_names.add(image_name)
        else:
            print(f"Warning: Missing image or formula for {image_name}, removing entry.")

    # Copy valid images to the target directory and rename them
    for idx, image_name in enumerate(sorted(valid_image_names)):
        source_path = os.path.join(formula_images_path, f"{image_name}.png")
        target_image_name = f"{idx:08d}.png"
        target_image_path = os.path.join(images_directory, target_image_name)
        shutil.copy(source_path, target_image_path)

    # Write valid formulas to the target file (formulas.txt)
    with open(os.path.join(target_directory, 'formulas.txt'), 'w') as formulas_file:
        formulas_file.write("\n".join(valid_formulas))

if __name__ == "__main__":
    current_directory = "/Users/eleanorewu/Latex-OCR/data/data-seperate/4"
    target_directory = "/Users/eleanorewu/Latex-OCR/data/data-seperate/4/converted"

    clean_and_convert_data(current_directory, target_directory)
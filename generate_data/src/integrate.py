import os
import shutil

def resequence_images(source_directories, target_directory):
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # Initialize the image counter
    image_counter = 0

    # Iterate over each source directory
    for source_directory in source_directories:
        # Sort the image files in the source directory
        image_files = sorted([f for f in os.listdir(source_directory) if f.endswith('.png')])
        
        # Copy each image to the target directory with updated sequence
        for image_file in image_files:
            source_path = os.path.join(source_directory, image_file)
            target_filename = f"{image_counter:08d}.png"
            target_path = os.path.join(target_directory, target_filename)
            shutil.copy(source_path, target_path)
            image_counter += 1


def integrate_txt_files(source_files, target_file):
    # Initialize the list to store all lines from the text files
    all_lines = []

    # Iterate over each source file
    for source_file in source_files:
        # Read the content of the source file and append it to all_lines
        with open(source_file, 'r') as file:
            lines = file.readlines()
            all_lines.extend(lines)

    # Write all the lines to the target file
    with open(target_file, 'w') as file:
        file.writelines(all_lines)


# Example usage:
source_directories = [
    "/Users/eleanorewu/Latex-OCR/data/1/converted/images",
    "/Users/eleanorewu/Latex-OCR/data/2/converted/images",
    "/Users/eleanorewu/Latex-OCR/data/3/converted/images",
    "/Users/eleanorewu/Latex-OCR/data/4/converted/images"
]
target_directory = "/Users/eleanorewu/Latex-OCR/data/images"
resequence_images(source_directories, target_directory)


source_files = [
    "/Users/eleanorewu/Latex-OCR/data/1/converted/formulas.txt",
    "/Users/eleanorewu/Latex-OCR/data/2/converted/formulas.txt",
    "/Users/eleanorewu/Latex-OCR/data/3/converted/formulas.txt",
    "/Users/eleanorewu/Latex-OCR/data/4/converted/formulas.txt"
]
target_file = "/Users/eleanorewu/Latex-OCR/data/formulas.txt"
integrate_txt_files(source_files, target_file)

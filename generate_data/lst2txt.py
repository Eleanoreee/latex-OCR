# Specify paths
lst_file_path = '/Users/eleanorewu/Latex-OCR/data/2/im2latex.lst'
txt_file_path = '/Users/eleanorewu/Latex-OCR/data/2/im2latex.txt'

# Read the .lst file and extract filenames
with open(lst_file_path, 'r') as lst_file:
    lines = lst_file.readlines()

# Extract filenames from the lines
filenames = [line.strip().split()[1] for line in lines]

# Write filenames to the .txt file
with open(txt_file_path, 'w') as txt_file:
    txt_file.write('\n'.join(filenames))

print(f"Conversion from {lst_file_path} to {txt_file_path} completed.")

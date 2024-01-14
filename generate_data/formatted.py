import re

generate_file = '/Users/eleanorewu/czb/dataset_format/generate_zephyr.txt'
formulas_file = '/Users/eleanorewu/czb/dataset_format/generate_zephyr_formatted.txt'

with open(generate_file, 'r') as f:
    content = f.read()  # Read the entire content as a single string

content = re.sub(r'\\begin\{[^}]+\}(.*?)\\end\{[^}]+\}', '', content, flags=re.DOTALL)  # Remove all content between \begin{} and \end{}
latex_expressions = re.findall(r'\$\$(.*?)\$\$|\$(.*?)\$', content)  # Re-sequence and format the formulas
filtered_expressions = [expr[0] if expr[0] else expr[1] for expr in latex_expressions if any(expr)]
formatted_content = '\n'.join(filter(lambda x: len(x) > 5, filtered_expressions))  # Remove lines with fewer than 5 characters

with open(formulas_file, 'w') as f:
    f.write(formatted_content)

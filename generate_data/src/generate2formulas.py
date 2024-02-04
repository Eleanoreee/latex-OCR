import sys
import os
import re

def format_latex(input_file):
    output_file = os.path.splitext(input_file)[0] + "_formatted.txt"
    
    with open(input_file, 'r') as f:
        content = f.read()

    content = re.sub(r'\\begin\{[^}]+\}(.*?)\\end\{[^}]+\}', '', content, flags=re.DOTALL)  # Remove all content between \begin{} and \end{}
    latex_expressions = re.findall(r'\$\$(.*?)\$\$|\$(.*?)\$', content)  # Re-sequence and format the formulas
    filtered_expressions = [expr[0] if expr[0] else expr[1] for expr in latex_expressions if any(expr)]
    formatted_content = '\n'.join(filter(lambda x: len(x) > 5, filtered_expressions))  # Remove lines with fewer than 5 characters
    
    with open(output_file, 'w') as f:
        f.write(formatted_content)

    return output_file

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py input_file")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"Input file '{input_file}' does not exist.")
        sys.exit(1)

    output_file = format_latex(input_file)
    print(f"Formatted content saved to {output_file}")
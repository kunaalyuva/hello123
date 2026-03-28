import ast
import re
from ollama_model import ollama_call, ollama_call_for_pdf
from markdown_to_pdf import create_pdf

def make_pdf(md):
    data = ollama_call_for_pdf(md)

    # Remove code block formatting if present
    data = data.replace("```python", "").replace("```", "").replace("```data", "").strip()

    # Extract the first dictionary found in the string
    match = re.search(r"\{.*\}", data, re.DOTALL)
    if not match:
        print("No dictionary found in the data!")
        print("Raw data:", repr(data))
        return

    dict_str = match.group(0)

    try:
        data_dict = ast.literal_eval(dict_str)
    except Exception as e:
        print("Failed to parse dictionary:", e)
        print("Dictionary string:", repr(dict_str))
        return

    # Optional: print the dictionary for verification
    print(data_dict)

    # Create the PDF
    create_pdf(data_dict)
    print("PDF generated successfully.")


def markdown_gen(code):
    md = ollama_call(code)
    md = md.replace("```markdown", "").replace("```", "").strip()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(md)
    print("README.md generated successfully.")

    # Generate PDF from the markdown
    make_pdf(md)


if __name__ == "__main__":
    code = '''
# file1.py
def add(a, b):
    """Returns the sum of two numbers."""
    return a + b

def multiply(a, b):
    """Returns the product of two numbers."""
    return a * b
    
# file2.py
class Calculator:
    """A simple calculator class."""
    
    def subtract(self, a, b):
        """Returns the difference of two numbers."""
        return a - b

    def divide(self, a, b):
        """Returns the division of two numbers."""
        if b == 0:
            raise ValueError("Cannot divide by zero.")
        return a / b
'''
    markdown_gen(code)

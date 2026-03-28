import ollama

def ollama_call(code):
    prompt = f"""
You are an expert Markdown README generator. Based on the code provided, you will create a professional and structured GitHub README in Markdown format.

Code:
{code}

Instructions:
1. Carefully analyze the code and its structure, including functions, classes, dependencies, and usage patterns.
2. Read the natural language query to understand the purpose and audience of the project.
3. Generate a Markdown README with the following sections:
   - **Title**: A concise, descriptive title for the project.
   - **Description**: A brief explanation of what the project does and its key purpose.
   - **Features**: A list of the main functionalities.
   - **Tech Stack**: Programming languages, libraries, frameworks, and tools used in the project.
   - **Advantages**: Uses of the project.
   - **Future Improvements**: Suggestions on how this project can be enhanced or extended.
4. Use proper Markdown formatting with headers, bullet points, bold, tables if needed.
5. Keep the content clear, concise, and informative, suitable for GitHub and documentation purposes.
6. Ensure the README is helpful to both developers and non-technical stakeholders who might want to use or understand the project.

Markdown Code:
"""

    try:
        response = ollama.chat(model='mistral:latest', messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ])
        
        return response['message']['content']
        
    except Exception as e:
        return "Error: " + str(e)


def ollama_call_for_pdf(md):
    prompt = f"""
You are an expert Markdown README PDF generator. Based on the md code provided below, create a professional and well-structured `data` dictionary that captures all relevant information extracted from the code.

The dictionary must follow this exact format with keys and values as shown.

Code:
{md}

Required Output Format:
data = {{
    ...
}}

Now generate the `data` dictionary like this:
```data
data = <filled dictionary here>
```
"""

    try:
        response = ollama.chat(model='mistral:instruct', messages=[
            {
                'role': 'user',
                'content': prompt
            }
        ])
        
        return response['message']['content']
        
    except Exception as e:
        return "Error: " + str(e)


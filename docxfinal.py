import json
import re

import json
import re
from docx import Document

def convert_docx_to_text(docx_file, text_file):
    """
    Converts a .docx file to a plain text file.
    """
    doc = Document(docx_file)
    with open(text_file, 'w', encoding='utf-8') as f:
        for para in doc.paragraphs:
            f.write(para.text + '\n')
    print(f"Converted '{docx_file}' to '{text_file}'")

# def parse_text_file_to_json(text_file):
#     """
#     Parses the text file to extract questions, options, and answers, and returns them in JSON format.
#     """
#     questions_data = []
#     question = None
#     options = []
#     answer = None

#     with open(text_file, 'r', encoding='utf-8') as file:
#         for line_num, line in enumerate(file, start=1):
#             text = line.strip()

#             # Detect a question by checking if it ends with a "?" symbol
#             if text.endswith("?"):
#                 # Save the previous question block before starting a new one
#                 if question:
#                     questions_data.append({
#                         "question": question,
#                         "options": options,
#                         "answer": answer
#                     })
#                 # Start a new question block
#                 question = text
#                 options = []
#                 answer = None

#             # Collect options until we hit an "Answer:" or new question line
#             elif not text.startswith("Answer:") and question:
#                 # Check if the answer is embedded in the option text
#                 if "Answer:" in text:
#                     # Split to capture option and answer separately
#                     option_text, embedded_answer = text.split("Answer:")
#                     options.append(option_text.strip())
#                     answer = embedded_answer.strip()
#                 else:
#                     # Otherwise, just add as an option
#                     options.append(text)

#             # Detect an answer line (e.g., "Answer: A")
#             elif text.startswith("Answer:"):
#                 answer = text.split("Answer:")[1].strip()

#         # Append the last question block after exiting the loop
#         if question:
#             # Remove empty options for the last question
#             options = [opt for opt in options if opt]  # Remove empty strings
#             questions_data.append({
#                 "question": question,
#                 "options": options,
#                 "answer": answer
#             })

#     return questions_data

def parse_text_file_to_json(text_file):
    """
    Parses the text file to extract questions, options, and answers, and returns them in JSON format.
    """
    questions_data = []
    question = None
    options = []
    answer = None

    with open(text_file, 'r', encoding='utf-8') as file:
        for line_num, line in enumerate(file, start=1):
            text = line.strip()  # Strip whitespace from the beginning and end

            # Detect a question by checking if it ends with a "?" symbol or starts with a number (e.g., "37.")
            if text.endswith("?") or re.match(r"^\d+\.", text):
            
                # Save the previous question block before starting a new one
                if question:
                    # Filter out empty or whitespace-only strings from options
                    options = [opt for opt in options if opt.strip()]
                    questions_data.append({
                        "question": question,
                        "options": options,
                        "answer": answer
                    })
                # Start a new question block
                question = text
                options = []
                answer = None

            # Collect options until we hit an "Answer:" or new question line
            elif not text.startswith("Answer:") and question:
                # Check if the answer is embedded in the option text
                if "Answer:" in text:
                    # Split to capture option and answer separately
                    option_text, embedded_answer = text.split("Answer:")
                    options.append(option_text.strip())
                    answer = embedded_answer.strip()
                else:
                    # Otherwise, just add as an option
                    options.append(text)

            # Detect answer line (e.g., "Answer: A")
            elif text.startswith("Answer:"):
                answer = text.split("Answer:")[1].strip()

        # Append the last question block after exiting the loop
        if question:
            # Filter out empty or whitespace-only strings from options
            options = [opt for opt in options if opt.strip()]
            questions_data.append({
                "question": question,
                "options": options,
                "answer": answer
            })

    return questions_data

def save_as_json(data, output_file):
    """
    Saves the parsed data to a JSON file.
    """
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to '{output_file}'")

docx_file='doc2.docx'

text_file = 'converted_text_file2.txt'
output_json = 'questions_and_answers22.json'

# Step 1: Convert .docx to plain text
convert_docx_to_text(docx_file, text_file)

# Step 2: Parse text file to JSON format
questions_data = parse_text_file_to_json(text_file)

# Step 3: Save data to JSON file
save_as_json(questions_data, output_json)

# # Usage example
# text_file = 'converted_text_file.txt'
# output_json = 'questions_and_answers4.json'

# # Parse text file and convert to JSON
# questions_data = parse_text_file_to_json(text_file)
# save_as_json(questions_data, output_json)
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
            text = line.strip()
            print(f"Line {line_num}: '{text}'")  # Debugging line-by-line output

            # Detect question line (e.g., "1. What is Zakat?")
            if re.match(r"^\d+\.\s", text):
                if question:  # Save previous question if it exists
                    questions_data.append({
                        "question": question,
                        "options": options,
                        "answer": answer
                    })
                # Start a new question block
                question = text
                options = []
                answer = None
                print(f"Detected question: '{question}'")  # Debugging output

            # Detect option line (e.g., "A: Option text")
            elif re.match(r"^[A-D]:", text):
                options.append(text)
                print(f"Detected option: '{text}'")  # Debugging output

            # Detect answer line (e.g., "Answer: A")
            elif text.startswith("Answer:"):
                answer = text.split("Answer:")[1].strip()
                print(f"Detected answer: '{answer}'")  # Debugging output

    # Add the last question after finishing the loop
    if question:
        questions_data.append({
            "question": question,
            "options": options,
            "answer": answer
        })

    return questions_data

# def parse_text_file_to_json(text_file):
#     """
#     Parses the text file to extract questions, options, and answers, and returns them in JSON format.
#     """
#     questions_data = []
#     question = None
#     options = []
#     answer = None

#     with open(text_file, 'r', encoding='utf-8') as file:
#         for line in file:
#             text = line.strip()

#             # Check if it's a question line (e.g., "1. What is Zakat?")
#             if re.match(r"^\d+\.\s", text):
#                 # Save the previous question block
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

#             # Check if it's an option line (e.g., "A:", "B:", etc.)
#             elif text.startswith(("A:", "B:", "C:", "D:")):
#                 options.append(text)

#             # Check if it's an answer line (e.g., "Answer: A")
#             elif text.startswith("Answer:"):
#                 answer = text.split("Answer:")[1].strip()

#     # Add the last question to the list
#     if question:
#         questions_data.append({
#             "question": question,
#             "options": options,
#             "answer": answer
#         })

#     return questions_data

def save_as_json(data, output_file):
    """
    Saves the parsed data to a JSON file.
    """
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to '{output_file}'")

# Combined usage
# docx_file = 'Objective-Type Questions and Answers on Financing Activities Guideline.docx'
docx_file='doc1.docx'
text_file = 'converted_text_file.txt'
output_json = 'questions_and_answers.json'

# Step 1: Convert .docx to plain text
convert_docx_to_text(docx_file, text_file)

# Step 2: Parse text file to JSON format
questions_data = parse_text_file_to_json(text_file)

# Step 3: Save data to JSON file
save_as_json(questions_data, output_json)

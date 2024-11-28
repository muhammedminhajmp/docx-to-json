import json
import re
from docx import Document

def extract_questions_from_docx(docx_file):
    # Load the document
    doc = Document(docx_file)

    questions_data = []
    question = None
    options = []
    answer = None

    for para in doc.paragraphs:
        text = para.text.strip()
        
        # Print each paragraph text to see how it's formatted in the document
        print("Processing paragraph:", text)

        # Detect a numbered question line (e.g., "1.", "2.")
        question_match = re.match(r"^\d+\.", text)
        if question_match:
            # Save the previous question block if exists
            if question:
                questions_data.append({
                    "question": question,
                    "options": options,
                    "answer": answer
                })
            # Start a new question block
            question = text
            options = []
            answer = None

        # Detect options (e.g., "A:", "B:", etc.)
        elif text.startswith(("A:", "B:", "C:", "D:")):
            options.append(text)

        # Detect answer line (e.g., "Answer: B")
        elif text.startswith("Answer:"):
            answer = text.split("Answer:")[1].strip()

    # Append the last question after exiting loop
    if question:
        questions_data.append({
            "question": question,
            "options": options,
            "answer": answer
        })

    return questions_data

def save_as_json(data, output_file):
    with open(output_file, 'w') as json_file:
        json.dump(data, json_file, indent=4)

# Usage
# docx_file = '/mnt/data/Objective-Type Questions and Answers on Financing Activities Guideline.docx'  # File path
# output_json = '/mnt/data/questions_and_answers.json'
docx_file = 'doc1.docx'  # File path
output_json = 'questions_and_answers2.json'
questions_data = extract_questions_from_docx(docx_file)
save_as_json(questions_data, output_json)

print(f"Data saved to {output_json}")

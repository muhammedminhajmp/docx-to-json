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

            # Replace Unicode apostrophe with a normal one
            text = text.replace("\u2019", "'")
            # Detect a question line by ending with "?" or starting with a number
            if text.endswith("?") or re.match(r"^\d+\.", text):
                text = re.sub(r'^\d+\.\s*', '', text)

                # Save the previous question block if it exists
                if question:
                    options = {
                        f"op{i+1}": re.sub(r'^[A-Za-z][.)\-\s]+', '', opt.strip())
                        for i, opt in enumerate(options) if opt.strip()
                    }

                    # Map answer to correct option key
                    if answer:
                        answer_label = re.match(r'^[a-dA-D]', answer)  # Extract just the option letter
                        if answer_label:
                            answer_letter = answer_label.group(0).lower()
                            answer = f"op{['a', 'b', 'c', 'd'].index(answer_letter) + 1}"

                    questions_data.append({
                        "question": question,
                        "options": options,
                        "answer": answer
                    })

                # Start a new question block
                question = text
                options = []
                answer = None

            # Detect options and answers embedded in the options line
            elif not text.startswith("Answer:") and question:
                if "Answer:" in text:
                    option_text, embedded_answer = text.split("Answer:")
                    options.append(option_text.strip())
                    answer = embedded_answer.strip()
                else:
                    options.append(text)

            # Standalone answer line (e.g., "Answer: B" or "Answer: b")
            elif text.startswith("Answer:"):
                answer = text.split("Answer:")[1].strip()

        # Handle the last question block after loop exits
        if question:
            options = {
                f"op{i+1}": re.sub(r'^[A-Za-z][.)\-\s]+', '', opt.strip())
                for i, opt in enumerate(options) if opt.strip()
            }
            if answer:
                answer_label = re.match(r'^[a-zA-Z]', answer)
                if answer_label:
                    answer_letter = answer_label.group(0).lower()
                    answer = f"op{['a', 'b', 'c', 'd'].index(answer_letter) + 1}"

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

# Define file paths
docx_file = 'Questions1.docx'
text_file = 'converted_text_file11.txt'
output_json = 'Questions1.json'

# Step 1: Convert .docx to plain text
convert_docx_to_text(docx_file, text_file)

# Step 2: Parse text file to JSON format
questions_data = parse_text_file_to_json(text_file)

# Step 3: Save data to JSON file
save_as_json(questions_data, output_json)

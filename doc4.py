import json
import re
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

            # Detect a question by checking if it ends with a "?" symbol
            if text.endswith("?"):
                # Save the previous question block before starting a new one
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

            # Detect an answer line (e.g., "Answer: A")
            elif text.startswith("Answer:"):
                answer = text.split("Answer:")[1].strip()

        # Append the last question block after exiting the loop
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
#                 # Add as an option if it doesn’t match answer or empty lines
#                 if text:
#                     options.append(text)

#             # Detect answer line (e.g., "Answer: A" or "Inventory Answer: C")
            
#             elif "Answer:" in text:
#                 answer = text.split("Answer:")[1].strip()

#         # Append the last question block after exiting the loop
#         if question:
#             questions_data.append({
#                 "question": question,
#                 "options": options,
#                 "answer": answer
#             })

#     return questions_data
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

#             # Detect options (e.g., lines starting with "A:", "B:", etc.)
#             elif re.match(r"^[A-D]:", text):
#                 options.append(text)

#             # Detect answer line (e.g., "Answer: A" or "Inventory Answer: C")
#             elif "Answer:" in text:
#                 answer = text.split("Answer:")[1].strip()

#         # Append the last question block after exiting the loop
#         if question:
#             questions_data.append({
#                 "question": question,
#                 "options": options,
#                 "answer": answer
#             })

#     return questions_data
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
#             print(f"Line {line_num}: '{text}'")  # Debugging line-by-line output

#             # Detect question line (e.g., "1. What is Zakat?")
#             if re.match(r"^\d+\.\s", text):
#                 if question:  # Save previous question if it exists
#                     questions_data.append({
#                         "question": question,
#                         "options": options,
#                         "answer": answer
#                     })
#                 # Start a new question block
#                 question = text
#                 options = []
#                 answer = None
#                 print(f"Detected question: '{question}'")  # Debugging output

#             # Detect option line (e.g., "A: Option text")
#             elif re.match(r"^[A-D]:", text):
#                 options.append(text)
#                 print(f"Detected option: '{text}'")  # Debugging output

#             # Detect answer line (e.g., "Answer: A")
#             elif text.startswith("Answer:"):
#                 answer = text.split("Answer:")[1].strip()
#                 print(f"Detected answer: '{answer}'")  # Debugging output

#     # Add the last question after finishing the loop
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

# Usage example
text_file = 'converted_text_file.txt'
output_json = 'questions_and_answers3.json'

# Parse text file and convert to JSON
questions_data = parse_text_file_to_json(text_file)
save_as_json(questions_data, output_json)

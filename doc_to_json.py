from docx import Document

def print_all_paragraphs(docx_file):
    # Load the document
    doc = Document(docx_file)
    
    # Print each paragraph with an index for debugging
    for i, para in enumerate(doc.paragraphs):
        print(f"Paragraph {i}: '{para.text.strip()}'")

# Usage
# docx_file = '/mnt/data/Objective-Type Questions and Answers on Financing Activities Guideline.docx'
docx_file = 'doc1.docx'  # File path
output_json = 'questions_and_answers2.json'
print_all_paragraphs(docx_file)

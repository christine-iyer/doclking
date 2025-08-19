# import pdfplumber
# import re

# def extract_fields(pdf_path):
#     with pdfplumber.open(pdf_path) as pdf:
#         text = ""
#         for page in pdf.pages:
#             text += page.extract_text() + "\n"

#     # Extract customer name (first non-empty line after "BILL TO")
#     customer_name = "Not found"
#     lines = [line.strip() for line in text.split('\n')]
#     for i, line in enumerate(lines):
#         if re.match(r'BILL TO$', line, re.IGNORECASE):
#             for next_line in lines[i+1:]:
#                 if next_line:
#                     customer_name = next_line
#                     break
#             break

#     # Find the subtotal amount
#     subtotal_match = re.search(r'Subtotal[^\d]*([\d,.]+)', text, re.IGNORECASE)
#     subtotal_value = subtotal_match.group(1).strip() if subtotal_match else "Not found"

#     # Find the field preceding the first "DATE"
#     preceding_field = "Not found"
#     lines_all = [line for line in lines if line]
#     for i, line in enumerate(lines_all):
#         if re.match(r'DATE\b', line, re.IGNORECASE):
#             if i > 0:
#                 preceding_field = lines_all[i - 1]
#             break

#     print(f"Customer Name: {customer_name}")
#     print(f"Subtotal: {subtotal_value}")
#     print(f"Field preceding first 'DATE': {preceding_field}")

# if __name__ == "__main__":
#     import sys
#     if len(sys.argv) < 2:
#         print("Usage: python pdf.py <path_to_pdf>")
#     else:
#         extract_fields(sys.argv[1])

# filepath: [pdf.py](http://_vscodecontentref_/0)
import pdfplumber
import re

def extract_customer(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() + "\n"

    # Split into lines and find "BILL TO"
    lines = [line.strip() for line in text.split('\n')]
    customer_name = "Not found"
    for i, line in enumerate(lines):
        if re.match(r'BILL TO$', line, re.IGNORECASE):
            # Look for the first non-empty line after "BILL TO"
            for next_line in lines[i+1:]:
                if next_line:
                    customer_name = next_line
                    break
            break

    print(f"Customer Name: {customer_name}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python pdf.py <path_to_pdf>")
    else:
        extract_customer(sys.argv[1])
# from docling.document_converter import DocumentConverter
# source = "https://arxiv.org/pdf/2206.01062" # PDF path or URL
# converter = DocumentConverter()
# result = converter.convert(source)
# markdown_content = result.document.export_to_markdown()

# with open("README.md", "w", encoding="utf-8") as f:
#     f.write(markdown_content)

# print("✅ Markdown exported to README.md") 

# ../data/statements.pdf
from docling.document_converter import DocumentConverter
import re
from pathlib import Path

from docling.document_converter import DocumentConverter
import re
from pathlib import Path

# Use absolute path or adjust relative path from scripts/ folder
source = str(Path(__file__).parent.parent / "data" / "statement.pdf")

converter = DocumentConverter()
result = converter.convert(source)

# Get the text content
text = result.document.export_to_markdown()

# First, let's see what the text looks like
print("📄 Extracted text preview:")
print("=" * 60)
print(text[:2000])  # Print first 2000 characters
print("=" * 60)

# Now let's search for ANY dates in December 2024
all_dates = re.findall(r'12/\d{1,2}/2024', text)
print(f"\n🔍 All December 2024 dates found: {set(all_dates)}")

# Let's also look for lines containing "balance" or dollar amounts
print("\n💰 Lines with dollar amounts:")
lines = text.split('\n')
for i, line in enumerate(lines[:50]):  # Check first 50 lines
    if re.search(r'\$[\d,]+\.\d{2}', line):
        print(f"Line {i}: {line}")

print("\n✅ Check the output above to see the actual format of your statement")
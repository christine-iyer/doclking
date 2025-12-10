from docling.document_converter import DocumentConverter
source = "https://arxiv.org/pdf/2206.01062" # PDF path or URL
converter = DocumentConverter()
result = converter.convert(source)
markdown_content = result.document.export_to_markdown()

with open("README.md", "w", encoding="utf-8") as f:
    f.write(markdown_content)

print("✅ Markdown exported to README.md") 

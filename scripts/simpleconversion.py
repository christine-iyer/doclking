from docling.document_converter import DocumentConverter
source = "https://arxiv.org/pdf/2206.01062" # PDF path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result) 

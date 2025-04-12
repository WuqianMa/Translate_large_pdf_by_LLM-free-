import os
from mistralai import Mistral
from mistralai.models import DocumentURLChunk

# Initialize Mistral client
api_key = os.getenv("MISTRAL_API_KEY")
client = Mistral(api_key=api_key)

# Specify your PDF file
pdf_filename = "The-Great-Cosmic-Mother.pdf"

# Upload the PDF file
with open(pdf_filename, "rb") as pdf_file:
    uploaded_file = client.files.upload(
        file={
            "file_name": pdf_filename,
            "content": pdf_file,
        },
        purpose="ocr",
    )

# Generate a signed URL for the uploaded file
signed_url = client.files.get_signed_url(file_id=uploaded_file.id, expiry=1)

# Process the document using OCR
ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=DocumentURLChunk(document_url=signed_url.url),
    include_image_base64=True
)

# Combine Markdown content from all pages
markdown_content = "\n\n".join(page.markdown for page in ocr_response.pages)

# Save the Markdown content to a file
with open("output.md", "w", encoding="utf-8") as md_file:
    md_file.write(markdown_content)

print("Markdown file created successfully: output.md")

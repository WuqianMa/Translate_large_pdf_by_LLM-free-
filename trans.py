import os
import time
import google.generativeai as genai

# Configure Gemini with API key
api_key=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=api_key)

# Load the Gemini model
model = genai.GenerativeModel("gemini-2.0-flash")

# Read your markdown file
input_filename = "output.md"
with open(input_filename, "r", encoding="utf-8") as file:
    md_text = file.read()


# Utility function to split text into smaller chunks
def split_markdown(text, max_chars=3500):
    chunks = []
    while len(text) > max_chars:
        split_point = text.rfind("\n", 0, max_chars)
        if split_point == -1:
            split_point = max_chars
        chunks.append(text[:split_point])
        text = text[split_point:]
    chunks.append(text)
    return chunks


# Split the markdown into chunks
chunks = split_markdown(md_text)

translated_md = ""
total_chunks = len(chunks)

# Set translation instructions
original_language = "English"
target_language = "Chinese"

# Process each chunk
start_from = 1  # Resuming from failed chunk

# Translate with retry
for i, chunk in enumerate(chunks[start_from - 1:], start=start_from):
    print(f"🔄 Translating chunk {i}/{total_chunks}...")

    prompt = (
        f"This is part {i} of a Markdown document originally written in {original_language}. "
        f"Please translate it into {target_language}, while strictly preserving all Markdown formatting "
        "(including headings, bullet points, numbered lists, bold/italic text, links, and code blocks). "
        "Translate in a fluent and natural style that reflects the voice of a Chinese-speaking feminist scholar, "
        "who is an expert in matriarchy, anthropology, and cosmology. "
        "Maintain an elegant, thoughtful tone appropriate for academic or spiritual discussions. "
        "Do not add explanations—just return the translated Markdown content.\n\n"
        f"{chunk}"
    )

    retry_delay = 3600  # initial retry wait time

    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            translated_md += response.text + "\n\n"
            print(f"✅ Completed chunk {i}/{total_chunks}")
            break  # exit retry loop on success
        except Exception as e:
            print(f"❌ Failed chunk {i} attempt {attempt+1}: {e}")
            if "429" in str(e) and attempt < 2:
                print(f"⏳ Waiting {retry_delay} seconds before retrying...")
                time.sleep(retry_delay)
                retry_delay *= 2  # exponential backoff
            else:
                translated_md += f"\n\n<!-- ERROR: Chunk {i} failed to translate -->\n\n"
                break





# Save final translated Markdown
output_filename = "trans.md"
with open(output_filename, "w", encoding="utf-8") as file:
    file.write(translated_md)



print(f"\n✅ All chunks processed. Markdown file saved as: {output_filename}")

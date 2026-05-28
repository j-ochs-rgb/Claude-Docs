import time
import os
import subprocess
from markitdown import MarkItDown

WATCH_FOLDER = os.path.expanduser("~/Claude-Docs/eingang")
OUTPUT_FOLDER = os.path.expanduser("~/Claude-Docs/markdown")
SUPPORTED = (".pdf", ".docx", ".pptx", ".xlsx", ".txt", ".csv")

os.makedirs(WATCH_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

md = MarkItDown()
print("Überwache Ordner... (Strg+C zum Beenden)")

seen = set()

while True:
    for file in os.listdir(WATCH_FOLDER):
        if file.endswith(SUPPORTED) and file not in seen:
            seen.add(file)
            input_path = os.path.join(WATCH_FOLDER, file)
            output_path = os.path.join(OUTPUT_FOLDER, file + ".md")
            print(f"Konvertiere: {file}")
            result = md.convert(input_path)
            with open(output_path, "w") as f:
                f.write(result.text_content)
            subprocess.run(["git", "add", "."], cwd=os.path.expanduser("~/Claude-Docs"))
            subprocess.run(["git", "commit", "-m", f"Add {file}"], cwd=os.path.expanduser("~/Claude-Docs"))
            subprocess.run(["git", "push"], cwd=os.path.expanduser("~/Claude-Docs"))
            print(f"Fertig: {file}.md auf GitHub!")
    time.sleep(5)

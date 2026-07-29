import sys
import markdown
from xhtml2pdf import pisa

CSS = """
<style>
  @page { size: A4; margin: 2cm; }
  body { font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; line-height: 1.45; color: #1a1a1a; }
  h1 { font-size: 18pt; border-bottom: 2px solid #24476E; padding-bottom: 6px; margin-top: 0; }
  h2 { font-size: 14pt; color: #24476E; margin-top: 22px; border-bottom: 1px solid #ccc; padding-bottom: 3px; }
  h3 { font-size: 12pt; color: #24476E; margin-top: 16px; }
  p { margin: 6px 0; text-align: justify; }
  table { border-collapse: collapse; width: 100%; margin: 10px 0; font-size: 9.5pt; }
  th, td { border: 1px solid #999; padding: 5px 8px; text-align: left; }
  th { background-color: #DCE4EC; font-weight: bold; }
  code { background-color: #f0f0f0; padding: 1px 4px; font-family: Courier, monospace; font-size: 9pt; }
  pre { background-color: #f0f0f0; padding: 8px; font-size: 9pt; }
  blockquote { border-left: 3px solid #A66A2E; margin: 8px 0; padding: 4px 12px; background-color: #fff8ee; }
  hr { border: none; border-top: 1px solid #ccc; margin: 16px 0; }
  ul, ol { margin: 4px 0; padding-left: 22px; }
  li { margin: 3px 0; }
  strong { color: #000; }
  .meta { font-size: 8.5pt; color: #666; }
</style>
"""

def convert(md_path, pdf_path):
    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Strip YAML frontmatter (between --- lines) and render as a small meta block instead
    meta_html = ""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            frontmatter = text[3:end].strip()
            text = text[end + 4:].lstrip("\n")
            meta_lines = "<br/>".join(l.strip() for l in frontmatter.splitlines() if l.strip())
            meta_html = f'<p class="meta">{meta_lines}</p><hr/>'

    body_html = markdown.markdown(text, extensions=["tables", "fenced_code", "sane_lists"])
    full_html = f"<html><head>{CSS}</head><body>{meta_html}{body_html}</body></html>"

    with open(pdf_path, "wb") as out:
        result = pisa.CreatePDF(full_html, dest=out)
    if result.err:
        print(f"ERROR converting {md_path}", file=sys.stderr)
        return False
    return True

if __name__ == "__main__":
    md_path = sys.argv[1]
    pdf_path = sys.argv[2]
    ok = convert(md_path, pdf_path)
    print("OK" if ok else "FAILED")

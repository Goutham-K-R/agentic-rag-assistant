import re

def clean_text(text: str) -> str:
    """Remove Markdown images and extra whitespace."""
    text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
    return text.strip()

def safe_filename(title: str) -> str:
    """Create filesystem-friendly filename from title."""
    cleaned = re.sub(r"[^\w\s-]", "", title)
    return cleaned.replace(" ", "_")[:50]

from typing import List


def split_text(text: str, chunk_size: int = 200) -> List[str]:
    """Split text into smaller chunks."""
    words = text.split()
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def search_keyword(text: str, keyword: str) -> List[str]:
    """Return sentences that contain the keyword."""
    sentences = text.split(".")
    keyword = keyword.lower()

    matches = [
        sentence.strip()
        for sentence in sentences
        if keyword in sentence.lower()
    ]

    return matches

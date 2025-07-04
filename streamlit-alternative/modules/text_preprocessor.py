# modules/text_preprocessor.py
    
from langchain.text_splitter import CharacterTextSplitter

def preprocess_text(text, chunk_size=1000, chunk_overlap=100):
    """
    Splits raw text into chunks using Langchain's CharacterTextSplitter.
    
    Args:
        text (str): The full text to be split.
        chunk_size (int): The maximum size of each chunk.
        chunk_overlap (int): The number of overlapping characters between chunks.

    Returns:
        List[str]: A list of text chunks.
    """
    splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = splitter.split_text(text)
    return chunks
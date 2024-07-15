from src.leafnode import LeafNode

def main():
    # Create a LeafNode instance
    paragraph = LeafNode("p", "This is a paragraph of text.")
    print(paragraph.to_html())
    # Output: <p>This is a paragraph of text.</p>

    # Creating an anchor LeafNode with attributes
    link = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(link.to_html())
    # Output: <a href
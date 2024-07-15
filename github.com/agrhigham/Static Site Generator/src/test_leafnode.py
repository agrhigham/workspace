import unittest
from src.leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    
    def test_leaf_node_creation(self):
        node = LeafNode("p", "This is a paragraph.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph.</p>")
    
    def test_leaf_node_with_props(self):
        props = {"href": "https://www.google.com"}
        node = LeafNode("a", "Click me!", props)
        self.assertEqual(node.to_html(), '<a href="https://www.google.com">Click me!</a>')
    
    def test_leaf_node_without_value(self):
        with self.assertRaises(ValueError):
            LeafNode("p", "")
    
    def test_leaf_node_without_tag(self):
        node = LeafNode(None, "Raw text")
        self.assertEqual(node.to_html(), "Raw text")

if __name__ == '__main__':
    unittest.main()
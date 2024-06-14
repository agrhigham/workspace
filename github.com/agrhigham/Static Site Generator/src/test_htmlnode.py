import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_HTMLNode(self):
        node = HTMLNode(tag='a', props={"href": "https://www.google.com", "target": "_blank"})
        expected_repr = "Tag: a, Value: None, Children: None, Props: {'href': 'https://www.google.com', 'target': '_blank'}"
        self.assertEqual(repr(node), expected_repr)
        expected_props_html = 'href="https://www.google.com" target="_blank"'
        self.assertEqual(node.props_to_html(), expected_props_html)


if __name__ == "__main__":
    unittest.main()
from .htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        # Call to the HTMLNode constructor to initialize `tag` and `props`
        super().__init__(tag=tag, value=value, props=props)
        
        # Ensure the value is provided
        if value is None or value == "":
            raise ValueError("LeafNode requires a value")
        
    def to_html(self):
        if self.tag:
            props_str = self.props_to_html() if self.props else ""
            if props_str:
                return f'<{self.tag} {props_str}>{self.value}</{self.tag}>'
            else:
                return f'<{self.tag}>{self.value}</{self.tag}>'
        else:
            return self.value
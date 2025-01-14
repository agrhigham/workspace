class HTMLNode:
    def __init__(self,tag=None, value=None, children=None, props=None):
       self.tag = tag
       self.value = value
       self.children = children
       self.props = props

    def props_to_html(self):
        props_list = []
        for key, value in self.props.items():
            props_list.append(f"{key}=\"{value}\"")
        return " ".join(props_list)
        
    def __repr__(self):
        return f"Tag: {self.tag}, Value: {self.value}, Children: {self.children}, Props: {self.props}"
        
        
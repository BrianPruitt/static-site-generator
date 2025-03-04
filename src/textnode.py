from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC_ = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    
    def __eq__(self, node_two):
        return (
            self.text == node_two.text 
            and self.text_type == node_two.text_type 
            and self.url == node_two.url
        )
        
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

from htmlnode import HTMLNode
from textnode import TextNode, TextType

def main():
    print(TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev"))
    print(HTMLNode("a", "Click here", [], {"href": "https://www.google.com", "target": "_blank"}))

main()
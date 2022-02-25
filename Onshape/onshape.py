from onshape_client.client import OAuthAuthorizationMethods
from onshape_client import OnshapeElement, Client

client = Client(keys_file="./config.yaml")

element = OnshapeElement("https://cad.onshape.com/documents/30822f0b8d537ef9bc7389fa/w/7a9bada48aac9a7c2ee37f89/e/3cec8f0f9e1492dbd67f2150")

print(element.elements())

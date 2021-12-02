import base64

img = 'iVBORw0KGgoAAAANSUhEUgAAASwAAACWCAYAAABkW7XSAAAAAXNSR0IArs4c6QAABGJJREFUeF7t1AEJAAAMAsHZv/RyPNwSyDncOQIECEQEFskpJgECBM5geQICBDICBitTlaAECBgsP0CAQEbAYGWqEpQAAYPlBwgQyAgYrExVghIgYLD8AAECGQGDlalKUAIEDJYfIEAgI2CwMlUJSoCAwfIDBAhkBAxWpipBCRAwWH6AAIGMgMHKVCUoAQIGyw8QIJARMFiZqgQlQMBg+QECBDICBitTlaAECBgsP0CAQEbAYGWqEpQAAYPlBwgQyAgYrExVghIgYLD8AAECGQGDlalKUAIEDJYfIEAgI2CwMlUJSoCAwfIDBAhkBAxWpipBCRAwWH6AAIGMgMHKVCUoAQIGyw8QIJARMFiZqgQlQMBg+QECBDICBitTlaAECBgsP0CAQEbAYGWqEpQAAYPlBwgQyAgYrExVghIgYbAYGWqEpQAAYPlBwgQyAgYrExVghIgYLD8AAECGQGDlalKUAIEDJYfIEAgI2CwMlUJSoCAwfIDBAhkBAxWpipBCRAwWH6AAIGMgMHKVCUoAQIGyw8QIJARMFiZqgQlQMBg+QECBDICBitTlaAECBgsP0CAQEbAYGWqEpQAAYPlBwgQyAgYrExVghIgYLD8AAECGQGDlalKUAIEDJYfIEAgI2CwMlUJSoCAwfIDBAhkBAxWpipBCRAwWH6AAIGMgMHKVCUoAQIGyw8QIJARMFiZqgQlQMBg+QECBDICBitTlaAECBgsP0CAQEbAYGWqEpQAAYPlBwgQyAgYrExVghIgYLD8AAECGQGDlalKUAIEDJYfIEAgI2CwMlUJSoCAwfIDBAhkBAxWpipBCRAwWH6AAIGMgMHKVCUoAQIGyw8QIJARMFiZqgQlQMBg+QECBDICBitTlaAECBgsP0CAQEbAYGWqEpQAgQdWMQCX4yW9owAAAABJRU5ErkJgg'
png = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x01,\x00\x00\x00\x96\x08\x06\x00\x00\x00d[\xb5\xd2\x00\x00\x00\x01sRGB\x00\xae\xce\x1c\xe9\x00\x00\x04bIDATx^\xed\xd4\x01\t\x00\x00\x0c\x02\xc1\xd9\xbf\xf4r<\xdc\x12\xc89\xdc9\x02\x04\x08D\x04\x16\xc9)&\x01\x02\x04\xce`y\x02\x02\x042\x02\x06+S\x95\xa0\x04\x08\x18,?@\x80@F\xc0`e\xaa\x12\x94\x00\x01\x83\xe5\x07\x08\x10\xc8\x08\x18\xacLU\x82\x12 `\xb0\xfc\x00\x01\x02\x19\x01\x83\x95\xa9JP\x02\x04\x0c\x96\x1f @ #`\xb02U\tJ\x80\x80\xc1\xf2\x03\x04\x08d\x04\x0cV\xa6*A\t\x100X~\x80\x00\x81\x8c\x80\xc1\xcaT%(\x01\x02\x06\xcb\x0f\x10 \x90\x110X\x99\xaa\x04%@\xc0`\xf9\x01\x02\x042\x02\x06+S\x95\xa0\x04\x08\x18,?@\x80@F\xc0`e\xaa\x12\x94\x00\x01\x83\xe5\x07\x08\x10\xc8\x08\x18\xacLU\x82\x12 `\xb0\xfc\x00\x01\x02\x19\x01\x83\x95\xa9JP\x02\x04\x0c\x96\x1f @ #`\xb02U\tJ\x80\x80\xc1\xf2\x03\x04\x08d\x04\x0cV\xa6*A\t\x100X~\x80\x00\x81\x8c\x80\xc1\xcaT%(\x01\x02\x06\xcb\x0f\x10 \x90\x110X\x99\xaa\x04%@\xc0`\xf9\x01\x02\x042\x02\x06+S\x95\xa0\x04\x08\x18,?@\x80@F\xc0`e\xaa\x12\x94\x00\x01\x83\xe5\x07\x08\x10\xc8\x08\x18\xacLU\x82\x12 a\xb0\x18\x19j\x84\xa5\x00\x00`\xf9A\xc2\x042\x02\x06+\x13\x15`\x84\x88\x18,?\x00\x00@\x86@`\xe5jR\x94\x00\x81\x03%\x87\xc8\x10\x08\x08\xd8,\x0c\x95BR\xa0 0|\x80\xc1\x02\x19\x01\x03\x15\xa9\x8a\x90BD\x0c\x16\x1f\xa0\x00 c 0r\x95\tJ\x00@\x81\xb2\xc3\xc4\x08$\x04L\x16&j\x81\tP0\x18>@@\x81\x0c\x80\x81\x8a\xd4\xe5h\x01\x02\x06\x0b\x0f\xd0 \x10\x11\xb0\x18\x19j\x84\xa5\x00\x00`\xf9A\xc2\x042\x02\x06+\x13\x15`\x84\x88\x18,?\x00\x00@\x86@`\xe5jR\x94\x00\x81\x03%\x87\xc8\x10\x08\x08\xd8,\x0c\x95BR\xa0 0|\x80\xc1\x02\x19\x01\x03\x15\xa9\x8a\x90BD\x0c\x16\x1f\xa0\x00 c 0r\x95\tJ\x00@\x81\xb2\xc3\xc4\x08$\x04L\x16&j\x81\tP0\x18>@@\x81\x0c\x80\x81\x8a\xd4\xe5h\x01\x02\x06\x0b\x0f\xd0 \x10\x11\xb0\x18\x19j\x84\xa5\x00\x00`\xf9A\xc2\x042\x02\x06+\x13\x15`\x84\x88\x18,?\x00\x00@\x86@`\xe5jR\x94\x00\x81\x03%\x87\xc8\x10\x08\x08\xd8,\x0c\x95BR\xa0 0|\x80\xc1\x02\x19\x01\x03\x15\xa9\x8a\x90BD\x0c\x16\x1f\xa0\x00 c 0r\x95\tJ\x00@\x81\xb2\xc3\xc4\x08$\x04L\x16&j\x81\tP0\x18>@@\x81\x0c\x80\x81\x8a\xd4\xe5h\x01\x02\x06\x0b\x0f\xd0 \x10\x11\xb0\x18\x19j\x84\xa5\x00 A\xd5\x8c@%\xf8\xc9oh\xc0\x00\x00\x00\x12QS\x91+\x90\x98 '

print(base64.b64decode(img))
with open('./img2', 'wb') as buffer:
    buffer.write(png)
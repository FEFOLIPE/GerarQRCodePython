import pyqrcode
import png
from pyqrcode import QRCode

# Link para gerar o QRCode
link = "https://github.com/FEFOLIPE/"

# Gerando o QRCode
url = pyqrcode.create(link)

# Salvando a imagem
url.png(r'imagem.png', scale=8)

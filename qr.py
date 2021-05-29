import pyqrcode as pqr 
import png 
from pyqrcode import QRCode 

# String which stores the Link of the Web site to create
s = input("enter the link for which you want generate QR Code: ")
  
# Generate QR code for the entered link or website 
url = pqr.create(s) 
  
# Create and save the svg file naming "myqr.svg" 
#url.svg("myqr.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
url.png('QRcode.png', scale = 6) 
print("Completed")
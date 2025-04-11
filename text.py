from PIL import Image
import pytesseract
import time

# Load the image
image = Image.open('img5.png')

# Start timing
start_time = time.time()

# Perform OCR
text = pytesseract.image_to_string(image)

# End timing
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time

# Output the result
print("Extracted text:")
print(text)
print(f"\n Time taken: {elapsed_time:.4f} seconds")


"""
Llegue a una conclusion con  pytesseract, podrias ayudarme a escribirlo mejor y de mejor forma no se:

Con pytsseract hice 5 imagenes 

img - 700 x 400 pixeles - cantidad de palabra 24 palabras - tiempo de procesamiento: 0.376 s
img2 - 522 x 325 pixeles - cantidad de palabra 252 palabras - tiempo de procesamiento: 1.103 s
img3 - 3000 x 2000 pixeles - cantidad de palabra 1 - tiempo de procesamiento: 2.994 s
img4 (misma imagen 3) - 640 x 480 pixeles - cantidad de palabra 1 - tiempo de procesamiento: 0.317 s
img5 (misma imagen 5) - 128 x 128 pixeles - cantidad de palabra 1 - tiempo de procesamiento: 0.104 s 



"""

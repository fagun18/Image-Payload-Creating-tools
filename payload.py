from PIL import Image
import base64

# Open the original image
with Image.open("original.jpg") as img:
    # Encode the payload as a base64 string
    payload = base64.b64encode(b"your payload here").decode()
    # Add the payload to the image
    img.info["Description"] = payload
    # Save the new image
    img.save("payload.jpg")

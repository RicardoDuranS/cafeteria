import base64


def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode("utf-8")
    return encoded_string


# Ejemplo de uso
image_path = "OIP.jpg"
encoded_image = image_to_base64(image_path)
print(encoded_image)

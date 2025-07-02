import base64
import os

def get_local_img(path: str):
    file_extension = os.path.splitext(path)[1][1:]
    print(file_extension)
    with open(path, "rb") as f:
        data = f.read()
        encoded = base64.b64encode(data)
    data = "data:image/" + file_extension + ";base64," + encoded.decode("utf-8")
    return data
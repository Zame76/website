from PIL import Image
from io import BytesIO
import base64

def processPhoto(response):
    # base64photo = ("data:" + response.headers['Content-Type'] + ";base64, " + str(base64.b64encode(response.content).decode("utf-8")))
    base64photo = str(base64.b64encode(response.content).decode("utf-8"))
    image = Image.open(BytesIO(base64.b64decode(base64photo)))
    new_image = image.resize((640, 360))
    buffered = BytesIO()
    new_image.save(buffered, format="JPEG")
    b64string = "data:" + response.headers['Content-Type'] + ";base64, " + str(base64.b64encode(buffered.getvalue()).decode("utf-8"))
    return b64string

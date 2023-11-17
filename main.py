from fastapi import FastAPI, File, UploadFile
import numpy as np
import cv2 as cv2
from pyzbar import pyzbar

app = FastAPI()

DEBUGGING = False


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/upload")
async def upload(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        numpy_arr = np.fromstring(contents, np.uint8)
        img = cv2.imdecode(numpy_arr, cv2.IMREAD_COLOR)

        barcodes = pyzbar.decode(img)
        barcode_dict_arr = []
        for barcode in barcodes:
            x, y, w, h = barcode.rect
            # partially for debugging
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 4)
            bdata = barcode.data.decode("utf-8")
            btype = barcode.type
            text = f"{bdata},{btype}"
            cv2.putText(img, text, (x - 50, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            bcode = {
                "data": bdata,
                "type": btype
            }

            barcode_dict_arr.append(bcode)

        # For Debugging
        if DEBUGGING:
            cv2.imshow("img", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        # end debugging

    except Exception:
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()

    return {"barcodes": barcode_dict_arr}

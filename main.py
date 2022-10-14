import uvicorn
from fastapi import FastAPI, File, UploadFile

from model import read_imagefile, preprocess, predict_imagefile


app = FastAPI()


@app.post("/predict/image")
async def predict_api(file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"

    image = read_imagefile(await file.read())

    img_array = preprocess(image)

    prediction = predict_imagefile(img_array)

    return prediction


if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000, debug=True)
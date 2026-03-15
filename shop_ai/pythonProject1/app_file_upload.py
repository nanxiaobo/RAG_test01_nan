import uvicorn, os
from fastapi import FastAPI, UploadFile

app = FastAPI()
UPLOAD_FILE = "upload_file"
if not os.path.exists(UPLOAD_FILE):
    os.mkdir(UPLOAD_FILE)


@app.post("/upload")
async def upload_file(file: UploadFile):
    filename = file.filename

    content = await file.read()
    text = content.decode("utf-8")
    # print(text)
    save_file = os.path.join(UPLOAD_FILE, filename)
    with open(save_file, "w", encoding="utf-8") as f:
        f.write(text)

    return {
        "filename": filename,
        "file_path": save_file,
        "file_size": len(save_file)}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)


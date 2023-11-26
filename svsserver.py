from fastapi import FastAPI
from fastapi import UploadFile
from fastapi.responses import FileResponse
from fastapi import File
from typing import Union
from pydantic import BaseModel
import os
app = FastAPI()

@app.get("/generate_voice")
def generate_voice(file: UploadFile = File(...)):

    with open(f"./raw/{file.filename}", 'wb') as f:
        for i in iter(lambda: file.file.read(1024 * 1024 * 10), b''):
            f.write(i)
    
    command = f'python inference_main.py -m "logs/44k/G_22250.pth" -c "configs/config.json" -n "{file.filename}" -t 0 -s "alxy"'
    os.system(command)

    return FileResponse(f"./results/{file.filename}_0key_alxy_sovits_pm.flac", media_type="audio/flac")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="192.168.0.106", port=8000)

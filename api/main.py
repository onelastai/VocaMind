from fastapi import FastAPI, UploadFile
from src.transcribe import transcribe_audio
from src.analyze import analyze_text
from src.db import save_transcript

app = FastAPI()

@app.post('/upload')
async def upload_audio(file: UploadFile):
    path = f'data/{file.filename}'
    with open(path, 'wb') as f:
        f.write(await file.read())
    transcript = transcribe_audio(path)
    save_transcript(file.filename, transcript)
    return {'transcript': transcript}

@app.post('/analyze')
async def analyze(call_id: str, transcript: str):
    result = analyze_text(transcript)
    return {'analysis': result}

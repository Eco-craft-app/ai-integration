from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import asyncio
import json
import os

from prompts.expert_chat import ExpertChat
from prompts.recycling_guidance import RecyclingGuide
from prompts.upcycling_ideas import UpcyclingIdeas
from prompts.waste_detection import WasteDetection
from prompts.recycling_guidance2 import RecyclingGuide2

from utils.image_fetcher import fetch_image
from utils.logging_config import log_execution, logger

api_key = os.getenv("GEMINI_API_KEY", "")

expert_chat = ExpertChat(api_key)
recycling_guide = RecyclingGuide(api_key)
upcycling_ideas = UpcyclingIdeas(api_key)
waste_detection = WasteDetection(api_key)
recycling_guide2 = RecyclingGuide2(api_key)

app = FastAPI()


class MessageModel(BaseModel):
    Message: str


class PhotoModel(BaseModel):
    Photo_URL: str


class UpcyclingTextModel(BaseModel):
    Message: list[dict]


@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request: {request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response


@log_execution
@app.post('/expert')
async def expert_endpoint(data: MessageModel):
    response = await expert_chat.generate_response(data.Message)
    return {"response": response}


@log_execution
@app.post('/detect')
async def waste_detect(data: PhotoModel):
    image = await fetch_image(data.Photo_URL)
    response = await waste_detection.generate_response(image)
    return {"response": response}


@log_execution
@app.post('/recycling_text')
async def recycling_text_endpoint(data: MessageModel):
    response = await recycling_guide.generate_response(data.Message)
    return {"response": response}


@log_execution
@app.post('/recycling_photo')
async def recycling_photo_endpoint(data: PhotoModel):
    image = await fetch_image(data.Photo_URL)
    response = await recycling_guide2.generate_response(image)
    cleaned = response.split("```json\n")[1].split("```")[0].replace("'", '"')
    return {"response": json.loads(cleaned)}


@log_execution
@app.post('/recycling_photo_2')
async def recycling_photo_endpoint_2(data: PhotoModel):
    photo = await fetch_image(data.Photo_URL)
    described_photo = await waste_detection.generate_response(photo)
    response = await recycling_guide.generate_response(described_photo)
    cleaned = response.split("```json\n")[1].split("```")[0]
    return {"response": json.loads(cleaned)}


@log_execution
@app.post('/upcycling_text')
async def upcycling_endpoint(data: UpcyclingTextModel):
    json_string = json.dumps(data.Message, ensure_ascii=False, indent=4)
    response = await upcycling_ideas.generate_response(json_string)
    return {"response": json.loads(response)}


@log_execution
@app.post('/upcycling_photo')
async def upcycling_photo_endpoint(data: PhotoModel):
    image = await fetch_image(data.Photo_URL)
    items = await recycling_guide2.generate_response(image)
    cleaned = items.split("```json\n")[1].split("```")[0].replace("'", '"')
    data = [{"item": entry["item"], "details": entry["details"]} for entry in json.loads(cleaned)]
    json_string = json.dumps(data, ensure_ascii=False, indent=4)
    response = await upcycling_ideas.generate_response(json_string)
    cleaned_response = response.split("```json\n")[0].split("```")[0]
    return {"response": json.loads(cleaned_response)}


# To run the FastAPI server
if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=1234)

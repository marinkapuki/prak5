from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

# Список для хранения отзывов
feedbacks: List[Feedback] = []

@app.post("/feedback")
async def send_feedback(feedback: Feedback):
    # Добавляем отзыв в список
    feedbacks.append(feedback)
    
    # Возвращаем ответ
    return {
        "message": f"Feedback received. Thank you, {feedback.name}!"
    }

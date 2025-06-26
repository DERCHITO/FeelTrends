from fastapi import FastAPI, Query
from services.twitter_collector import get_tweets
from services.youtube_collector import get_youtube_comments
from services.instagram_collector import get_instagram_comments
from services.sentiment_analysis import analyze_sentiment
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

    return {"message": "Sentimientos API - MVP"}

@app.get("/analizar/twitter")
def analizar_twitter(query: str = Query(...), count: int = 10):
    tweets = get_tweets(query, count, BEARER_TOKEN)
    return _analizar_textos(tweets)

@app.get("/analizar/youtube")
def analizar_youtube(video_id: str = Query(...), count: int = 10):
    comments = get_youtube_comments(video_id, YOUTUBE_API_KEY, count)
    return _analizar_textos(comments)

@app.get("/analizar/instagram")
def analizar_instagram(media_id: str = Query(...)):
    comments = get_instagram_comments(media_id, INSTAGRAM_ACCESS_TOKEN)
    return _analizar_textos(comments)

def _analizar_textos(textos):
    resultados = []
    for text in textos:
        analisis = analyze_sentiment(text)
        resultados.append({
            "texto": text,
            "score": analisis["score"],
            "magnitude": analisis["magnitude"]
        })
    return {"resultado": resultados}

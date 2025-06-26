import requests
from typing import List

def get_youtube_comments(video_id: str, api_key: str, max_results: int = 20) -> List[str]:
    url = "https://www.googleapis.com/youtube/v3/commentThreads"
    params = {
        "part": "snippet",
        "videoId": video_id,
        "maxResults": min(max_results, 100),
        "key": api_key,
        "textFormat": "plainText"
    }

    response = requests.get(url, params=params)
    data = response.json()

    comments = [
        item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
        for item in data.get("items", [])
    ]
    return comments

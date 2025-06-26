import requests
from typing import List

def get_instagram_comments(media_id: str, access_token: str) -> List[str]:
    url = f"https://graph.facebook.com/v18.0/{media_id}/comments"
    params = {
        "access_token": access_token,
        "fields": "text",
        "limit": 50
    }

    response = requests.get(url, params=params)
    data = response.json()

    comments = [item["text"] for item in data.get("data", [])]
    return comments

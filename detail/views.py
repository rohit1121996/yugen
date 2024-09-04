import json
import os
from django.shortcuts import render
import requests
from functools import lru_cache
from watch.utils import get_all_episode_metadata, get_from_redis_cache, store_in_redis_cache

def detail(request, anime_id):
    anime_data = get_anime_data(anime_id)
    if not anime_data:
        return render(request, "detail/error.html", {"error": "Anime not found"}, status=404)

    anime_episodes = get_anime_episodes(anime_id)
    
    if anime_episodes:
        attach_episode_metadata(anime_data, anime_episodes)

    context = {
        "anime": anime_data,
        "episodes": anime_episodes,
    }

    return render(request, "detail/detail.html", context)

@lru_cache(maxsize=100)
def get_anime_data(anime_id):
    cache_key = f"anime_{anime_id}_anime_data"
    anime_data = get_from_redis_cache(cache_key)
    
    if not anime_data:
        base_url = f"{os.getenv('CONSUMET_URL')}/meta/anilist/info/{anime_id}?provider=zoro"
        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            anime_data = response.json()
            if anime_data["status"] == "Completed":
                store_in_redis_cache(cache_key, json.dumps(anime_data), 3600 * 24 * 30)  # Cache for 30 days
            else:
                store_in_redis_cache(cache_key, json.dumps(anime_data), 3600 * 12) # Cache for 12 hours
        except requests.RequestException as e:
            print(f"Error fetching anime data for ID {anime_id}: {e}")
            return None
    else:
        anime_data = json.loads(anime_data)
    
    return anime_data

@lru_cache(maxsize=100)
def get_anime_episodes(anime_id):
    cache_key = f"anime_{anime_id}_anime_episodes"
    anime_episodes = get_from_redis_cache(cache_key)
    
    if not anime_episodes:
        anime_data = get_anime_data(anime_id)
        if not anime_data or not anime_data.get("episodes"):
            return None

        z_anime_id = anime_data["episodes"][0]["id"].split("$")[0]
        base_url = f"{os.getenv('ZORO_URL')}/anime/episodes/{z_anime_id}"
        try:
            response = requests.get(base_url, timeout=10)
            response.raise_for_status()
            anime_episodes = response.json()
            store_in_redis_cache(cache_key, json.dumps(anime_episodes), 86400)  # Cache for 24 hours
        except requests.RequestException as e:
            print(f"Error fetching anime episodes for ID {anime_id}: {e}")
            return None
    else:
        anime_episodes = json.loads(anime_episodes)
    
    return anime_episodes

def attach_episode_metadata(anime_data, anime_episodes):
    anime_episodes_metadata = get_all_episode_metadata(anime_data)
    if anime_episodes_metadata:
        for i, episode in enumerate(anime_episodes.get("episodes", [])):
            if i < len(anime_episodes_metadata):
                episode["metadata"] = anime_episodes_metadata[i]
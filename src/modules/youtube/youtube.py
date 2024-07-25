import os
from dataclasses import dataclass
from typing import List, Dict
import requests

from youtubesearchpython import VideosSearch

from src.modules.youtube.consts import (
    DEFAULT_NUMBER_OF_VIDEOS,
    MAX_DESCRIPTION_LENGTH,
)


@dataclass
class VideoData:
    title: str
    url: str
    duration: str
    views: str
    channel: str
    description: str
    published_time: str


class YoutubeConnector:
    @staticmethod
    def play_video(url: str) -> None:
        main_pc_ip = os.environ.get("MAIN_PC_IP")
        requests.post(f"http://{main_pc_ip}:8001/play_video", data={"url": url})

    @staticmethod
    def search_videos(
        text_to_search: str, number_of_videos: int = DEFAULT_NUMBER_OF_VIDEOS
    ) -> List[VideoData]:
        result: Dict = VideosSearch(text_to_search, limit=number_of_videos).result()
        return [
            VideoData(
                title=video["title"],
                url=video["link"],
                duration=video["duration"],
                views=video["viewCount"]["short"],
                channel=video["channel"]["name"],
                description="\n".join(
                    line["text"] for line in video["descriptionSnippet"]
                )[:MAX_DESCRIPTION_LENGTH],
                published_time=video["publishedTime"],
            )
            for video in result["result"]
        ]


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=S9uTScSgzrM"
    YoutubeConnector.play_video(video_url)
    # results = YoutubeConnector.search_videos("good music")
    # x = 1

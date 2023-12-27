import time
import webbrowser
from dataclasses import dataclass
from typing import List, Dict

import pyautogui
from youtubesearchpython import VideosSearch

from src.modules.youtube.consts import (
    DEFAULT_NUMBER_OF_VIDEOS,
    DEFAULT_TIME_TO_WAIT,
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
    def play_video(url: str, time_to_wait: int = DEFAULT_TIME_TO_WAIT) -> None:
        browser = webbrowser.get()
        browser.open(url)
        time.sleep(time_to_wait)  # give it a couple seconds to load
        firefox_window = pyautogui.getWindowsWithTitle("Firefox")[0]
        firefox_window.activate()
        pyautogui.press("space")

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

import time
import webbrowser

import pyautogui

from src.modules.youtube.consts import DEFAULT_TIME_TO_WAIT
from youtube_search import YoutubeSearch

class YoutubeConnector:
    @staticmethod
    def play_video(url: str, time_to_wait: int = DEFAULT_TIME_TO_WAIT) -> None:
        webbrowser.open(url)
        time.sleep(time_to_wait)  # give it a couple seconds to load
        pyautogui.press("space")

    @staticmethod
    def search_and_play_video(text_to_search: str) -> str:
        print("searching for: ", text_to_search)
        # videosSearch = VideosSearch(text_to_search, limit=1)
        # YoutubeConnector.play_video(videosSearch.resultComponents[0]["link"])
        return "The video has been played."

    @staticmethod
    def search_video(text_to_search: str) -> str:
        pass


if __name__ == "__main__":
    # video_url = "https://www.youtube.com/watch?v=S9uTScSgzrM"
    # YoutubeConnector.play_video(video_url)
    YoutubeConnector.search_and_play_video("good music")

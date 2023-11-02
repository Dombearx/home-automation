import time
import webbrowser

from src.modules.youtube.consts import DEFAULT_TIME_TO_WAIT

# import pyautogui


class YoutubeConnector:
    @staticmethod
    def play_video(url, time_to_wait: int = DEFAULT_TIME_TO_WAIT):
        webbrowser.open(url)
        time.sleep(time_to_wait)  # give it a couple seconds to load
        # pyautogui.press("space")

    @staticmethod
    def search_and_play_video(text_to_search: str) -> str:
        print("searching for: ", text_to_search)
        # videosSearch = VideosSearch(text_to_search, limit=1)
        # YoutubeConnector.play_video(videosSearch.resultComponents[0]["link"])
        return "The video has been played."


if __name__ == "__main__":
    # video_url = "https://www.youtube.com/watch?v=S9uTScSgzrM"
    # YoutubeConnector.play_video(video_url)
    YoutubeConnector.search_and_play_video("good music")

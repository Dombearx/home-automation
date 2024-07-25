import time
import webbrowser
import pyautogui

from consts import (
    DEFAULT_TIME_TO_WAIT,
)


class YoutubeConnector:
    @staticmethod
    def play_video(url: str, time_to_wait: int = DEFAULT_TIME_TO_WAIT) -> None:
        browser = webbrowser.get()
        browser.open(url)
        time.sleep(time_to_wait)  # give it a couple seconds to load
        firefox_window = pyautogui.getWindowsWithTitle("Firefox")[0]
        firefox_window.activate()
        pyautogui.press("space")


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=S9uTScSgzrM"
    YoutubeConnector.play_video(video_url)
    # results = YoutubeConnector.search_videos("good music")
    # x = 1

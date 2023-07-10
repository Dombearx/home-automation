import time
import webbrowser

import pyautogui

from src.modules.youtube.consts import DEFAULT_TIME_TO_WAIT


class YoutubeConnector:
    @staticmethod
    def play_video(url, time_to_wait: int = DEFAULT_TIME_TO_WAIT):
        webbrowser.open(url)
        time.sleep(time_to_wait)  # give it a couple seconds to load
        pyautogui.press("space")


if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=S9uTScSgzrM"
    YoutubeConnector.play_video(video_url)

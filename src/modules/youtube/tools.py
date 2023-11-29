import json
from typing import Optional, Type

from langchain.callbacks.manager import (
    AsyncCallbackManagerForToolRun,
    CallbackManagerForToolRun,
)
from langchain.tools import BaseTool
from pydantic import BaseModel, Field

from src.modules.youtube.consts import DEFAULT_NUMBER_OF_VIDEOS
from src.modules.youtube.youtube import YoutubeConnector


class YouTubeSearchSchema(BaseModel):
    text_to_search: str = Field(
        description="should be a text that will be used to search for videos"
    )
    num_results: int = Field(
        description=f"should be a number of videos to return, default is {DEFAULT_NUMBER_OF_VIDEOS}",
        default=DEFAULT_NUMBER_OF_VIDEOS,
    )


class YouTubeSearchTool(BaseTool):
    """Tool that queries YouTube."""

    name: str = "youtube_search"
    description: str = (
        "search for youtube videos associated with passed text "
        "return videos urls and basic information about them: "
        "title, duration, views, description, channel name, published time."
    )
    args_schema: Type[YouTubeSearchSchema] = YouTubeSearchSchema

    def _run(
        self,
        text_to_search: str,
        num_results: int = DEFAULT_NUMBER_OF_VIDEOS,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        results = YoutubeConnector.search_videos(text_to_search, num_results)
        return json.dumps([result.__dict__ for result in results])

    async def _arun(
        self,
        text_to_search: str,
        num_results: int = DEFAULT_NUMBER_OF_VIDEOS,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")


class YouTubePlayVideoSchema(BaseModel):
    url: str = Field(description="should be a url of video to play")


class YouTubePlayVideoTool(BaseTool):
    """Tool that queries YouTube."""

    name: str = "youtube_play_video"
    description: str = "plays YouTube video from given url."
    args_schema: Type[YouTubePlayVideoSchema] = YouTubePlayVideoSchema

    def _run(
        self,
        url: str,
        run_manager: Optional[CallbackManagerForToolRun] = None,
    ) -> str:
        """Use the tool."""
        YoutubeConnector.play_video(url)
        return "Video played!"

    async def _arun(
        self,
        url: str,
        run_manager: Optional[AsyncCallbackManagerForToolRun] = None,
    ) -> bool:
        """Use the tool asynchronously."""
        raise NotImplementedError("custom_search does not support async")

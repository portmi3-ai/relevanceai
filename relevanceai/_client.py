from __future__ import annotations

import os
from typing import TYPE_CHECKING
import httpx

if TYPE_CHECKING:
    from . import resources

from ._base_client import SyncAPIClient, AsyncAPIClient


class RelevanceAI(SyncAPIClient):

    agents: resources.AgentsManager
    tasks: resources.Tasks
    tools: resources.ToolsManager
    knowledge: resources.Knowledge
    oauth: resources.OAuthManager

    api_key: str
    region: str | None
    project: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        region: str | None = None,
        project: str | None = None,
        base_url: str | httpx.URL | None = None,
    ) -> None:

        if api_key is None:
            api_key = os.environ.get("RAI_API_KEY")
        if api_key is None:
            raise ValueError("API key is required")
        self.api_key = api_key

        if region is None:
            region = os.environ.get("RAI_REGION")
        if region is None:
            raise ValueError("Region is required")
        self.region = region

        if project is None:
            project = os.environ.get("RAI_PROJECT")
        if project is None:
            raise ValueError("Project is required")
        self.project = project

        headers = {"Authorization": f"{self.project}:{self.api_key}"}
        base_url = f"https://api-{self.region}.stack.tryrelevance.com/latest"

        super().__init__(base_url=base_url, headers=headers)

        from . import resources

        self.agents = resources.AgentsManager(self)
        self.tasks = resources.Tasks(self)
        self.tools = resources.ToolsManager(self)
        self.knowledge = resources.Knowledge(self)
        self.oauth = resources.OAuthManager(self)


class AsyncRelevanceAI(AsyncAPIClient):
    agents: resources.AsyncAgentsManager
    tasks: resources.AsyncTasks
    tools: resources.AsyncToolsManager
    knowledge: resources.AsyncKnowledge

    api_key: str
    region: str | None
    project: str | None

    def __init__(
        self,
        *,
        api_key: str | None = None,
        region: str | None = None,
        project: str | None = None,
        base_url: str | httpx.URL | None = None,
    ) -> None:

        if api_key is None:
            api_key = os.environ.get("RAI_API_KEY")
        if api_key is None:
            raise ValueError("API key is required")
        self.api_key = api_key

        if region is None:
            region = os.environ.get("RAI_REGION")
        if region is None:
            raise ValueError("Region is required")
        self.region = region

        if project is None:
            project = os.environ.get("RAI_PROJECT")
        if project is None:
            raise ValueError("Project is required")
        self.project = project

        headers = {"Authorization": f"{self.project}:{self.api_key}"}
        base_url = f"https://api-{self.region}.stack.tryrelevance.com/latest"

        super().__init__(base_url=base_url, headers=headers)

        from . import resources

        self.agents = resources.AsyncAgentsManager(self)
        self.tasks = resources.AsyncTasks(self)
        self.tools = resources.AsyncToolsManager(self)
        self.knowledge = resources.AsyncKnowledge(self)

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()


if __name__ == "__main__":

    client = RelevanceAI()

from hunterx.core.logger import logger
from hunterx.core.plugin import Plugin


class TestPlugin(Plugin):

    name = "test"

    description = "Test plugin"

    async def execute(self, target: str) -> None:

        logger.info(f"Running Test Plugin against {target}")

        logger.success("Plugin finished.")
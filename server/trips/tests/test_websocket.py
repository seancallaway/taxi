import pytest
from channels.testing import WebsocketCommunicator

from taxi.asgi import application

TEST_CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}


@pytest.mark.asyncio
class TestWebsocket:

    async def test_can_connect_to_server(self, settings):
        settings.CHANNEL_LAYERS = TEST_CHANNEL_LAYERS
        communicator = WebsocketCommunicator(
            application=application,
            path='/taxi/',
        )
        connected, _ = await communicator.connect()
        assert connected is True
        await communicator.disconnect()

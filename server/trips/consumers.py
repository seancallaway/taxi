from channels.generic.websocket import AsyncJsonWebsocketConsumer


class TaxiConsumer(AsyncJsonWebsocketConsumer):
    groups = ['test']

    async def connect(self):
        await self.channel_layer.group_add(
            group='test',
            channel=self.channel_name,
        )
        await self.accept()

    async def disconnect(self, code):
        await self.channel_layer.group_discard(
            group='test',
            channel=self.channel_name,
        )
        await super().disconnect(code)

    async def echo_message(self, msg):
        await self.send_json({
            'type': msg.get('type'),
            'data': msg.get('data'),
        })

    async def receive_json(self, content, **kwargs):
        message_type = content.get('type')
        if message_type == 'echo.message':
            await self.echo_message(content)

import asyncio
from aiohttp import web
import os

from mouse import MouseEventHandler
from camera import CameraHandler
from sqlite_db import save_to_database

REFRESH_TIME = 0.01
TAKE_PHOTO_ON = 'Released'  # Mouse button being either 'Pressed' or 'Released'


def get_event_data(last_mouse_event: dict):
    event_type = last_mouse_event['event_type']
    data = {
        'event_type': event_type,
        'x': last_mouse_event['x'],
        'y': last_mouse_event['y']
    }
    if event_type == 'click':
        for data_point in {'button', 'action'}:
            data[data_point] = last_mouse_event[data_point]

    return data


def left_mouse_button_clicked(data):
    return (data['event_type'] == 'click'
            and data['action'] == TAKE_PHOTO_ON
            and 'left' in data['button'])


async def websocket_handler(request):
    mouse = MouseEventHandler()
    camera = CameraHandler()

    ws = web.WebSocketResponse()
    await ws.prepare(request)

    try:
        mouse.start_listening()
        previous_event = {}

        while True:
            last_mouse_event = mouse.get_last_event()

            if last_mouse_event and last_mouse_event != previous_event:
                event_data = get_event_data(last_mouse_event)
                await ws.send_json(event_data)
                if left_mouse_button_clicked(event_data):
                    await camera.take_picture()
                    await save_to_database(event_data['x'], event_data['y'], camera.absolute_file_path)
                    await ws.send_json({'image_path': camera.relative_file_path})

            await asyncio.sleep(REFRESH_TIME)
            previous_event = last_mouse_event

    finally:
        mouse.stop_listening()
        await ws.close()


async def http_handler(request):
    return web.FileResponse('index.html')


async def image_handler(request):
    filename = request.match_info.get('filename')
    file_path = os.path.join(os.path.dirname(__file__), 'images', filename)

    if os.path.exists(file_path):
        return web.FileResponse(file_path)
    else:
        return web.Response(status=404)

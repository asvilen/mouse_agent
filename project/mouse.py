from pynput.mouse import Listener


class MouseEventHandler:
    def __init__(self):
        self.last_event = None
        self.listener = None

    def on_move(self, x, y):
        self.last_event = {'event_type': 'move', 'x': x, 'y': y}

    def on_click(self, x, y, button, pressed):
        action = 'Pressed' if pressed else 'Released'
        self.last_event = {'event_type': 'click', 'x': x, 'y': y, 'button': str(button), 'action': action}

    def start_listening(self):
        self.listener = Listener(on_move=self.on_move, on_click=self.on_click)
        self.listener.start()

    def stop_listening(self):
        if self.listener:
            self.listener.stop()
            self.listener.join()

    def get_last_event(self):
        return self.last_event

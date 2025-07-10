import json
import requests
class NotionAPI:
    def __init__(self, token):
        self.token = token
        self.base_url = "https://api.notion.com/v1/"

    def _headers(self):
        return 
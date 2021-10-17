import requests
import json
import warnings

from dataclasses import asdict
from anki_helpers.models import AddNoteRequest

ANKI_CONNECT_URL = 'http://localhost:8765'

class AnkiConnectClient:
    def __init__(self):
        if not self.is_online():
            warnings.warn(f'Anki connect is not installed or anki is not open')

    def is_online(self):
        try:
            requests.head(ANKI_CONNECT_URL)
        except requests.exceptions.ConnectionError:
            return False

        return True

    def browse_notes(self, query):
        params = {
            'query': query
        }
        request_body = self._create_request_body('findNotes', params)
        request_json = json.dumps(request_body)
        response = requests.post(ANKI_CONNECT_URL, data=request_json)
        return response.json()['result']

    def get_notes(self, note_ids):
        params = {
            'notes': note_ids
        }
        request_body = self._create_request_body('notesInfo', params)
        request_json = json.dumps(request_body)
        response = requests.post(ANKI_CONNECT_URL, data=request_json)
        return response.json()['result']


    def add_note(self, request: AddNoteRequest):
        params = {
            'note': asdict(request)
        }
        return self._make_request(params)


    def _create_request_body(self, action, params):
        return {
            'action': action,
            'version': 6,
            'params': params
        }

    def _make_request(self, params):
        request_body = self._create_request_body('addNote', params)
        request_json = json.dumps(request_body)
        response = requests.post(ANKI_CONNECT_URL, data=request_json)
        return response.json()['result']

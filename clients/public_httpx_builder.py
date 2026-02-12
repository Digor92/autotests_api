from httpx import Client
from clients.event_hooks import curl_event_hook, log_request_event_hook, log_response_event_hook
from config import settings

def get_public_http_client() -> Client:
    """
    фуункция создает экземпляр httpx.Client с базовыми насройками
    return: готовый к сипользованию объектр httpx.Client
    """
    return Client(timeout = settings.http_client.timeout,# Таймаут теперь берётся из настроек
                  base_url = settings.http_client.client_url, # Базовый URL также из настроек
                  event_hooks = {"request": [curl_event_hook, log_request_event_hook],
                                 "response": [log_response_event_hook]} ) # Добавляем event hook для запроса
from httpx import Client

def get_public_http_client() -> Client:
    """
    фуункция создает экземпляр httpx.Client с базовыми насройками
    return: готовый к сипользованию объектр httpx.Client
    """
    return Client(timeout = 100,
                  base_url = 'http://localhost:8000')
import httpx


def test(name):
    return f"hello world {name}"

def hello():
    response = httpx.get('https://google.com')
    return response.content

print(hello())

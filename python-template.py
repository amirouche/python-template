from loguru import logger as log


async def uvicorn(scope, receive, send):
    log.debug(scope)

    if scope["type"] == "lifespan":
        return

    await send(
        {
            "type": "http.response.start",
            "status": 200,
            "headers": [
                [b"content-type", b"text/plain"],
            ],
        }
    )

    await send(
        {
            "type": "http.response.body",
            "body": b"Hello, hacker, and happy hacking!",
        }
    )


def test_success():
    assert True

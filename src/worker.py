from uvicorn.workers import UvicornWorker


class NotesWorker(UvicornWorker):
    CONFIG_KWARGS = {
        'host': '0.0.0.0',
        'port': '8000'
    }

from app.config import Settings, Environment


class AppBuilder():
    ''' Application builder. This class keeps the logic of app bootstrapping  '''

    def __init__(self):
        self.settings: Settings = Environment.select()

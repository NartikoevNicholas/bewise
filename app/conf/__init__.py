from app.conf.settings import DefaultSettings


def get_setting() -> DefaultSettings:
    return DefaultSettings()


settings = get_setting()

__app__ = [
    'settings'
]

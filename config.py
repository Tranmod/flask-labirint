import os


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'asfdasdgasdgas56406asdg6w53gfasd'

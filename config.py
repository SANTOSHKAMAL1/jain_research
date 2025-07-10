import os

class Config:
    SECRET_KEY = '53c16457dad3b471352cfda5ccf3a1a5'

    MONGO_URI = os.environ.get('MONGO_URI') or \
        'mongodb+srv://jainresearch:jain@cluster0.9imrqqp.mongodb.net/jain?retryWrites=true&w=majority&appName=Cluster0'

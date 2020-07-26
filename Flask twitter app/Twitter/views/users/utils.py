import secrets, os
from PIL import Image

from flask import current_app

def save_picture(picture):
    picture_fn = get_picture_fn(picture)
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)

    i = Image.open(picture)
    i = i.resize((200,200))
    i.thumbnail((200,200))
    i.save(picture_path)

    return picture_fn


def save_header(picture):
    picture_fn = get_picture_fn(picture)
    picture_path = os.path.join(current_app.root_path, 'static/headers', picture_fn)

    i = Image.open(picture)
    i = i.resize((578,230))
    i.save(picture_path)

    return picture_fn


def get_picture_fn(picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture.filename)
    picture_fn = random_hex + f_ext

    return picture_fn
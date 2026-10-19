import openai
import os
from dotenv import load_dotenv
import re


def test_api_key() -> str:
    load_dotenv()
    env_api_key = str(os.environ.get('OPEN_AI_API_KEY'))
    identifier = (re.search('sk-', env_api_key).span() == (0, 3))
    check_if_string = isinstance(env_api_key, str)
    if len(env_api_key) == 51 and check_if_string is True and identifier is True:
        return env_api_key
    raise Exception("Invalid API key! Please check that the right key has been inserted.")


def set_api_key():
    api_key = test_api_key()
    print(api_key)
    openai.api_key = api_key


def set_organisation(has_organisation=False):
    if has_organisation:
        load_dotenv()
        openai.organization = os.environ.get('ORGANISATION_ID')


def get_model_list():
    print(openai.Model.list())


def get_model_description(model):
    print(openai.Model.retrieve(model))


# Written responses
def create_request(chosen_model: str, **kwargs):
    set_api_key()
    request = openai.Completion.create(model=chosen_model, **kwargs)
    return request


def create_chat_request(chosen_model: str, role: str, content_of_message: str, **kwargs):
    set_api_key()
    messages = [{'role': role, 'content': content_of_message, 'name': kwargs.get('name', None)}]
    message_request = openai.Completion.create(model=chosen_model, messages=messages, **kwargs)
    return message_request


def create_edit_request(model: str, instruction: str, **kwargs):
    edit_message = openai.Edit.create(model=model, instruction=instruction, **kwargs)
    return edit_message


# Image AI

def create_image(prompt: str, **kwargs):
    image_request = openai.Image.create(prompt=prompt, **kwargs)
    return image_request


def create_edit_image_request(image: str, prompt: str, **kwargs):
    edit_image_request = openai.Image.create(image=image, prompt=prompt, **kwargs)
    return edit_image_request


def create_image_variation(image: str, **kwargs):
    image_variation = openai.Image.create_variation(image=image, **kwargs)
    return image_variation


# Embeddings

def create_embedding(model: str, input_request: str | list, **kwargs):
    embedding = openai.Embedding.create(model=model, input=input_request, **kwargs)
    return embedding


# Audio AI

def create_transcription(file: str, model: str, **kwargs):
    transcription = openai.Audio.transcribe(file=file, model=model, **kwargs)
    return transcription


def create_translation(file: str, model: str, **kwargs):
    translation = openai.Audio.translate(file=file, model=model, **kwargs)


# For editing Files

def list_files():
    return openai.File.list()


def upload_file(file: str, purpose: str):
    openai.File.create(file=file, purpose=purpose)


def delete_file(file_id: str):
    openai.File.delete(file_id)


def retrieve_file(file_id: str):
    return openai.File.retrieve(file_id)


def retrieve_content(file_id: str):
    return openai.File.download(file_id)

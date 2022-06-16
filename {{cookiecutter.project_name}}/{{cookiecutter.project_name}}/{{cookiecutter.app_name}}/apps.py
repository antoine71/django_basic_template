from django.apps import AppConfig


class {{cookiecutter.app_name.capitalize()|replace('_', '')}}Config(AppConfig):
    name = '{{cookiecutter.project_name}}.{{cookiecutter.app_name}}'

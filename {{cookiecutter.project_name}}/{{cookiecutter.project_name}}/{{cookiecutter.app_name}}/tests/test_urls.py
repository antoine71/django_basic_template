from django.urls import resolve, reverse


def test_index():
    assert reverse('{{cookiecutter.app_name}}:index') == '/{{cookiecutter.app_name}}/'
    assert resolve('/{{cookiecutter.app_name}}/').view_name == '{{cookiecutter.app_name}}:index'


def test_address():
    assert reverse('{{cookiecutter.app_name}}:address', kwargs={'address_id': 1}) == '/{{cookiecutter.app_name}}/1/'
    assert resolve('/{{cookiecutter.app_name}}/1/').view_name == '{{cookiecutter.app_name}}:adress'

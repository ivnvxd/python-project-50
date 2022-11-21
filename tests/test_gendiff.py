import pytest

from gendiff.diff import generate_diff


@pytest.fixture
def json():
    link = {}
    link['before'] = './tests/fixtures/file1.json'
    link['after'] = './tests/fixtures/file2.json'
    link['result'] = './tests/fixtures/result_json.txt'
    return link


@pytest.fixture
def yaml():
    link = {}
    link['before'] = './tests/fixtures/file1.yml'
    link['after'] = './tests/fixtures/file2.yml'
    link['result'] = './tests/fixtures/result_yaml.txt'
    return link


def test_generate_diff(json):
    with open(json['result']) as file:
        expected = file.read()    
    assert generate_diff(json['before'], json['after']) == expected


def test_generate_diff_yaml(yaml):
    with open(yaml['result']) as file:
        expected = file.read()    
    assert generate_diff(yaml['before'], yaml['after']) == expected

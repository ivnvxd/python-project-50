import pytest

from gendiff.diff import generate_diff


@pytest.fixture
def json_plain():
    link = {}
    link['before'] = './tests/fixtures/file1_plain.json'
    link['after'] = './tests/fixtures/file2_plain.json'
    link['result'] = './tests/fixtures/result_plain.txt'
    return link


@pytest.fixture
def yaml_plain():
    link = {}
    link['before'] = './tests/fixtures/file1_plain.yml'
    link['after'] = './tests/fixtures/file2_plain.yml'
    link['result'] = './tests/fixtures/result_plain.txt'
    return link


@pytest.fixture
def json_nested():
    link = {}
    link['before'] = './tests/fixtures/file1_nested.json'
    link['after'] = './tests/fixtures/file2_nested.json'
    link['result'] = './tests/fixtures/result_nested.txt'
    return link


@pytest.fixture
def yaml_nested():
    link = {}
    link['before'] = './tests/fixtures/file1_nested.yaml'
    link['after'] = './tests/fixtures/file2_nested.yaml'
    link['result'] = './tests/fixtures/result_nested.txt'
    return link

def test_json_plain(json_plain):
    with open(json_plain['result']) as file:
        expected = file.read()    
    assert generate_diff(json_plain['before'], json_plain['after'], '') == expected


def test_yaml_plain(yaml_plain):
    with open(yaml_plain['result']) as file:
        expected = file.read()    
    assert generate_diff(yaml_plain['before'], yaml_plain['after'], '') == expected


def test_json_nested(json_nested):
    with open(json_nested['result']) as file:
        expected = file.read()
    assert generate_diff(json_nested['before'], json_nested['after'], '') == expected


def test_yaml_nested(yaml_nested):
    with open(yaml_nested['result']) as file:
        expected = file.read()
    assert generate_diff(yaml_nested['before'], yaml_nested['after'], '') == expected

import pytest

from gendiff.diff import generate_diff


@pytest.fixture
def links():
    link = {}
    link['before'] = './tests/fixtures/file1.json'
    link['after'] = './tests/fixtures/file2.json'
    link['result'] = './tests/fixtures/result_json.txt'
    return link


def test_generate_diff(links):
    with open(links['result']) as file:
        expected = file.read()    
    assert generate_diff(links['before'], links['after']) == expected

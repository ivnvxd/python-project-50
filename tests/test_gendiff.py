import pytest

from gendiff.diff import generate_diff


@pytest.fixture
def files():
    links = {
        'file1_json_flat': './tests/fixtures/json/file1_flat.json',
        'file1_yml_flat': './tests/fixtures/yaml/file1_flat.yml',
        'file1_yaml_flat': './tests/fixtures/yaml/file1_flat.yaml',
        'file2_json_flat': './tests/fixtures/json/file2_flat.json',
        'file2_yml_flat': './tests/fixtures/yaml/file2_flat.yml',
        'file2_yaml_flat': './tests/fixtures/yaml/file2_flat.yaml',

        'file1_json_nested': './tests/fixtures/json/file1_nested.json',
        'file1_yml_nested': './tests/fixtures/yaml/file1_nested.yml',
        'file1_yaml_nested': './tests/fixtures/yaml/file1_nested.yaml',
        'file2_json_nested': './tests/fixtures/json/file2_nested.json',
        'file2_yml_nested': './tests/fixtures/yaml/file2_nested.yml',
        'file2_yaml_nested': './tests/fixtures/yaml/file2_nested.yaml',

        'stylish_flat': './tests/fixtures/result/stylish_flat.txt',
        'stylish_nested': './tests/fixtures/result/stylish_nested.txt',

        'plain_flat': './tests/fixtures/result/plain_flat.txt',
        'plain_nested': './tests/fixtures/result/plain_nested.txt',
    }
    return links


def test_stylish_flat(files):
    with open(files['stylish_flat']) as file:
        expected = file.read()
    assert generate_diff(files['file1_json_flat'], files['file2_json_flat'], 'stylish') == expected
    assert generate_diff(files['file1_yml_flat'], files['file2_yml_flat'], 'stylish') == expected
    assert generate_diff(files['file1_yaml_flat'], files['file2_yaml_flat'], 'stylish') == expected


def test_stylish_nested(files):
    with open(files['stylish_nested']) as file:
        expected = file.read()
    assert generate_diff(files['file1_json_nested'], files['file2_json_nested'], 'stylish') == expected
    assert generate_diff(files['file1_yml_nested'], files['file2_yml_nested'], 'stylish') == expected
    assert generate_diff(files['file1_yaml_nested'], files['file2_yaml_nested'], 'stylish') == expected


def test_plain_flat(files):
    with open(files['plain_flat']) as file:
        expected = file.read()
    assert generate_diff(files['file1_json_flat'], files['file2_json_flat'], 'plain') == expected
    assert generate_diff(files['file1_yml_flat'], files['file2_yml_flat'], 'plain') == expected
    assert generate_diff(files['file1_yaml_flat'], files['file2_yaml_flat'], 'plain') == expected


def test_plain_nested(files):
    with open(files['plain_nested']) as file:
        expected = file.read()
    assert generate_diff(files['file1_json_nested'], files['file2_json_nested'], 'plain') == expected
    assert generate_diff(files['file1_yml_nested'], files['file2_yml_nested'], 'plain') == expected
    assert generate_diff(files['file1_yaml_nested'], files['file2_yaml_nested'], 'plain') == expected

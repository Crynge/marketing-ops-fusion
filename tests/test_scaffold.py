from pathlib import Path


def test_readme_exists():
    assert Path('README.md').exists()


def test_source_tree_exists():
    assert Path('src').exists()

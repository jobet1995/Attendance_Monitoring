import pytest
import os


def pytest_runtest_protocol(item, nextitem):
    if "github_workflow" in item.keywords and "GITHUB_WORKFLOW" in os.environ:
        pytest.skip("Bypassing test in GitHub workflow")
    return None  # continues with the default protocol

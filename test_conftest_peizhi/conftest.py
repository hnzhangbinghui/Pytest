
import pytest


@pytest.fixture(scope="module", autouse=True)
def first():
    print("\n第一步先运行conftest脚本")













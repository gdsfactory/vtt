import pathlib

import pytest
from gdsfactory.component import Component
from gdsfactory.difftest import difftest
from pytest_regressions.data_regression import DataRegressionFixture

from gvtt import cells

skip_test: set[str] = set()
cell_names = set(cells.keys()) - set(skip_test)
dirpath_ref = pathlib.Path(__file__).absolute().parent / "ref"


@pytest.fixture(params=cell_names, scope="function")
def component(request: pytest.FixtureRequest) -> Component:
    return cells[request.param]()


def test_pdk_gds(component: Component) -> None:
    """Avoid regressions in GDS geometry, cell names and layers."""
    difftest(component, dirpath=dirpath_ref)


def test_pdk_settings(
    component: Component, data_regression: DataRegressionFixture
) -> None:
    """Avoid regressions when exporting settings."""
    data_regression.check(component.to_dict())

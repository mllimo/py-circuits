import pytest
import pyray as pr

from libs.MVC.models.grid_model import GridModel
from libs.MVC.controllers.grid_controller import GridController
from libs.MVC.controllers.component_controller import ComponentController


@pytest.fixture
def grid_controller():
    return GridController()


def test_set_color(grid_controller: GridController):
    new_color = pr.RED
    grid_controller.set_color(new_color)
    assert grid_controller.get_color() == new_color


def test_set_rows_columns(grid_controller: GridController):
    new_size = pr.Vector2(5, 5)
    grid_controller.set_rows_columns(new_size)
    assert grid_controller.get_rows_columns() == new_size


def test_set_size(grid_controller: GridController):
    new_size = pr.Vector2(100, 100)
    grid_controller.set_size(new_size)
    assert new_size == grid_controller.get_size()


def test_set_at(grid_controller: GridController):
    element = ComponentController()
    x, y = 2, 3
    grid_controller.set_at(x, y, element)
    cell = grid_controller.get_at(x, y)
    assert cell.get_content() == element


def test_get_at(grid_controller: GridController):
    element = ComponentController()
    x, y = 1, 1
    grid_controller.set_at(x, y, element)
    cell = grid_controller.get_at(x, y)
    assert cell.get_content() == element


def test_collide_with_index(grid_controller: GridController):
    rect = pr.Rectangle(0, 0, 10, 10)
    index = grid_controller.collide_with_index(rect)
    assert isinstance(index, pr.Vector2)

import pytest
import pyray as pr

from libs.MVC.models.grid_model import GridModel
from libs.MVC.controllers.grid_controller import GridController
from libs.MVC.controllers.component_controller import ComponentController
from libs.MVC.models.component_model import ComponentModel


@pytest.fixture
def grid_controller():
    grid = GridController()
    new_size = pr.Vector2(5, 5)
    grid.set_rows_columns(new_size)
    return grid


def test_set_color(grid_controller: GridController):
    new_color = pr.RED
    grid_controller.set_color(new_color)
    assert grid_controller.get_color() == new_color


def test_set_rows_columns(grid_controller: GridController):
    new_size = pr.Vector2(10, 10)
    grid_controller.set_rows_columns(new_size)
    assert pr.vector2_equals(grid_controller.get_rows_columns(), new_size)


def test_set_size(grid_controller: GridController):
    new_size = pr.Vector2(100, 100)
    grid_controller.set_size(new_size)
    assert pr.vector2_equals(grid_controller.get_size(), new_size)


def test_set_at(grid_controller: GridController):
    element = ComponentController(ComponentModel(), None)
    x, y = 2, 3
    grid_controller.set_at(x, y, element)
    cell = grid_controller.get_at(x, y)
    assert cell.get_content() == element


def test_get_at(grid_controller: GridController):
    element = ComponentController(ComponentModel(), None)
    x, y = 1, 1
    grid_controller.set_at(x, y, element)
    cell = grid_controller.get_at(x, y)
    assert cell.get_content() == element


def test_collide_with_index(grid_controller: GridController):
    new_size = pr.Vector2(100, 100)
    rect = pr.Rectangle(10, 10, 10, 10)
    grid_controller.set_size(new_size)
    index = grid_controller.collide_with_index(rect)
    assert index is not None

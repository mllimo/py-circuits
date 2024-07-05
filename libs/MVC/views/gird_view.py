import pyray as pr
from pyray import RED

from libs.MVC.models.grid_model import GridModel
from libs.MVC.views.component_view import ComponentView


class GridView(ComponentView):
    def __init__(self):
        super().__init__()


    def display(self, model: GridModel):
        current_pos = model.get_position()
        grid_size = model.get_rows_columns()

        for y in range(0, int(grid_size.y)):
            for x in range(0, int(grid_size.x)):
                cell = model.get_at(x, y)
                pr.draw_rectangle(int(current_pos.x), int(current_pos.y), cell.get_width(), cell.get_height(), model.get_color())
                pr.draw_rectangle_lines(int(current_pos.x), int(current_pos.y), cell.get_width(), cell.get_height(), pr.BLACK)
                current_pos.x += cell.get_width()

            current_pos.y += model.get_at(0, y).get_height()
            current_pos.x = model.get_position().x

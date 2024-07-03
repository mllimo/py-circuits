import pyray as pr
from pyray import RED

from MVC.models.grid_model import GridModel
from MVC.views.component_view import ComponentView


class GridView(ComponentView):
    def __init__(self):
        super().__init__()


    def display(self, model: GridModel):
        current_pos = model.get_position()
        grid_size = model.get_rows_columns()

        for y in range(0, int(grid_size.y)):
            for x in range(0, int(grid_size.x)):
                cell = model.at(x, y)
                pr.draw_rectangle(int(current_pos.x), int(current_pos.y), cell.width, cell.height, model.get_color())
                pr.draw_rectangle_lines(int(current_pos.x), int(current_pos.y), int(cell.width), int(cell.height), pr.BLACK)
                current_pos.x += cell.width

            current_pos.y += model.at(0, y).height
            current_pos.x = model.get_position().x

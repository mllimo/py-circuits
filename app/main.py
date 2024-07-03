from typing import Tuple
import enum

import pyray as pr

from MVC.controllers.box_controller import BoxController
from MVC.controllers.cursor_controller import CursorController
from MVC.controllers.grid_controller import GridController


pr.init_window(800, 450, "Hello Pyray")
pr.set_target_fps(60)

camera = pr.Camera2D()


def run():
    texture = pr.load_texture("C:/workspace/Electronics/assets/GameIcon.jpg")

    grid = GridController()
    grid.set_position(pr.Vector2(0, 0))
    grid.set_rows_columns(pr.Vector2(5, 5))
    grid.set_size(pr.Vector2(800, 450))
    

    cursor = CursorController()

    box = BoxController(pr.Rectangle(100, 100, 60, 60))
    box.set_color(pr.YELLOW)
    box.set_texture(texture)


    while not pr.window_should_close():
        # events

        # logic
        cursor.set_position(pr.get_mouse_position())
        
        if pr.is_mouse_button_pressed(pr.MouseButton.MOUSE_BUTTON_LEFT):
            raycast = pr.Rectangle(pr.get_mouse_position().x, pr.get_mouse_position().y, 1, 1)
            collide = pr.check_collision_recs(box.get_rect(), raycast)
            if collide:
                cursor.set_selection(box)


        if cursor.get_selection() is not None and pr.is_mouse_button_down(pr.MouseButton.MOUSE_BUTTON_LEFT):
            cursor.get_selection().set_position(cursor.get_position())
            
        if pr.is_mouse_button_released(pr.MouseButton.MOUSE_BUTTON_LEFT):
            cursor.set_selection(None)

        collision_index = grid.collide_with_index(box.get_rect())
        if collision_index is not None:
            print(f'Colliding with pos {collision_index.x},{collision_index.y}')
            if cursor.get_selection() is not None:
                grid.set_at(collision_index.x, collision_index.y, cursor.get_selection())


        # draw
        pr.clear_background(pr.BLACK)
        pr.begin_drawing()

        grid.display()
        box.display()
        
        pr.draw_fps(10, 10)
        pr.end_drawing()

    pr.close_window()
import pyray as pr


from MVC.models.box_model import BoxModel
from MVC.views.component_view import ComponentView


class BoxView(ComponentView):
    def __init__(self, color: pr.Color = pr.RED, texture: pr.Texture2D = None):
        super().__init__()
        self.color = color
        self.texture = texture


    def display(self, model: BoxModel):
        if self.texture:
            pr.draw_texture_pro(
                self.texture, 
                pr.Rectangle(0, 0, self.texture.width, self.texture.height),
                model.get_rectangle(),
                pr.Vector2(0, 0),
                0,
                pr.WHITE
            )
        else:
            pr.draw_rectangle_rec(model.get_rectangle(), self.color)
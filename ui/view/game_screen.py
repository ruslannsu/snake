from typing import List, Tuple
import arcade

class GameScreen(arcade.Window):
    def __init__(self, screen_width, screen_height, sidebar_width, grid_size) -> None:
        super().__init__(width=screen_width, height=screen_height, title="Змейка")
        
        arcade.set_background_color(arcade.color.WHITE)

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.sidebar_width = sidebar_width
        self.grid_size = grid_size
        self.grid_width = (self.screen_width - self.sidebar_width) // self.grid_size
        self.grid_height = self.screen_height // self.grid_size
        
        self.init_game()
    
    def init_game(self) -> None:
        self.sidebar_color = arcade.color.BLACK
        self.grid_color = arcade.color.LIGHT_GRAY
        self.snake_color = arcade.color.GREEN
        self.food_color = arcade.color.RED
        self.text_color = arcade.color.WHITE
        
        self.snake: List[Tuple[int, int]] = [
            (self.grid_width // 2, self.grid_height // 2),
            (self.grid_width // 2 - 1, self.grid_height // 2),
            (self.grid_width // 2 - 2, self.grid_height // 2)
        ]
        
        self.food: Tuple[int, int] = (self.grid_width - 1, self.grid_height - 1)

        self.score = 0
        self.level = 1
        self.snake_length = len(self.snake)
    
    def on_draw(self) -> None:
        self.clear()
        
        arcade.draw_lrbt_rectangle_filled(
            left=self.screen_width - self.sidebar_width,
            right=self.screen_width,
            bottom=0,
            top=self.screen_height,
            color=self.sidebar_color
        )
        
        for x in range(0, self.screen_width - self.sidebar_width, self.grid_size):
            arcade.draw_line(x, 0, x, self.screen_height, self.grid_color, 1)
        for y in range(0, self.screen_height, self.grid_size):
            arcade.draw_line(0, y, self.screen_width - self.sidebar_width, y, self.grid_color, 1)
        
        game_field_rect = arcade.LRBT(
            left=0,
            right=self.screen_width - self.sidebar_width,
            bottom=0,
            top=self.screen_height
        )
        arcade.draw_rect_outline(
            rect=game_field_rect,
            color=arcade.color.BLACK,
            border_width=2
        )
        
        for segment in self.snake:
            left = segment[0] * self.grid_size
            bottom = segment[1] * self.grid_size
            segment_rect = arcade.LRBT(
                left=left,
                right=left + self.grid_size - 2,
                bottom=bottom,
                top=bottom + self.grid_size - 2
            )
            arcade.draw_rect_filled(
                rect=segment_rect,
                color=self.snake_color
            )
        
        food_x = self.food[0] * self.grid_size + self.grid_size // 2
        food_y = self.food[1] * self.grid_size + self.grid_size // 2
        arcade.draw_circle_filled(
            center_x=food_x,
            center_y=food_y,
            radius=self.grid_size // 2 - 2,
            color=self.food_color
        )
        
        start_y = self.screen_height - 50
        
        arcade.draw_text(
            "СТАТИСТИКА", 
            self.screen_width - self.sidebar_width + 20, 
            start_y, 
            self.text_color, 
            font_size=16, 
            bold=True
        )
        
        arcade.draw_text(
            f"Счет: {self.score}", 
            self.screen_width - self.sidebar_width + 20, 
            start_y - 50, 
            self.text_color, 
            font_size=14
        )
        
        arcade.draw_text(
            f"Уровень: {self.level}", 
            self.screen_width - self.sidebar_width + 20, 
            start_y - 90, 
            self.text_color, 
            font_size=14
        )
        
        arcade.draw_text(
            f"Длина: {self.snake_length}", 
            self.screen_width - self.sidebar_width + 20, 
            start_y - 130, 
            self.text_color, 
            font_size=14
        )
        
        arcade.draw_text(
            "Управление:", 
            self.screen_width - self.sidebar_width + 20, 
            start_y - 200, 
            self.text_color, 
            font_size=14, 
            bold=True
        )
        
    
    


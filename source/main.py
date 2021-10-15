from PyGE.Engine import side_scroller
from source.Objects.Bullet import Bullet
from source.Objects.Enemy import Enemy, EnemyHandler
from source.Objects.Player import Player

def run():
    from source.Objects.Button import Button
    side_scroller(
        xml=open("resources/xml/rooms.xml").read(),
        start_room="menu",
        images={
            "player1": {"path": "resources/images/player/player.png", "w": 32, "h": 32},
            "player2": {"path": "resources/images/player/player2.png", "w": 32, "h": 32},
            "enemy": {"path": "resources/images/enemy/enemy.png", "w": 32, "h": 32}
        },
        sprite_sheets={

        },
        sounds={
        },
        font={
          "Querround16": {"path": "resources/font/querround/QUERROUND.TTF", "size": 16}
        },
        custom_objects=[
            Player, Bullet, Enemy, EnemyHandler, Button
        ],
        initial_variables={
        },
        development_screen_size=(800, 500),
        fullscreen=False,
        auto_scale=False,
        background_color=(10, 10, 10),
        debug=True
    )
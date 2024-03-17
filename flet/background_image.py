import flet as ft
from random import randint


def main(page: ft.Page):

    # létrehozol egy tartalmat
    tartalom = ft.Column()

    # Az oldalnak beállítasz egy kontainert, aminek az elsőnek kell lennie
    # A containernek beállítasz egy háttérképet
    # beállítot a kitöltést
    # expandit True-ra állítod
    # a container tartalmának beállítod, amit az oldalra akarsz tenni
    page.add(ft.Container(
            image_src=f"https://picsum.photos/200/200?{randint(0,100)}",
            image_fit=ft.ImageFit.COVER,
            expand=True,
            content=tartalom
        )
    )

    # A tartalomhoz adod hozzá az új tartalmakat - egyesével
    tartalom.controls.append(ft.Text('Border radius'))
    tartalom.controls.append(ft.Image(
            src='assets/images/mandelbrot_set.jpg',
            border_radius=ft.border_radius.only(top_left=75, bottom_right=100),
            height=200,
            width=200,
        ))
    tartalom.controls.append(ft.Divider())
    tartalom.controls.append(ft.Text('Második kép'))
    tartalom.controls.append(ft.Image(
            src=f"https://picsum.photos/200/200?{randint(0,100)}",
            height=200,
            width=200,
        ))

    page.update()


ft.app(target=main)

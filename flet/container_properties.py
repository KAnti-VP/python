import flet as ft


def main(page: ft.Page):
    page.title = "Containers - clickable and not"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Row(
            [
                ft.Container(
                    content=ft.Text("Non clickable"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.AMBER,
                    width=150,
                    height=150,
                    border_radius=10,
                ),
                ft.Container(
                    content=ft.Text("Clickable without Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    on_click=lambda e: print("Clickable without Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable with Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.CYAN_200,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: print("Clickable with Ink clicked!"),
                ),
                ft.Container(
                    content=ft.Text("Clickable transparent with Ink"),
                    margin=10,
                    padding=10,
                    alignment=ft.alignment.center,
                    width=150,
                    height=150,
                    border_radius=10,
                    ink=True,
                    on_click=lambda e: page.launch_url(url='https://flet.dev/docs/controls/container#content')
                ),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    page.add(ft.Divider(height=1, color="blue", thickness=3))

    c = ft.Container(
        content=ft.Text('Tartalom'),
        alignment=ft.alignment.center,
        width=100,
        height=100,
        bgcolor="teal",
        animate=ft.animation.Animation(1000, "bounceOut"),
        border=ft.border.only(left=ft.border.BorderSide(10, 'yellow'), right=ft.border.BorderSide(10, 'teal')),
        border_radius=ft.border_radius.only(bottom_left=50),
        shape=ft.BoxShape.CIRCLE,
    )

    def animate_container(e):
        c.width = 100 if c.width == 200 else 200
        c.height = 100 if c.height == 200 else 200
        c.bgcolor = "blue" if c.bgcolor == "red" else "red"
        c.update()
    
    col = ft.Column(
        width=page.width,
        height=300,
        horizontal_alignment='center',
        controls=[
        c,
        ft.ElevatedButton("Animate container", on_click=animate_container)
    ])

    page.add(col)

    page.add(ft.Divider(height=1, color="blue", thickness=3))

    t = ft.Text()

    def container_click(e: ft.ContainerTapEvent):
        if not t.value:
            page.controls.pop()
        t.value = f"local_x: {e.local_x}\nlocal_y: {e.local_y}\nglobal_x: {e.global_x}\nglobal_y: {e.global_y}"
        t.update()
        print(f"local_x: {e.local_x}\nlocal_y: {e.local_y}\nglobal_x: {e.global_x}\nglobal_y: {e.global_y}")
        # page.update()

    page.add(
        ft.Column(
            [
                ft.Container(
                    content=ft.Text("Clickable inside container"),
                    alignment=ft.alignment.center,
                    bgcolor=ft.colors.GREEN_200,
                    width=200,
                    height=200,
                    border_radius=10,
                    on_click=container_click,
                ),
                t,
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        ),
    )

    # page.update()


if __name__ == '__main__':
    ft.app(target=main)

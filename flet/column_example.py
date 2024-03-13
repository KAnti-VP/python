import flet as ft


def main(page: ft.Page):
    page.title = "Column példa"
    page.bgcolor = ft.colors.TEAL_100

    column1 = ft.Column(
        controls=[
            ft.Container(height=100, width=100, bgcolor='red'),
            ft.Container(height=100, width=100, bgcolor='yellow'),
            ft.Container(height=100, width=100, bgcolor='green'),
            # ft.Container(height=100, width=100, bgcolor='red'),
            # ft.Container(height=100, width=100, bgcolor='yellow'),
            # ft.Container(height=100, width=100, bgcolor='green'),
            # ft.Container(height=100, width=100, bgcolor='red'),
            # ft.Container(height=100, width=100, bgcolor='yellow'),
            # ft.Container(height=100, width=100, bgcolor='green'),
            # ft.Container(height=100, width=100, bgcolor='red'),
            # ft.Container(height=100, width=100, bgcolor='yellow'),
            # ft.Container(height=100, width=100, bgcolor='green'),
        ],
        # alignment=ft.MainAxisAlignment.START, # Default beállítás
        alignment=ft.MainAxisAlignment.END,
        # alignment=ft.MainAxisAlignment.CENTER,
        # alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        # alignment=ft.MainAxisAlignment.SPACE_AROUND,
        # alignment=ft.MainAxisAlignment.SPACE_EVENLY,

        # horizontal_alignment=ft.CrossAxisAlignment.START, # Default beállítás
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        # horizontal_alignment=ft.CrossAxisAlignment.END,
        # horizontal_alignment=ft.CrossAxisAlignment.STRETCH,

        # run_spacing=50,
        # spacing=20,
        # scroll=ft.ScrollMode.ALWAYS,
        # wrap=True,

    )
    container1 = ft.Container(column1, bgcolor='blue', height=600, width=400, expand=True)
    page.add(container1)


if __name__ == '__main__':
    ft.app(target=main)

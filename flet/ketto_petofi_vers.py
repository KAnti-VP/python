import flet as ft


def main(page: ft.Page):

    def open_page(e):
        page.launch_url(url='https://szerelmes-versek.info/rozsabokor-domboldalon-petofi-sandor.vers')

    page.title = "Petőfi vers"
    page.bgcolor = "#5C0204"
    page.scroll = ft.ScrollMode.AUTO
    page.padding = ft.padding.symmetric(vertical=30)

    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(
        ft.Container(
            width=600,
            height=400,
            bgcolor="#F4E7BD",
            alignment=ft.alignment.top_center,
            padding=ft.padding.symmetric(horizontal=30),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                # alignment=ft.MainAxisAlignment.START,
                controls=[
                    ft.Text("Akarlak", italic=True, color="#749FA6", size=40),
                    ft.Row(
                        controls=[
                            ft.Icon(name=ft.icons.CALENDAR_MONTH, color="#9C393A", size=30),
                            ft.Text("2010-09-20", color="#8A8B92", italic=True, size=20)
                        ],
                        alignment=ft.MainAxisAlignment.CENTER,
                    ),
                    ft.Text("Akarom a két gyönyörű szemedet,"),
                    ft.Row(
                        controls=[ft.Text("vers folytatása >>>", weight=ft.FontWeight.BOLD)],
                        alignment=ft.MainAxisAlignment.END,
                    )
                ]
            )
        ),
        ft.Container(
            width=600,
            height=400,
            bgcolor="#F4E7BD",
        )
    )

    # page.update()


if __name__ == "__main__":
    ft.app(target=main)

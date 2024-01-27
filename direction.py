import flet as ft


def main(page: ft.Page) -> None:

    def open_page(e):
        print('Clicked. ', e)
        page.launch_url('https://flet.dev/docs/guides/python/colors')

    def print_entered(e):
        print('Entered. ', e)

    def print_exited(e):
        print('Exited. ', e)

    page.fonts = {
        'Anton': '/fonts/Anton-Regular.ttf'
    }

    text: ft.Text = ft.Text(value='Szöveg igazítás gyakorlása', color=ft.colors.GREY_50)
    page.controls.append(text)

    page.title = 'Szövegigazítás gyakorlás'
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = ft.padding.only(left=120, top=30)

    szoveg = ft.Text(
        value='A szöveg, ami megjelenik, ',
        bgcolor=ft.colors.INDIGO_400,
        color=ft.colors.AMBER_300,
        italic=True,
        font_family='Anton',
        selectable=True,
        size=40,
        text_align=ft.TextAlign.CENTER,
        theme_style=ft.TextThemeStyle.DISPLAY_LARGE,
        weight=ft.FontWeight.W_600,
        spans=[
            ft.TextSpan(
                text='a kiemelt rész először, ',
                style=ft.TextStyle(
                    bgcolor=ft.colors.GREY_100,
                    color=ft.colors.INDIGO_400,
                    decoration=ft.TextDecoration.UNDERLINE,
                    decoration_style=ft.TextDecorationStyle.WAVY,
                    decoration_thickness=2,
                    decoration_color=ft.colors.AMBER_300,
                    font_family='Arial',
                    size=30,
                    weight=ft.FontWeight.W_200,
                ),
            ),
            ft.TextSpan(
                text='majd másodszor.',
                style=ft.TextStyle(
                    bgcolor=ft.colors.TEAL,
                    # color=ft.colors.AMBER_300, # a szülő tulajdonságai veszi át
                    # italic=True,
                ),
                on_click=open_page,
                on_enter=print_entered,
                on_exit=print_exited,
            ),
        ]
    )

    page.add(szoveg)
    page.update()


if __name__ == '__main__':
    ft.app(target=main)

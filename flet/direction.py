import flet as ft


def main(page: ft.Page):

    def page_resize(e):
        print("Az oldal új mérete: ", page.window_width, page.window_height, e)
        resize: ft.Text = ft.Text(f'Oldalméret : {round(page.window_width, 1)}, {round(page.window_height, 1)}')
        page.add(resize)

    def open_page(e):
        print('Rákattintva. ', e)
        page.launch_url(url='https://flet.dev/docs/guides/python/colors')

    def print_entered(e):
        print('Rávíve az egérmutató. ', e)

    def print_exited(e):
        print('Levéve az egérmutató. ', e)

    page.fonts = {
        'Anton': '/fonts/Anton-Regular.ttf'
    }

    page.title = 'Szövegigazítás gyakorlás'
    page.theme_mode = ft.ThemeMode.DARK
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.padding = ft.padding.only(left=120, top=30)
    page.window_width = 700
    page.window_height = 500
    page.on_resize = page_resize

    text = ft.Text(value='Szöveg igazítás gyakorlása', color=ft.colors.GREY_50)
    page.controls.append(text)

    szoveg = ft.Text(
        value='A szöveg, ami megjelenik, ',
        bgcolor=ft.colors.INDIGO_400,
        color=ft.colors.AMBER_300,
        italic=True,
        font_family='Anton',
        selectable=True,
        size=30,
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
                    size=20,
                    weight=ft.FontWeight.W_200,
                ),
            ),
            ft.TextSpan(
                text='\nmajd másodszor mint link.',
                style=ft.TextStyle(
                    bgcolor=ft.colors.TEAL,
                    # color=ft.colors.AMBER_300, # a szülő tulajdonságai veszi át
                    # italic=True,
                ),
                url='https://flet.dev/docs/guides/python/colors',
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

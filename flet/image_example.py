import flet as ft
from random import randint


def main(page: ft.Page):
    page.title = "Images Example"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 50
    page.scroll = ft.ScrollMode.AUTO

    page.add(ft.Text('Kép háttérszínnel egy konténerben.'))
    img = ft.Container(
        content=ft.Image(
            # src=f"./assets/icons/logo.svg",
            src='icons/logo.svg',
            width=100,
            height=100,
            fit=ft.ImageFit.CONTAIN,
        ),
        bgcolor='yellow'
    )
    page.add(img, ft.Divider())

    page.add(ft.Text('Border radius'))
    page.add(ft.Image(
        src='assets/images/mandelbrot_set.jpg',
        # border_radius=100,
        border_radius=ft.border_radius.only(top_left=75, bottom_right=100),
        height=200,
        width=200,
        ),
        ft.Divider(),
    )

    page.add(ft.Text('Color használata alap beállítással'))
    page.add(ft.Image(
        src='assets/images/colored_hexagon.jpg',
        height=200,
        width=200,
        color='green',
        ),
        ft.Divider(),
    )

    page.add(ft.Text('Color használata color_blend_mode beállítással'))
    images_blend = ft.Row(wrap=False, scroll=ft.ScrollMode.ALWAYS)
    page.add(images_blend, ft.Divider(),)

    for i, blend_mode in enumerate(ft.BlendMode):
        images_blend.controls.append(ft.Image(
            src='assets/images/colored_hexagon.jpg',
            height=200,
            width=200,
            color='green',
            color_blend_mode=blend_mode
        ))
        print(f'{i}. Blemd mode: {blend_mode}')
    page.update()

    page.add(ft.Text('Error, a kép nem jeleníthető meg'))
    page.add(ft.Image(
        src='assets/images/mandelbrot__set.jpg',
        border_radius=100,
        height=200,
        width=200,
        error_content=ft.Container(ft.Text('A kép helye ...'),
                                   height=200,
                                   width=200,
                                   bgcolor='yellow',
                                   alignment=ft.alignment.center)
        ),
        ft.Divider(),
    )

    page.add(ft.Text('Fit használata kép beillesztéséhez'))
    images_fit = ft.Row(wrap=False, scroll=ft.ScrollMode.ALWAYS)
    page.add(images_fit, ft.Divider(),)

    for i, fit_mode in enumerate(ft.ImageFit):
        images_fit.controls.append(ft.Image(
            src='assets/images/mandelbrot_set.jpg',
            height=200,
            width=200,
            fit=fit_mode
        ))
        print(f'{i}. Image fit mode: {fit_mode}')
    page.update()

    page.add(ft.Text('Képmegjelenítés külső forrásból'))
    page.add(ft.Image(
        src=f"https://picsum.photos/200/200?{randint(0,100)}",
        height=200,
        width=200,
        ),
        ft.Divider()
    )

    page.add(ft.Text('src_base64 használata. Szöveeggé konvertált Kép beilletsztése.'))
    page.add(ft.Image(
        src_base64="iVBORw0KGgoAAAANSUhEUgAAABkAAAAgCAYAAADnnNMGAAAACXBIWXMAAAORAAADkQFnq8zdAAAAGXRFWHRTb2Z0d2FyZQB3d3cuaW5rc2NhcGUub3Jnm+48GgAAA6dJREFUSImllltoHFUYx3/fzOzm0lt23ZrQ1AQbtBehNpvQohgkBYVo410RwQctNE3Sh0IfiiBoIAjqi6TYrKnFy4O3oiiRavDJFi3mXomIBmOxNZe63ay52GR3Zj4f2sTEzmx3m//TYf7/c35zvgPnO6KqrESXqpq3muocAikv6m+/zytj3ejik1VN21G31YA9CgJ6xC+bMyQZPVCuarciPAMYC99V6Vw5pLbFSibHmlVoRVj9P3cmPBM8tSJI/M6mzabpfoAQ9fIF7WK4bd5vvuFnLGgy2vi0abg94A0AcJGvMq3hDxGRyar9r4F+iLAm0yIiRk8m37tctS1WsrIhhrI30+Srmg+J87OXUf3lWGS1q89dC6ltsSanxk4Aj2QBABii96300g87P/rtlrWr8l+vyDMfdlXSyyEikqxsiOUAQJCBhfHdXRfCq1LSsSlcWG+KBAGStvvrMkgiuv8lUc2mREukPwLUfHG+uTQv8Eown7VL3XlbBxYhf1c17hbVF3MDwA9bts280TnaU1YYqPby07aeFlUlHt27wSQ4CLo+F8AvoTCvHmyKF+ZbEb/M77P2LgvAwmrTHAHflN3KZxVbMC2jMFNOpgPnrMSOhvvFkMezXdwV4ePbtvHtxnJAMQ0j4JtVnO+eLb5oiSlt5HDbv7t1O90lpYCCCKbhfzW5kAIwUAazR0BlfII8Ow0I6uoVmI9MyAMwbMs8CExmDbk4zgu931MyO4OI4KrYflkRjOoTI+uM9d1vjotwKPu9QMk/sxzuO8POiVFcdZ1M2YBVsMEAKOqLvaPIe7mACuw0z/80SMH58SMplxlfiDhVi7dw2pltRhjKBQTQdrSja2KKTfE551NHuaZ0QVPvWYQUn31/Vm2nDvgjF4grVJx6suSvrvrSJ/6cSW2Oz9mf264uNrB806xZ1k/CZ49dUKgDEtlCROX2hfHpx8pGuuo3PpqYulw8fjndOp1yhgtNKRevJ1FyR2Ola+jXAjdnwTkZ6o896GdWdxDw7IxFg+0DpmXchTKSBWQnIuJn9u4j7dt+13UfHXEkXQOcuQ4kMhVtqsgUyPiQiPQfHw1NB2sRjmXKuTg1NwwBYLhtPtQX26eqTwGXPDOqvmcC4Hnwfrrad94GrVsOYTqUTkQY+iTlNe/6O1miSP/x0VB/+wMIDwHn/vtV1iQC4Xv95uUEWVCoL9Y5Z+gdovoyMHUFJHv88jmVy0vTuw7cZNv2YaA61Bfb7ZX5F8SaUv2xwZevAAAAAElFTkSuQmCC"
        ),
        ft.Divider()
    )

    page.add(ft.Text('Képen kívüli terület kitöltése'))
    images_repeat = ft.Row(wrap=False, scroll=ft.ScrollMode.ALWAYS)
    page.add(images_repeat, ft.Divider(), )

    for i, repeat_mode in enumerate(ft.ImageRepeat):
        images_repeat.controls.append(ft.Image(
            src='assets/images/colored_hexagon.jpg',
            height=400,
            width=400,
            repeat=repeat_mode
        ))
        print(f'{i}. Repeat mode: {repeat_mode}')
    page.update()

    page.add(ft.Text('Tooltip - egérmutató a kép fölött'))
    page.add(ft.Image(
        src='./assets/images/mandelbrot_set.jpg',
        height=200,
        width=200,
        tooltip='Mandelbrot halmaz'
    ),
        ft.Divider(),
    )

    page.add(ft.Text('Görgethető képek:'))
    images = ft.Row(wrap=False, scroll=ft.ScrollMode.ALWAYS)
    page.add(images)

    for i in range(0, 30):
        images.controls.append(
            ft.Image(
                src=f"https://picsum.photos/200/200?{i}",
                width=200,
                height=200,
                fit=ft.ImageFit.NONE,
                repeat=ft.ImageRepeat.NO_REPEAT,
                border_radius=ft.border_radius.all(10),
            )
        )
    page.update()


ft.app(target=main)
# ft.app(target=main, assets_dir="assets")

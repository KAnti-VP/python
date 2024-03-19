import flet as ft


def main(page: ft.Page):
    page.title = 'Szövegmezők'
    page.scroll = ft.ScrollMode.AUTO

    def button_clicked(e):
        t1.value = f"A szövegmezől tartalma:\n'{tb1.value}',\n '{tb2.value}',\n '{tb3.value}',\n '{tb4.value}',\n '{tb5.value}',\n '{tb6.value}',\n '{tb7.value}',\n '{tb8.value}'."
        page.update()

    t1 = ft.Text()
    cont1 = ft.Container(t1, height=250, width=600, bgcolor=ft.colors.AMBER_50, padding=20)
    tb1 = ft.TextField(label="Standard")
    tb2 = ft.TextField(label="Disabled", disabled=True, value="First name")
    tb3 = ft.TextField(label="Read-only", read_only=True, value="Last name")
    tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
    tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)
    tb6 = ft.TextField(label="Multiline textbox", multiline=True, width=300, min_lines=3, max_lines=2)
    tb7 =  ft.TextField(label="Password with reveal button", password=True, can_reveal_password=True, width=300)
    tb8 =  ft.TextField(label="Password without reveal button", password=True, width=300)
    b1 = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb1, tb2, tb3, tb4, tb5, tb6, tb7, tb8, b1, cont1)

    page.add(ft.Divider())

    def button_clicked(e):
        t2.value = f"Szövegmezők értékei:\n'{tb9.value}',\n '{tb10.value}',\n '{tb11.value}',\n '{tb12.value}'."
        page.update()

    def count_characters(e):
        tb12.counter_text = f'{len(tb12.value)} symbols typed'
        page.update()

    t2 = ft.Text()
    cont2 = ft.Container(t2, height=150, width=600, bgcolor=ft.colors.AMBER_50, padding=20)
    tb9 = ft.TextField(label="With prefix", prefix_text="https://")
    tb10 = ft.TextField(label="With suffix", suffix_text=".com")
    tb11 = ft.TextField(label="With prefix and suffix", prefix_text="https://", suffix_text=".com")
    tb12 = ft.TextField(
            label="My favorite color",
            icon=ft.icons.FORMAT_SIZE,
            hint_text="Type your favorite color",
            helper_text="You can type only one color",
            counter_text="0 symbols typed",
            on_change=count_characters,
            prefix_icon=ft.icons.COLOR_LENS,
            prefix_text="Color: ",
            suffix_text="...is your color",
            # error_text="Somehing went wrong",
        )
    b2 = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    page.add(tb9, tb10, tb11, tb12, b2, cont2)


ft.app(target=main)

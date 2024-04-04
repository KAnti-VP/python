import flet as ft


def main(page: ft.Page):
    page.title = 'Kikéredzkedők'

    def login(e):
        text.value = f'{user.value}\n{password.value}'
        page.update()
    
    def set_text_value():
        text.value = f'Start time: {start_hour.value}:{start_minute.value} End time: {end_hour.value}:{end_minute.value}'
    
    def change_time(e):
        print(e.__dict__)
        print(f"Time picker changed, value (minute) is {time_picker.value.minute}")
        start_hour.value = time_picker.value.hour
        start_minute.value = time_picker.value.minute
        end_hour_list.options.append(ft.dropdown.Option(start_hour.value))
        end_hour_list.value = start_hour.value
        end_hour_list.options.append(ft.dropdown.Option(str(int(start_hour.value) + 1)))

        for i in range(int(start_minute.value), int(start_minute.value) + 46):
            end_minute_list.options.append(ft.dropdown.Option(str(i % 60)))
        end_minute_list.value = start_minute.value
        set_text_value()
        page.update()

    def dismissed(e):
        print(f"Time picker dismissed, value is {time_picker.value}")
        text.value = f'{time_picker.value.hour} # {time_picker.value.minute}'
        page.update()
    
    def set_end_time_on_change(e):
        end_hour.value = end_hour_list.value
        end_minute.value = end_minute_list.value
        set_text_value()
        page.update()
    

    user = ft.TextField(label='e-main')
    password = ft.TextField(label='password')
    login_btn = ft.ElevatedButton(text='Küld', on_click=login)
    text = ft.Text()
    start_hour = ft.Text(width=20)
    start_minute = ft.Text(width=20)
    end_hour = ft.Text(width=20)
    end_minute = ft.Text(width=20)
    end_hour_list = ft.Dropdown(width=100, on_change=set_end_time_on_change)
    end_minute_list = ft.Dropdown(width=100, on_change=set_end_time_on_change)

    # page.add(user, password, login_btn, text)

    class_list = ft.Dropdown(width=100)
    classes = ['9/a', '9/b', '9/c', '9/NY', '10/a', '10/b', '10/c', '11/a', '11/b', '11/c', '12/a', '12/b', '12/c']
    for clas in classes:
        class_list.options.append(ft.dropdown.Option(clas))

    page.add(class_list)

    time_picker = ft.TimePicker(
        confirm_text="Confirm",
        error_invalid_text="Time out of range",
        help_text="Pick your time slot",
        on_change=change_time,
        on_dismiss=dismissed,
    )

    page.overlay.append(time_picker)

    start_date_button = ft.ElevatedButton(
        "Pick time",
        icon=ft.icons.ACCESS_TIME,
        on_click=lambda _: time_picker.pick_time(),
    )

    page.add(start_hour, start_minute, start_date_button, end_hour, end_minute, end_hour_list, end_minute_list, text)
    

ft.app(target=main)
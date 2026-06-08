import flet as ft
from login import login_view
from crud import crud_view

def main(page: ft.Page):
    page.title = "Sistema CRUD Alumnos"
    page.theme_mode = ft.ThemeMode.LIGHT

    def route_change(e):
        page.views.clear()
        if page.route == "/":
            page.views.append(ft.View("/", [login_view(page)]))
        elif page.route == "/crud":
            page.views.append(ft.View("/crud", [crud_view(page)]))
        page.update()

    page.on_route_change = route_change
    page.go("/")

ft.app(target=main)

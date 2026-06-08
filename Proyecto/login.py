import flet as ft
from database import get_connection
from utilidades import check_password

def login_view(page: ft.Page):
    usuario = ft.TextField(label="Usuario")
    contrasena = ft.TextField(label="Contraseña", password=True)
    mensaje = ft.Text("")

    def validar_login(e):
        conn = get_connection()
        if conn:
            cursor = conn.cursor()
            cursor.execute("SELECT password FROM usuarios WHERE usuario=%s", (usuario.value,))
            result = cursor.fetchone()
            if result and check_password(contrasena.value, result[0]):
                page.go("/crud")
            else:
                mensaje.value = "Credenciales incorrectas"
            conn.close()
        else:
            mensaje.value = "Error de conexión a BD"
        page.update()

    return ft.Column([
        ft.Text("Login del Sistema", size=20),
        usuario,
        contrasena,
        ft.ElevatedButton("Ingresar", on_click=validar_login),
        mensaje
    ], alignment=ft.MainAxisAlignment.CENTER)

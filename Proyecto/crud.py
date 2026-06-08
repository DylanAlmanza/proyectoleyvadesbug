import flet as ft
from database import get_connection
from utilidades import validar_curp, validar_telefono

def crud_view(page: ft.Page):
    matricula = ft.TextField(label="Matrícula")
    nombre = ft.TextField(label="Nombre(s)")
    ap_pat = ft.TextField(label="Apellido Paterno")
    ap_mat = ft.TextField(label="Apellido Materno")
    curp = ft.TextField(label="CURP")
    telefono = ft.TextField(label="Teléfono")
    especialidad = ft.TextField(label="Especialidad")
    ciudad = ft.TextField(label="Ciudad")
    estado = ft.Dropdown(options=[ft.dropdown.Option("Chihuahua"), ft.dropdown.Option("Sonora")])
    mensaje = ft.Text("")

    def insertar(e):
        if not validar_curp(curp.value):
            mensaje.value = "CURP inválida"
        elif not validar_telefono(telefono.value):
            mensaje.value = "Teléfono inválido"
        else:
            conn = get_connection()
            if conn:
                try:
                    cursor = conn.cursor()
                    cursor.execute("""
                        INSERT INTO alumnos (matricula, nombre, ap_pat, ap_mat, curp, telefono, especialidad, ciudad, estado)
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """, (matricula.value, nombre.value, ap_pat.value, ap_mat.value, curp.value.upper(),
                          telefono.value, especialidad.value, ciudad.value, estado.value))
                    conn.commit()
                    mensaje.value = "Alumno registrado correctamente"
                except Exception as ex:
                    mensaje.value = f"Error: {ex}"
                finally:
                    conn.close()
            else:
                mensaje.value = "Error de conexión"
        page.update()

    return ft.Column([
        ft.Text("Gestión de Alumnos", size=20),
        matricula, nombre, ap_pat, ap_mat, curp, telefono,
        especialidad, ciudad, estado,
        ft.ElevatedButton("Insertar", on_click=insertar),
        mensaje
    ])

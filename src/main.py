import flet as ft


def main(page: ft.Page):
    page.title = "Convert hex to oklch"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.window.max_height = 500
    page.window.max_width = 450
    page.window.min_height = 400
    page.window.min_width = 400
    page.window.resizable = False

    title = ft.Text(
        value="Converter HEX em OKLCH",
        size=20,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD,
    )

    def copy_oklch(e):
        page.set_clipboard(cod_oklch)
        page.open(ft.SnackBar(ft.Text("OKLCH Copiado!")))
        page.update()

    def RGB_RGBA(e):
        hex.value = ""
        hex.max_length = int(e.control.value)
        page.update()

    hex = ft.TextField(label="HEX", prefix_text="#",
                       capitalization=ft.TextCapitalization.CHARACTERS, max_length=6)

    rgb_rgba = ft.RadioGroup(content=ft.Row([
        ft.Radio(value="6", label="RGB"),
        ft.Radio(value="8", label="RGBA")]), on_change=RGB_RGBA, value="6")

    cod_oklch = f"oklch(59% 0.145 163.225)"
    # cod_ = f"oklch({l}% {c} {m})"

    oklch = ft.TextField(label="OKLCH", read_only=True,
                         value=cod_oklch, suffix_icon=ft.IconButton(ft.icons.CONTENT_COPY, on_click=copy_oklch))

    btn = ft.OutlinedButton("Converter Cor",
                            style=ft.ButtonStyle(
                                color=ft.colors.GREEN_500,
                                text_style=ft.TextStyle(
                                    size=18,
                                    weight=ft.FontWeight.BOLD
                                ),
                                shape=ft.RoundedRectangleBorder(radius=5)
                            ))

    page.add(
        ft.Row(controls=[title], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[hex], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[rgb_rgba], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[oklch], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[btn], alignment=ft.MainAxisAlignment.CENTER),
    )
    pass


ft.app(main)

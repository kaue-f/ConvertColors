import flet as ft
import convert as convert


def main(page: ft.Page):
    page.title = "Convert hex to oklch"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    page.window.height = 500
    page.window.width = 450
    page.window.min_height = 400
    page.window.min_width = 400
    page.window.center()
    page.bgcolor = ('#191615')

    title = ft.Text(
        value="Converter HEX em OKLCH",
        size=20,
        text_align=ft.TextAlign.CENTER,
        weight=ft.FontWeight.BOLD,
    )

    def copy_oklch(e):
        page.set_clipboard(oklch.value)
        page.open(ft.SnackBar(ft.Text("OKLCH Copiado!")))
        page.update()

    def convert_color(e):
        oklch.value = convert.hex_to_oklch(hex.value)
        page.update()

    hex = ft.TextField(label="HEX", prefix_text="#",
                       capitalization=ft.TextCapitalization.CHARACTERS, max_length=6)

    oklch = ft.TextField(label="OKLCH", read_only=True,
                         value="", suffix_icon=ft.IconButton(ft.icons.CONTENT_COPY, on_click=copy_oklch))

    btn = ft.OutlinedButton("Converter Cor",
                            style=ft.ButtonStyle(
                                color=('#7acc00'),
                                text_style=ft.TextStyle(
                                    size=18,
                                    weight=ft.FontWeight.BOLD
                                ),
                                shape=ft.RoundedRectangleBorder(radius=5),
                                side=ft.BorderSide(width=2, color='#7acc00')),
                            on_click=convert_color)

    page.add(
        ft.Row(controls=[title], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[hex], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[oklch], alignment=ft.MainAxisAlignment.CENTER),
        ft.Row(controls=[btn], alignment=ft.MainAxisAlignment.CENTER),
    )
    pass


ft.app(main)

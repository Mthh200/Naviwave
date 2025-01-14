import flet as ft

def main(page: ft.Page):
    page.appbar = ft.AppBar(
        leading = ft.Row([
            ft.IconButton(icon= ft.Icons.CHEVRON_LEFT),
            ft.TextButton(text = 'Equipes', style = ft.ButtonStyle(padding=0))
        ]),
        title = ft.Text('NaviWave'),
        center_title=True
    )
    page.add(
        ft.Card(
            content=ft.Container(
                content= ft.Column([
                    ft.Row([
                        ft.IconButton(icon=ft.Icons.PERSON_3),
                        ft.IconButton(icon=ft.Icons.PERSON_3),
                        ft.IconButton(icon=ft.Icons.PERSON_3),
                        ft.IconButton(icon=ft.Icons.PERSON_3)
                    ]),
                    ft.Row([
                        ft.IconButton(icon=ft.Icons.PERSON_3),
                        ft.IconButton(icon=ft.Icons.PERSON_3),
                        ft.IconButton(icon=ft.Icons.PERSON_3),
                        ft.IconButton(icon=ft.Icons.PERSON_3)
                    ])
                ]),
                
             width=320,
             height=186,
             border_radius=10,
             alignment=ft.alignment.center,
             bgcolor='green'
            )
        )
    )
    page.add(ft.Text(value='body'))



ft.app(main)
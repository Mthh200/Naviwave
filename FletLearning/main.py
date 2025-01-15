import flet as ft

def main(page: ft.Page):

    page.window.width=360
    page.window.height=800

    page.appbar = ft.AppBar(
        leading = ft.Row([
            ft.IconButton(icon= ft.Icons.CHEVRON_LEFT),
            ft.TextButton(text = 'Equipes', style = ft.ButtonStyle(padding=0))
        ]),
        title = ft.Text('NaviWave'),
        center_title=True
    )
    
    def view_pop(view):
        page.views.pop()
        top_view = page.views[-1]
        page.go(top_view.route)

    def mudanca_de_rota(route):
        page.go('/membro')
        page.views.clear()
        if page.route == '/membro':
            page.views.append(
                ft.View('/membro',
                    [
                        ft.Text('Tela de membro'),
                        ft.Text('Em obras')
                    ]
                )
            )


    page.add(
        ft.Card(
            content=ft.Container(
                content= ft.Column([
                    ft.Row([
                        ft.Text('Membros'),
                        ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT, on_click=mudanca_de_rota)
                    ], spacing=160),
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
             border_radius=10,
             alignment=ft.alignment.center,
             bgcolor='green',
             padding=10
            )
        ),
        ft.Container(content=ft.Column([
            ft.Text('Produtividade da equipe'),
            ft.Row([
                ft.Container(bgcolor='blue', border_radius=10, width=60, height=24),
                ft.Container(bgcolor='blue', border_radius=10, width=60, height=24),
                ft.Container(bgcolor='blue', border_radius=10, width=60, height=24),
                ft.Container(bgcolor='blue', border_radius=10, width=60, height=24),
                ft.Container(bgcolor='#E1E1E1', border_radius=10, width=60, height=24)
            ])
        ])),
        ft.Container(content=ft.Column([
            ft.Text('Harmonia da equipe'),
            ft.Row([
                ft.Container(bgcolor='blue', border_radius=10, width=60, height=24),
                ft.Container(bgcolor='blue', border_radius=10, width=60, height=24),
                ft.Container(bgcolor='blue', border_radius=10, width=60, height=24),
                ft.Container(bgcolor='#E1E1E1', border_radius=10, width=60, height=24),
                ft.Container(bgcolor='#E1E1E1', border_radius=10, width=60, height=24)
            ])
        ])),
        ft.Container(content=ft.Column([
            ft.Row([
                ft.Text('Pontos de Atenção'),
                ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT)
            ], spacing=160),
            ft.Row([
                ft.Card(content= ft.Container(content=ft.Column([
                    ft.IconButton(icon=ft.Icons.PERSON_3),
                    ft.Text('Amanda', color='white')
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER), 
                width=146,
                height=126,
                border_radius=15,
                bgcolor='green',
                alignment=ft.alignment.center
                )),
                ft.Card(content= ft.Container(content=ft.Column([
                    ft.IconButton(icon=ft.Icons.PERSON_3),
                    ft.Text('Gustavo', color='white')
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER), 
                width=146,
                height=126,
                border_radius=15,
                bgcolor='green',
                alignment=ft.alignment.center
                ))
                ])
                
            ]))
    
    )
    page.on_route_change = mudanca_de_rota
    page.on_view_pop = view_pop
    page.go(page.route)


ft.app(main)

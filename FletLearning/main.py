import flet as ft

def main(page: ft.Page):

    page.window.width=360
    page.window.height=800

    page.appbar = ft.AppBar(
        leading = ft.Row([
            ft.IconButton(icon= ft.Icons.CHEVRON_LEFT, padding=0),
        ]),
        title = ft.Text('NaviWave'),
        center_title=True
    )

    def go_to_equipe(view):
        page.clean()
        page.add(equipeView())
        page.update()

    def go_to_membro(route):
        page.clean()
        page.add(membrosView())

    def membrosView():
       
        return ft.Container(
            ft.Text('Membros View')
        )
        
    

    def equipeView():
        return ft.Container(ft.Column([
            ft.Card(
                content=ft.Container(
                    content= ft.Column([
                        ft.Row([
                            ft.Text('Membros', color='white'),
                            ft.IconButton(icon=ft.Icons.CHEVRON_RIGHT, on_click=go_to_membro)
                        ], spacing=210),
                        ft.Column([
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
                        ])
                    ]),
                width=330,
                border_radius=10,
                alignment=ft.alignment.center,
                bgcolor='green',
                padding=5
                )
            ),
            ft.Container(content=ft.Column([
                ft.Text('Produtividade da equipe'),
                ft.Row([
                    ft.Container(bgcolor='blue', border_radius=10, width=55, height=24),
                    ft.Container(bgcolor='blue', border_radius=10, width=55, height=24),
                    ft.Container(bgcolor='blue', border_radius=10, width=55, height=24),
                    ft.Container(bgcolor='blue', border_radius=10, width=55, height=24),
                    ft.Container(bgcolor='#E1E1E1', border_radius=10, width=55, height=24)
                ])
            ])),
            ft.Container(content=ft.Column([
                ft.Text('Harmonia da equipe'),
                ft.Row([
                    ft.Container(bgcolor='blue', border_radius=10, width=55, height=24),
                    ft.Container(bgcolor='blue', border_radius=10, width=55, height=24),
                    ft.Container(bgcolor='blue', border_radius=10, width=55, height=24),
                    ft.Container(bgcolor='#E1E1E1', border_radius=10, width=55, height=24),
                    ft.Container(bgcolor='#E1E1E1', border_radius=10, width=55, height=24)
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
                        ft.Text('Amanda', color='white'),
                        ft.Text('Publicitária', color='white')
                    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER), 
                    width=146,
                    height=126,
                    border_radius=15,
                    bgcolor='green',
                    alignment=ft.alignment.center
                    )),
                    ft.Card(content= ft.Container(content=ft.Column([
                        ft.IconButton(icon=ft.Icons.PERSON_3),
                        ft.Text('Gustavo', color='white'),
                        ft.Text('Desenvolvedor', color='white')
                    ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER), 
                    width=146,
                    height=126,
                    border_radius=15,
                    bgcolor='green',
                    alignment=ft.alignment.center
                    ))
                    ])
                    
                ]))
            ])
        
    )
    page.add(equipeView())


ft.app(main)

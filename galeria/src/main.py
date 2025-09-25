import flet as 

def main(page: ft.Page):
    page.title="Galeria"
    page.bgcolor=ft.Colors.BLACK45
    
    libros = [
        {
            "titulo": "Antes de diciembre"
            "autor": "Joana Marcús"
            "año": 2021 
            "descripcion": "famoso por ser un romance universitario"
            "imagen": "https://raw.githubusercontent.com/luz2929/PROYECTO_BIMESTRAL_PRIMER-PERIODO/refs/heads/main/antes%20de%20diciembre.jpg" 
        },
        {
            "titulo": "Despues de diciembre"
            "autor": "Joana Marcús"
            "año": 2021 
            "descripcion": "famoso por ser un romance universitario"
            "imagen": "https://raw.githubusercontent.com/luz2929/PROYECTO_BIMESTRAL_PRIMER-PERIODO/refs/heads/main/despues%20de%20diciembre.jpg" 
        },
        {
            "titulo": "Tres meses"
            "autor": "Joana Marcús"
            "año": 2021  
            "descripcion": "famoso por ser un romance universitario"
            "imagen": "https://raw.githubusercontent.com/luz2929/PROYECTO_BIMESTRAL_PRIMER-PERIODO/refs/heads/main/tres%20meses.jpg"
        },
        {
            "titulo": "Las luces de frebrero"
            "autor": "Joana Marcús"
            "año": 2021  
            "descripcion": "famoso por ser un romance universitario"
            "imagen": 
        },
        {
            "titulo": "Damian" 
            "autor": "Alex Mirez"
            "año": 2022  
            "descripcion": "famoso por ser un romance entre especies diferentes"
            "imagen": 
        },
    ]
    
    indice_actual=[0]
    
    contenedor=ft.Container(
        content=ft.Column([]),
        width=400,
        height=500,
        bgcolor=ft.Colors.BLUE_400,
        alignment=ft.alignment.center,
        padding=20
    )
    
    boton_siguiente=ft.ElevatedButton(text="Siguiente libro")
    

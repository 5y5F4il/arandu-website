import solara


@solara.component
def Home():
    with solara.Column(classes=["container"]):
        with solara.Column(classes=["hero"]):
            solara.Markdown("# Bienvenidos a Arandú")
            solara.Markdown("## Transformando políticas públicas con ciencia de datos e inteligencia artificial")
            solara.Markdown("Desarrollamos soluciones tecnológicas para mejorar la implementación, fiscalización y optimización de políticas públicas en Uruguay y América Latina.")
        
        with solara.Row(justify="center", gap="30px"):
            with solara.Column(style="max-width: 300px; text-align: center;"):
                solara.Markdown("### Implementación")
                solara.Markdown("Diseñamos y desarrollamos herramientas para una implementación más eficiente de políticas públicas.")
            
            with solara.Column(style="max-width: 300px; text-align: center;"):
                solara.Markdown("### Fiscalización")
                solara.Markdown("Creamos sistemas inteligentes para mejorar los procesos de control y fiscalización.")
            
            with solara.Column(style="max-width: 300px; text-align: center;"):
                solara.Markdown("### Optimización")
                solara.Markdown("Aplicamos algoritmos avanzados para optimizar recursos y maximizar el impacto social.")


@solara.component
def Blog():
    with solara.Card("Blog", style={"margin-top": "50px"}):
        solara.Markdown(
            """
            ## Blog de Arandú  
            *(Aquí aparecerán las publicaciones sobre las actividades de la startup)*  
            """
        )

@solara.component
def Proyetos():
    with solara.Card("Proyectos", style={"margin-top": "50px"}):
        solara.Markdown(
            """
            Legal chatbot: Un chatbot legal que utiliza inteligencia artificial para hacer más accesibles las normas 
            legales a organizaciones sociales y ambientales, y sugerirles abogados referentes de cada área.  
            """
        )
        solara.Markdown(
            """
            Fiscalización de plantaciones: Un sistema de inteligencia artificial que permite a los funcionarios del Ministerio de
            Ganadería, Agricultura y Pesca (MGAP) identificar plantaciones que no cumplen con las distancias correctas a cauces de agua,
            caminos y otras plantaciones.    
            """
        )
        solara.Markdown(
            """
            Monitoreo de la calidad del agua: Un sistema de inteligencia artificial que permite a los funcionarios del Ministerio de
            Ambiente (MA) identificar anomalías en la calidad del agua en tiempo real, utilizando datos de sensores y modelos predictivos.  
            """
        )
        solara.Markdown(
            """
            Automatización de resolución de conflictos en SIG: Un sistema de inteligencia artificial que permite a los funcionarios de la
            Intendencia de Montevideo resolver conflictos en capas de información geográfica (SIG) de manera automática, utilizando 
            algoritmos de aprendizaje automático.
            """
        )
    

@solara.component
def QSomos():
    with solara.Card("Quiénes somos", style={"margin-top": "50px"}):
        solara.Markdown(
            """
            Misión:
            Arandú transforma la gestión pública uruguaya mediante la aplicación de ciencia de datos e inteligencia artificial, diseñando soluciones 
            éticas, transparentes y de alto impacto social que optimizan la fiscalización e implementación de políticas públicas. Dedicamos una parte 
            sustancial de nuestros esfuerzos a la investigación científica, la creación de nuevo conocimiento y su comunicación efectiva. 
            Democratizamos el acceso al conocimiento y fortalecemos la capacidad del Estado para tomar decisiones basadas en evidencia, priorizando 
            áreas clave como educación, salud, vivienda, soberanía alimentaria y sostenibilidad ambiental.  
            """
        )
        solara.Markdown(
            """
            Visión:
            AEn 2030, Arandú será reconocida como la organización referente en la integración de ciencia de datos avanzada con políticas públicas 
            en Uruguay, habiendo transformado la forma en que el Estado implementa, evalúa y fiscaliza sus programas. Nuestro equipo multidisciplinario 
            habrá consolidado una robusta línea de investigación científica, publicando y comunicando activamente sus hallazgos para contribuir al 
            avance del conocimiento global. Habremos desarrollado metodologías innovadoras adaptadas a la realidad latinoamericana, generando un 
            cuerpo de conocimiento científico que se comparte abiertamente con la sociedad. Aspiramos a que nuestro modelo sea replicado en otros 
            países de la región, demostrando que la tecnología, cuando se aplica con conciencia social y ambiental, puede fortalecer el rol del 
            Estado como garante del bienestar colectivo."""
        )

routes = [
    solara.Route(path="/", component=Home, label="Home"),
    solara.Route(path="blog", component=Blog, label="Blog"),
    solara.Route(path="proyectos", component=Proyetos, label="Proyectos"),
    solara.Route(path="quienes-somos", component=QSomos, label="Quiénes somos")
]
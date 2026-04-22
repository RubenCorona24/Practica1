import streamlit as st

#--------CREACIÓN DE FORMULARIOS CON STREAMLIT--------

#Configuramos la ventana
st.set_page_config(page_title='Formulario Web',initial_sidebar_state='collapsed',layout='wide')
def inicio():
    st.header("Bienvenidos a nuestra app")
    st.write("""
    Dentro manejamos diferentes formularios para mejorar la experiencia al cliente
    - Podemos analizar el puesto y nombre de un trabajador
    - Podemos calcular salario de un trabajador en base a horas de trabajo y pago por hora
    - Analizar envíos de usuario""")

def main():
    st.title("Aplicación de formularios")
    secciones = ['Inicio','Formularios Básicos','Enfoques de formularios','Calculadora de salario','Reinicio de formularios']
    seccion = st.sidebar.selectbox('Sección',secciones)
    if seccion == 'Inicio':
        inicio()
    elif seccion == 'Formularios Básicos':
        st.header("Formularios Básicos para empleados")
        #Empezamos a crear formulario
        with st.form(key='formulario_basico'):
            st.write("Introduce los datos correctamente")
            nombre = st.text_input("Nombre: ")
            apellido = st.text_input("Apellido: ")
            edad = st.number_input("Edad: ")
            #Creamos el boton enviar
            boton_enviar = st.form_submit_button(label='Enviar')
            if boton_enviar:
                if (nombre != "") and (apellido!="") and (edad!=0):
                    st.success(f"Hola {nombre}, has creado una cuenta exitosamente!")
                else:
                    st.warning("Formato de datos no cumplida")
    elif seccion == 'Enfoques de formularios':
        st.header("Enfoque de formularios")
        st.subheader("1. Enfoque con Administrador de contexto")
        with st.form(key='Administrador de contexto'):
            st.write("Formulario 1: Usando administrador de contextos")
            nombre =st.text_input("Nombre: ")
            enviar1 = st.form_submit_button(label='Iniciar Sesión')
            if enviar1:
                if nombre != "":
                    st.success(f"Bienvenido {nombre}")
                else:
                    st.warning("Completar campo")
        with st.form(key='formulario2'):
            st.write("Formulario 2: con enfoque declarado")
            puesto = st.selectbox("Puesto de trabajo",['Ingeniero','Científico de Datos','Desarrollador','Ciberseguridad']) #selectbox
            enviar2 = st.form_submit_button(label="Enviar datos")
            if enviar2:
                st.success(f"Datos enviados correctamente - Puesto: {puesto}")
    elif seccion == 'Calculadora de salario':
        st.header("Calculadora de Salario")
        #Empezamos otro formulario
        with st.form(key="calculadora"):
            col1,col2,col3 = st.columns(3)
            with col1:
                tarifa_hora = st.number_input("Tarifa por hora ($)",min_value=0.0) #Input de número
            with col2:
                horas_dia = st.number_input("Horas de trabajo por día",min_value=0,max_value=168)
            with col3:
                calcular = st.form_submit_button("Calcular salario")
        if calcular:
            #Calculamos los datos
            diario = tarifa_hora * horas_dia #sueldo diario
            semanal = diario * 7
            mensual = semanal * 4
            anual = semanal * 52
            st.subheader("Desglose salario") #Añadimos subtítulo
            col1,col2 = st.columns(2) #Creamos nuevas olumnas
            with col1:
                st.write(f"- Salario diario: {diario} MXM")
                st.write(f"- Salario semanal: {semanal} MXM")
            with col2:
                st.write(f"- Salario mensual: {mensual} MXM")
                st.write(f"- Salario anual: {anual} MXM")
    elif seccion == 'Reinicio de formularios':
        st.header("Formulario pero con reinicio de datos")
        with st.form(key='formulario_reinicio',clear_on_submit=True): #Me reinicia todo el campo
            nombre = st.text_input("Nombre: ")
            info = st.text_input("Localidad: ")
            envio = st.form_submit_button(label='Enviar datos')
            if envio:
                if (nombre != "") and (info != ""):
                    st.success(f"Bienvenido {nombre}, vives en {info}")
                    st.info("El formulario se reinicia automáticamente")
                else:
                    st.warning("Información obligatoria")


if __name__ == '__main__':
    main()
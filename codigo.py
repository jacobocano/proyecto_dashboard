# Manager: Jacobo cano
# Project: Dashboard (Web Applicattion) for "Socialize your knowledge" organization, created with Streamlit Plattform
# Creaton Date: 04.01.2026

import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(
    page_title="Dashboard",
    layout="wide", # This sets the app to wide mode
    initial_sidebar_state="expanded" # Optional: control sidebar state
)

# Dataset of Employee's Data
employees_data = pd.read_csv('Employee_data.csv')

# ------------------------------------------------------------------------------------------------------------------------------------
# 1.    Código que contenga las instrucciones para el despliegue de un título y una breve descripción de la aplicación web.
# ------------------------------------------------------------------------------------------------------------------------------------
st.title('Performance analysis of the collaborators of Socialize your knowledge')
st.subheader('Dashboard to identify your strengths and areas for improvement, enabling you to enhance your performance and achieve higher quality services.')

# ------------------------------------------------------------------------------------------------------------------------------------
# 2.    Código que permita desplegar el logotipo de la empresa en la aplicación web.
# ------------------------------------------------------------------------------------------------------------------------------------
image = Image.open('Logo.png')
st.image(image, width="content")

# Titulo en la barra lateral

# st.sidebar.image(image, width="content")
st.sidebar.title("Dashboard 📄")
st.sidebar.caption(" Filters: ")

# ------------------------------------------------------------------------------------------------------------------------------------
# 3.    Código que permita desplegar un control para seleccionar el género del empleado.
# ------------------------------------------------------------------------------------------------------------------------------------
selected_gender = st.sidebar.radio("Select gender", employees_data['gender'].unique(), horizontal=True, label_visibility="visible")
# st.write(f"Select gender: {selected_gender!r}")

# ------------------------------------------------------------------------------------------------------------------------------------
# 4.    Código que permita desplegar un control para seleccionar un rango del puntaje de desempeño del empleado.
# ------------------------------------------------------------------------------------------------------------------------------------

slider_performance_score = st.sidebar.slider("Select performance score range", employees_data['performance_score'].min(), employees_data['performance_score'].max(), (employees_data['performance_score'].min(), employees_data['performance_score'].max()))
# st.write(f"Select performance score range: {slider_performance_score!r}")

# ------------------------------------------------------------------------------------------------------------------------------------
# 5.    Código que permita desplegar un control para seleccionar el estado civil del empleado.
# ------------------------------------------------------------------------------------------------------------------------------------
select_marital_status = st.sidebar.selectbox("Select Marital Status", employees_data['marital_status'].unique())
# st.write(f"Selected Marital Status: {select_marital_status}")


# ------------------------------------------------------------------------------------------------------------------------------------
# ***
# 6.    Código que permita mostrar un gráfico en donde se visualice la distribución de los puntajes de desempeño.
# ------------------------------------------------------------------------------------------------------------------------------------

# El gráfico de dispersión (Scatter plot), es el tipo de gráfico seleccionado para mostrar la distribución de puntuajes de desepeño (performance_score)
# Instrucciones: 
# 1. Seleccionar datos númericos en un dataframe (dos columnas o series) : puntuajes de desempeño (performance_score) y id_employee

# DataFrame: slider_performance_score
st.markdown("""
<hr style="height:2px;border:none;color:#333;background-color:#333;" />
""", unsafe_allow_html=True)

st.write(' Performance Score Distribution ')

chart = (
    alt.Chart(employees_data)
    .mark_bar()
    .encode(
        x=alt.X('performance_score:O', title='Performance Score'),
        y=alt.Y('count()', title='Frecuency'),
        tooltip=['count()']
    )
)

st.altair_chart(chart, use_container_width=True)

# st.bar_chart(employees_data
#                 ,x = 'age'
#                 ,x_label = 'Age'
#                 ,y = 'performance_score'
#                 ,y_label='Performance Score'
#                 ,color="#0004ff"
#                 ,sort='age'
#                 ,stack=True
#                 ,width='stretch'
#                 ,height='content'
#                 )

# Columns
col1, col2 = st.columns(2)

with col1:
    # ------------------------------------------------------------------------------------------------------------------------------------
    # 7.    Código que permita mostrar un gráfico en donde se visualice el promedio de horas trabajadas por el género del empleado.
    # ------------------------------------------------------------------------------------------------------------------------------------
    st.markdown("""
    <hr style="height:2px;border:none;color:#333;background-color:#333;" />
    """, unsafe_allow_html=True)

    st.write(' Average Work Hours vs. Gender ')

    st.bar_chart(employees_data
                    ,x = 'gender'
                    ,x_label='Gender'
                    ,y = 'average_work_hours'
                    ,y_label = 'Average Work Hours'
                    ,color="#00ff88"
                    ,sort='average_work_hours'
                    ,horizontal=False
                    )

with col2:
    # ------------------------------------------------------------------------------------------------------------------------------------
    # 8.    Código que permita mostrar un gráfico en donde se visualice la edad de los empleados con respecto al salario de los mismo.
    # ------------------------------------------------------------------------------------------------------------------------------------
    st.markdown("""
    <hr style="height:2px;border:none;color:#333;background-color:#333;" />
    """, unsafe_allow_html=True)

    st.write(' Age vs. Salary ')

    st.area_chart(employees_data
                    ,x = 'age'
                    ,x_label = 'Age'
                    ,y = 'salary'
                    ,y_label='Salary'
                    ,color="#faa14e"
                    # ,size=85
                    # ,width="stretch"
                    # ,height="content"
                    )

# ------------------------------------------------------------------------------------------------------------------------------------
# 9.    Código que permita mostrar un gráfico en donde se visualice la relación del promedio de horas trabajadas versus el puntaje de desempeño.
# ------------------------------------------------------------------------------------------------------------------------------------
st.markdown("""
<hr style="height:2px;border:none;color:#333;background-color:#333;" />
""", unsafe_allow_html=True)
st.write(' Average Work Hours vs. Performance Score')

st.area_chart(employees_data
                 ,x = 'performance_score'
                 ,x_label='Performance Score'
                 ,y = 'average_work_hours'
                 ,y_label = 'Average Work Hours'
                 ,color="#73fc495c"
                 )

# ------------------------------------------------------------------------------------------------------------------------------------
# 10.   Código que permita desplegar una conclusión sobre el análisis mostrado en la aplicación web.
# ------------------------------------------------------------------------------------------------------------------------------------
st.markdown("""
<hr style="height:2px;border:none;color:#333;background-color:#333;" />
""", unsafe_allow_html=True)
st.write(' **Conclusions** ')

st.text("1. De acuerdo al primer gráfico ""Performance Score Distribution"", se puede identificar que la mayoría de los empleados tienen una calificación por desempeño igual a 3, equivalente al 78%, por lo que es un buen desempeño de manera general, sin embargo, es recomendable detectar los motivos de las personas con calificación igual a 4, y conocer los motivos por los que existen calificaciones igual a 1 o 2.")

st.text("2. De acuerdo al gráfico ""Average Work Hours vs. Gender"", las mujeres siendo mayoría en los empleados (56% de la población total) también en promedio trabajan más tiempo que los hombres, uno de los motivos es debido que la mayoría de las mujeres tiene 29 años y tienen una posición de técnico de producción (Production Technician), sin embargo, es recomendable conocer más acerca de la población femenina para conocer los motivos que propician que tengan más horas de trabajo.")

st.text("3. De acuerdo con la gráfica ""Age vs. Salary"", el rango de edad entre 35 y 41 años son en promedio los empleados con mayores ingresos, sin embargo, el la primera posición de ingresos corresponde a la edad de 67 años y en segundo lugar a la edad de 55 años. Por lo que se podría inferir que a la población de mayor edad le corresponden mayores ingresos en la organización.")

st.text("4. Por útlimo, de acuerdo con el gráfico ""Average Work Hours vs. Performance Score"", se identifica que la mayor calificación por desempeño no corresponde al mayor número de horas trabajadas, por lo que se podrías deducir que no necesariamente trabajar más tiempo genera mayor desempeño en las actividades laborales. ")


st.markdown("""
<hr style="height:2px;border:none;color:#333;background-color:#333;" />
""", unsafe_allow_html=True)

with st.expander("Employee Data"):

    # Gridview to show Employee's Data
    employees_subset =  employees_data[['name_employee'
                                        , 'birth_date'
                                        ,'age'
                                        ,'gender'
                                        ,'marital_status'
                                        ,'hiring_date'
                                        ,'position'
                                        ,'salary'
                                        ,'performance_score'
                                        ,'last_performance_date'
                                        ,'average_work_hours'
                                        ,'satisfaction_level'
                                        ,'absences'
                                        ]].rename(columns={'name_employee': 'Name Employee'
                                                        , 'birth_date': 'Birth Date'
                                                        ,'age':'Age'
                                                        ,'gender':'Gender'
                                                        ,'marital_status':'Marital Status'
                                                        ,'hiring_date':'Hiring Date'
                                                        ,'position':'Position'
                                                        ,'salary':'Salary'
                                                        ,'performance_score':'Performance Score'
                                                        ,'last_performance_date':'Last Performance Date'
                                                        ,'average_work_hours':'Average Work Hours'
                                                        ,'satisfaction_level':'Satisfaction Level'
                                                        ,'absences':'Absences'                                                       
                                                        })
    st.dataframe(employees_subset)

#•  Nombre del empleado (name_employee)
#•  Fecha de nacimiento (birth_date)
#•  Edad (age)
#•  Género (gender)
#•  Estado civil (marital_status)
#•  Fecha de contratación (hiring_date)
#•  Puesto (position)
#•  Salario (salary)
#•  Puntaje de desempeño (de 1 a 5, donde 5 es la máxima calificación) (performance_score)
#•  Fecha de revisión de desempeño más reciente (last_performance_date)
#•  Promedio de horas mensuales trabajadas (average_work_hours)
#•  Nivel de satisfacción de los empleados (satisfaction_level)
#•  Ausencias (absences)




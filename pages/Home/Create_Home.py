import streamlit as st
import Utils as ut

def Create_Home():  
    with st.container(): 
        ut.Divisor('Escola', 'mortarboard-fill','rgb(20,80,90)', 'Home01')
        st.write('\n \n')
        col1, col2, col3 = st.columns([3, 2, 3])
        col1_d, col2_d = st.columns([8, 0.01])

        with col1:
            st.write('')

        with col2:
            st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7IXmgTxQAaJ1q3vrff6Hzq1wC7_ScfywO0w&usqp=CAU', width=300, use_column_width='auto') 
        
        with col3:
            st.write('')
        
        with col1_d:
            st.write("""
6 - Uma escola precisa de um novo sistema para cadastro de estudantes, 
o sistema deve ser capaz de registrar novos alunos, respeitando a estrutura dos dados já existentes da escola. A lista a seguir é o exemplo da estrutura de dados utilizada pela escola. \n
Ex:
registros_alunos = [
    {
        "nome": "João Silva",
        "idade": 15,
        "classe": "9º ano",
        "notas": {"Matemática": 85, "Português": 78, "Ciências": 92, "História": 93}
    },
    {
        "nome": "Maria Oliveira",
        "idade": 14,
        "classe": "8º ano",
        "notas": {"Matemática": 90, "Português": 82, "Ciências": 88, "História": 84}
    },
    {
        "nome": "Carlos Santos",
        "idade": 16,
        "classe": "9º ano",
        "notas": {"Matemática": 78, "Português": 80, "Ciências": 75, "História": 78}
    },
    {
        "nome": "Ana Pereira",
        "idade": 15,
        "classe": "9º ano",
        "notas": {"Matemática": 92, "Português": 85, "Ciências": 90, "História": 88}
    },
    {
        "nome": "Pedro Costa",
        "idade": 14,
        "classe": "8º ano",
        "notas": {"Matemática": 88, "Português": 79, "Ciências": 84, "História": 80}
    }
]

6.1 Crie uma função para filtrar alunos por nome. \n
6.2 Crie uma função para filtrar alunos por ano \n
6.3 Crie uma função para filtrar alunos por desempenho em uma materia específica. \n
""")
        with col2_d:
            st.write('')
        
        st.write('\n \n')
        ut.Divisor('Copyright (c) 2024', '', 'rgb(20,80,90)', 'Home02')

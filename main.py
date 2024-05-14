import streamlit as st
import streamlit_antd_components as sac
import pages.Escola.FormEscola as fe
import pages.Escola.FormPesquisaEscola as fpe
from pages.Home.Create_Home import Create_Home    
from pages.Login.Login import login_page    
from Controllers.PadraoController import *  

def Main():
    # # Limpar os parâmetros necessários aqui
    st.session_state.Descricao = None

    # Menu
    with st.sidebar:
        st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT7IXmgTxQAaJ1q3vrff6Hzq1wC7_ScfywO0w&usqp=CAU', width=None, use_column_width='auto') 
        selected_usu = sac.menu([
            sac.MenuItem(f'Bem-vindo, "{st.session_state.Apelido_L}"!', icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
            # Usuário Logado
            sac.MenuItem(type='divider'),
            sac.MenuItem('Logout', icon=sac.BsIcon(name='box-arrow-left', color='red')),
            sac.MenuItem(type='divider'),
        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_login')
    
    if selected_usu == 'Logout':
        st.session_state.logged_in = False
        st.rerun()  
          
    with st.sidebar:
        selected = sac.menu([
            sac.MenuItem('Menu Principal', icon=sac.BsIcon(name='person-bounding-box', color='rgb(20,80,90)')),   
             # Empresa
            sac.MenuItem(type='divider'),
            sac.MenuItem('Novo Aluno',  icon=sac.BsIcon(name='person-fill', color='rgb(20,80,90)'), description='Adicionar novo Aluno'),
            # Clientes
            sac.MenuItem(type='divider'),
            sac.MenuItem('Listar Alunos', icon=sac.BsIcon(name='clipboard2-data', color='rgb(20,80,90)'), description='Listar os Alunos'),

        ], color='rgb(20,80,90)', open_all=False, return_index=False, index=0, key='Menu_principal')
    
    if selected == 'Menu Principal':
        Create_Home()
    elif selected == 'Novo Aluno':
        if __name__ == "__main__":
            fe.Form_Escola()
    elif selected == 'Listar Alunos':
         if __name__ == "__main__":
            fpe.Form_PesquisaEscola()   
          
# Lógica para alternar entre as páginas com base na ação do usuário
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
 
st.set_page_config(
    page_title="Escola",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded"
)   
        
if __name__ == "__main__":
    if st.session_state.logged_in:        
        Main()
    else:
        opcao = st.radio("Escolha uma opção:", ["Login"], horizontal= True)
        if opcao == "Login":
            if __name__ == "__main__":
                login_page()

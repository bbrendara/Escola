import this
from turtle import onclick
import streamlit as st;
import Controllers.AlunoController as AlunoController
import models.Aluno as aluno

def Create():
    idAlteracao = st.experimental_get_query_params()
    alunoRecuperado = None
    if idAlteracao.get("matricula") != None:
        idAlteracao = idAlteracao.get("matricula")[0]
        alunoRecuperado = AlunoController.SelecionarById(idAlteracao)
        st.experimental_set_query_params(
            matricula=[alunoRecuperado.matricula]
        )
        st.title("Alterar aluno")
    else:
        st.title("Incluir aluno")

    with st.form(key="include_aluno"):
        listserie = ["1º ano", "2º ano", "3º ano", "4º ano", "5º ano"]
        if alunoRecuperado == None:
            input_matricula = st.number_input(label="Insira a matrícula", format="%d",step=1)   
            input_nome = st.text_input(label="Insira o nome do aluno")
            input_serie = st.selectbox(label="Selecione a série", options=listserie)
            input_artes = st.number_input(label="Nota do aluno em artes (Campo não obrigatório)", format="%d",step=1)
            input_ciencias = st.number_input(label="Nota do aluno em ciências (Campo não obrigatório)", format="%d",step=1)
            input_fisica = st.number_input(label="Nota do aluno em educação física (Campo não obrigatório)", format="%d",step=1)
            input_geografia = st.number_input(label="Nota do aluno em geografia (Campo não obrigatório)", format="%d",step=1)
            input_historia = st.number_input(label="Nota do aluno em história (Campo não obrigatório)", format="%d",step=1)
            input_portugues = st.number_input(label="Nota do aluno em lingua portuguesa (Campo não obrigatório)", format="%d",step=1)
            input_matematica = st.number_input(label="Nota do aluno em matemática (Campo não obrigatório)", format="%d",step=1)
            
        else:
            input_matricula = st.number_input(label="Insira a matrícula", format="%d",step=1, value= alunoRecuperado.matricula)
            input_nome = st.text_input(label="Insira o nome do aluno", value=alunoRecuperado.nome)
            input_serie = st.selectbox(label="Selecione a série", options=listserie, index=listserie.index(alunoRecuperado.serie))
            input_artes = st.number_input(label="Nota do aluno em artes", format="%d",step=1, value= alunoRecuperado.artes)
            input_ciencias = st.number_input(label="Nota do aluno em ciências", format="%d",step=1, value= alunoRecuperado.ciencias)
            input_fisica = st.number_input(label="Nota do aluno em educação física", format="%d",step=1, value= alunoRecuperado.fisica)
            input_geografia = st.number_input(label="Nota do aluno em geografia", format="%d",step=1, value= alunoRecuperado.geografia)
            input_historia = st.number_input(label="Nota do aluno em história", format="%d",step=1, value= alunoRecuperado.historia)
            input_portugues = st.number_input(label="Nota do aluno em lingua portuguesa ", format="%d",step=1, value= alunoRecuperado.portugues)
            input_matematica = st.number_input(label="Nota do aluno em matemática", format="%d",step=1, value= alunoRecuperado.matematica)
        
            
        input_button_submit = st.form_submit_button("Enviar")


    if input_button_submit:
        if alunoRecuperado == None:
            AlunoController.Incluir(aluno.Aluno(input_matricula, input_nome, input_serie, input_artes, input_ciencias, input_fisica, input_geografia, input_historia, input_portugues, input_matematica))
            st.success("Aluno incluido com sucesso!")
        else:
            st.experimental_set_query_params()
            AlunoController.Alterar(aluno.Aluno(input_matricula, input_nome, input_serie, input_artes, input_ciencias, input_fisica, input_geografia, input_historia, input_portugues, input_matematica))
            st.success("Aluno alterado com sucesso!")
        
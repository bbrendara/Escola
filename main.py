from cgitb import text
from multiprocessing import Value
from os import write
from turtle import onclick, onscreenclick
from typing import List
from numpy.core.fromnumeric import size
import streamlit as st
import Pages.Aluno.Create as PageCreateAluno
import Pages.Aluno.List as PageListAluno


Page_aluno = st.sidebar.selectbox(
    'Boletim escolar', ['Incluir', 'Consultar'], 0)

if Page_aluno == 'Consultar':
    PageListAluno.List()

if Page_aluno == 'Incluir':
    st.experimental_set_query_params()
    PageCreateAluno.Create()
    

   

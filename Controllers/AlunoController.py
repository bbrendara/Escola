import string
from typing import List
import services.database as db;
import models.Aluno as aluno;
import numpy as np


def Incluir(aluno):
    count = db.cursor.execute("""
    INSERT INTO Estudante (imatricula, inome, iserie, iartes, iciencias, ifisica, igeografia, ihistoria, iportugues, imatematica) 
    VALUES (?,?,?,?,?,?,?,?,?, ?)""",
    aluno.matricula, aluno.nome, aluno.serie, aluno.artes, aluno.ciencias, aluno.fisica, aluno.geografia, aluno.historia, aluno.portugues, aluno.matematica).rowcount
    db.cnxn.commit()
    
def SelecionarById(matricula):
    db.cursor.execute("SELECT * FROM Estudante WHERE imatricula = ?", matricula)
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(aluno.Aluno(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    return costumerList[0]

def Alterar(aluno):
    count = db.cursor.execute("""
    UPDATE Estudante
    SET imatricula = ?, inome = ?, iserie = ?, iartes = ?, iciencias = ?, ifisica = ?, igeografia = ?, ihistoria = ?, iportugues = ?, imatematica = ?
    WHERE imatricula = ?
    """,
    aluno.matricula, aluno.nome, aluno.serie, aluno.artes, aluno.ciencias, aluno.fisica, aluno.geografia, aluno.historia, aluno.portugues, aluno.matematica, aluno.matricula).rowcount
    db.cnxn.commit()

def Excluir(matricula):
    count = db.cursor.execute("""
    DELETE FROM Estudante WHERE imatricula = ?""",
    matricula).rowcount
    db.cnxn.commit()

def SelecionarTodos():
    db.cursor.execute("SELECT * FROM Estudante")
    costumerList = []

    for row in db.cursor.fetchall():
        costumerList.append(aluno.Aluno(row[0], row[1],row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    return costumerList
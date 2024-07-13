from model.persona import Persona
from model.curso import Curso

objPersona=Persona("Luis","Salvatierra","98765432","lsavatierra@gmail.com")

objPersona.saludar()

objCurso=Curso("EPOO 1","C001","5")

objCurso.mostrar()
objCurso.set_credito(4)
objCurso.mostrar()

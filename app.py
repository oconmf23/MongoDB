from classes import Estudiante
from dotenv import load_dotenv

def main():
    estudiante = Estudiante("Mafer","Ocon","5555555")
    estudiante.save()
    estudiante.apellido = "Ocon Rosales"
    estudiante.update()

if __name__ =="__main__":
    load_dotenv()
    main()

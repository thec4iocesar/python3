#!/usr/bin/python3

from classes.Entidades import Paciente
from classes.Entidades import Funcionario
from datetime import date
from config.banco import session

# paciente = Paciente(nome='Joaquim dos Santos', dtnasc=date(1982,5,13))
# recepcionista = Funcionario(nome='Marcelo Dantas', cargo='Recepcionista', dtnasc=date(1978,3,5))
# medico = Funcionario(nome='Marielle Danjou', cargo='Médico', dtnasc=date(1978,3,5))

# session.add_all([
#     paciente,
#     recepcionista,
#     medico
# ])


session.add(paciente)

session.commit()
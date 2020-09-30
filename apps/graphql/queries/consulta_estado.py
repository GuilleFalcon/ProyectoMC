import graphene
import os

class EstadoServidor(graphene.ObjectType):
	estado = graphene.String()

	def resolve_estado(self, info):
		output = os.popen('screen -ls').read()
		if '.minecraft'  in output:
			return 'Encendido'
		else:
			return 'Apagado'
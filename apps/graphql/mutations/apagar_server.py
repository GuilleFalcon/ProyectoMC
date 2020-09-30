import graphene
import os

class ApagarServer(graphene.Mutation):
	estado = graphene.Boolean()

	def mutate(self, info):
		os.system('screen -S minecraft -X stuff "{}\015"'.format('stop'))
		return ApagarServer(estado=False)
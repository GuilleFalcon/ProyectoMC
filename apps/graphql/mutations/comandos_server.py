import graphene
import os

class ComandosServer(graphene.Mutation):
	cmd = graphene.String()
	class Arguments:
		cmd = graphene.String(required=True)

	def mutate(self, info, cmd):
		os.system('screen -S minecraft -X stuff "{}\015"'.format(cmd))
		return ComandosServer(cmd=cmd)
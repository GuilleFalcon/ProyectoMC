import graphene
import os


class IniciarServer(graphene.Mutation):
	estado = graphene.Boolean()

	def mutate(self, info):
		#'/home/erick/Escritorio/Server/'
		direccion = '/home/erick/Escritorio/Server/'
		nombre_jar = 'server-awa.jar'
		comando = 'screen -dmS "minecraft" java -Xmx1024M -Xms1024M -jar '+nombre_jar+' --nogui'

		#os.chdir se mueve a una dirección espesifica
		os.chdir(direccion)
		os.system(comando)
		return IniciarServer(estado=True)


#class IniciarServer(graphene.Mutation):
#	estado = graphene.Boolean()
#	minecraft_dir = graphene.String()
#	nombre_jar = graphene.String()
#	class Arguments:
#		minecraft_dir = graphene.String(required=True)
#		nombre_jar = graphene.String(required=True)
#
#	def mutate(self, info, minecraft_dir, nombre_jar):
#		direccion = minecraft_dir
#		comando = 'screen -dmS "minecraft" java -Xmx1024M -Xms1024M -jar '+nombre_jar+' --nogui'
#		os.chdir(direccion)
#		os.system(comando)
#		return IniciarServer(estado=True, minecraft_dir=minecraft_dir, nombre_jar=nombre_jar)
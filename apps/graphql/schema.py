import graphene
from .queries.consulta_estado import EstadoServidor
from .mutations.iniciar_server import IniciarServer
from .mutations.apagar_server import ApagarServer
from .mutations.comandos_server import ComandosServer

class Query(EstadoServidor):
    pass

class Mutation(graphene.ObjectType):
   prender = IniciarServer.Field()
   apagar = ApagarServer.Field()
   comando = ComandosServer.Field()
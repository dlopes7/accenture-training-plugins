import requests
import logging
from ruxit.api.base_plugin import RemoteBasePlugin

log = logging.getLogger(__name__)


class CustomExtensionDavidLopes(RemoteBasePlugin):

    def query(self, **kwargs):
        meu_nome = "David Lopes"
        log.info("Extension executando!")

        grupo = self.topology_builder.create_group(f"{meu_nome} - SpaceX", f"{meu_nome} - SpaceX")
        navios = self.get_ships()
        for navio in navios:

            log.info(navio["ship_name"])
            id_navio = f'{meu_nome} {navio["ship_id"]}'
            nome_navio = f'{meu_nome} {navio["ship_name"]}'

            device = grupo.create_device(id_navio, nome_navio)
            device.absolute("combustivel", navio["fuel"])


    def get_ships(self):
        return requests.get("http://ec2-18-207-157-255.compute-1.amazonaws.com/v3/ships").json()




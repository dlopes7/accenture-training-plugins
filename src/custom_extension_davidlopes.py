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

            # Cria o custom device
            id_navio = f'{meu_nome} {navio["ship_id"]}'
            nome_navio = f'{meu_nome} {navio["ship_name"]}'
            device = grupo.create_device(id_navio, nome_navio)

            # Manda uma métrica absoluta (simples)
            device.absolute("combustivel", navio["fuel"])

            # Métrica com dimensões
            for motor in navio["thrust"]:
                device.absolute("potencia", motor["power"], dimensions={"Motor": motor["engine"]})

            # Propriedades
            device.report_property("Tipo", navio.get("ship_type", "Desconhecido"))
            device.report_property("Porto", navio.get("home_port", "Desconhecido"))

            # Topologia
            device.add_endpoint(navio["ship_ip"])

            # Statetimeseries
            device.state_metric("clima", navio["weather"])

    def get_ships(self):
        return requests.get(f"{self.config['url']}/v3/ships").json()





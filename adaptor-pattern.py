from enum import Enum
from abc import ABC


class SOCKET_TYPES(Enum):
    M_TYPE = "M"
    G_TYPE = "G"

class Charger(ABC):
    supported_voltage = None
    supported_socket = None


class PlugChargerMixin:    
    def plug_charger(self, charger: Charger):
        if charger.supported_socket == self.socket and charger.supported_voltage == self.voltage:
            print("Charger compatible. Charging ON.")
        else:
            print("Incompatible charger. Unable to charge.")


class Socket(ABC, PlugChargerMixin):
    voltage = None
    socket = None


class UAESocket(Socket):
    def __init__(self):
        self.voltage = 180
        self.socket = SOCKET_TYPES.G_TYPE


class IndianSocket(Socket):
    def __init__(self):
        self.voltage = 230
        self.socket = SOCKET_TYPES.M_TYPE


class UAECharger(Charger):
    def __init__(self):
        self.supported_voltage = 180
        self.supported_socket = SOCKET_TYPES.G_TYPE

class IndianCharger(Charger):
    def __init__(self):
        self.supported_voltage = 230
        self.supported_socket = SOCKET_TYPES.M_TYPE

class IndiaToUAEAdaptor(Charger):
    def __init__(self, charger: IndianCharger) -> None:
        self.supported_voltage = charger.supported_voltage - 50
        self.supported_socket = SOCKET_TYPES.G_TYPE

if __name__ == '__main__':
    uae_socket = UAESocket()
    indian_charger = IndianCharger()
    uae_socket.plug_charger(indian_charger)

    indiansocket = IndianSocket()
    indiansocket.plug_charger(indian_charger)

    india_to_uae_adaptor = IndiaToUAEAdaptor(indian_charger)
    uae_socket.plug_charger(india_to_uae_adaptor)


# Output
# Incompatible charger. Unable to charge.
# Charger compatible. Charging ON.
# Charger compatible. Charging ON.

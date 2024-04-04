# Каротажи SP по скважинам
class WellLogging:
    MD: float # m
    SP: float # mV

    def __init__(self, MD, SP):
        self.MD = MD
        self.SP = SP

    def __str__(self) -> str:
        return f'MD, m: {self.MD}; SP, mV: {self.SP}'

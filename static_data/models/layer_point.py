class LayerPoint:
    H: float
    FWL_bottom: float
    S_poro: float
    S_perm: float

    def __init__(self, H, FWL_bottom, S_poro, S_perm):
        self.H = H
        self.FWL_bottom = FWL_bottom
        self.S_poro = S_poro
        self.S_perm = S_perm

    def __str__(self) -> str:
        return f'H: {self.H}, FWL_bottom: {self.FWL_bottom}, S_poro: {self.S_poro}, S_perm: {self.S_perm}'

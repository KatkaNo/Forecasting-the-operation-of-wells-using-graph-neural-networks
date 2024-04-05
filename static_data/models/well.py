from models.well_logging import WellLogging
from models.layer_point import LayerPoint
from datetime import date


# Скважина
class Well:
    well_name: str
    x: int
    y: int
    bottom: int
    is_extracting: bool
    loggings: list[WellLogging]
    start_date: date
    layer_point: LayerPoint

    def __init__(self, well: str, x: int, y: int, bottom: int, 
                 well_logs: list[WellLogging], start_date: date, layer_point):
        self.well_name = well
        self.is_extracting = well[0] == 'P'
        self.x = x
        self.y = y
        self.bottom = bottom
        self.loggings = well_logs.copy()
        self.start_date = start_date
        self.layer_point = layer_point

    def __str__(self) -> str:
        return f'''{self.well_name}: xy=({self.x}; {self.y}), 
        bottom: {self.bottom}, opened at: {self.start_date}. 
        Logs: {len(self.loggings)} item(s). Layer: {self.layer_point}'''

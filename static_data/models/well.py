from models.well_logging import WellLogging
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

    def __init__(self, well: str, x: int, y: int, bottom: int, 
                 well_logs: list[WellLogging], start_date: date):
        self.well_name = well
        self.is_extracting = well[0] == 'P'
        self.x = x
        self.y = y
        self.bottom = bottom
        self.loggings = well_logs.copy()
        self.start_date = start_date

    def __str__(self) -> str:
        return f'{self.well_name}: xy=({self.x}; {self.y}), bottom: {self.bottom}, opened at: {self.start_date}. Logs: {len(self.loggings)} item(s)'

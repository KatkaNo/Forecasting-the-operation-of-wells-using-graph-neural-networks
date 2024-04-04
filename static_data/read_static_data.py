import pandas as pd
from models.well_logging import WellLogging
from models.well import Well


FILENAME = 'Исходные данные SRM-6.xlsx'



def read_static_data():
    wells_df = pd.read_excel(FILENAME, 
                      sheet_name='Скважины',
                      header=3,
                      usecols='B:E'
    )
        
    loggings = pd.read_excel(FILENAME,
                            sheet_name='Каротажи',
                            header=4,
                            usecols='B:R'
    )
    dates =  pd.read_excel(FILENAME, 
                        sheet_name='График бурения',
                        header=3,
                        usecols='B:C'
    )

    wells = []
    for i in wells_df.index:
        well = wells_df.loc[i]
        name = well['Well']
        x = well['X']
        y = well['Y']
        bottom = well['Bottom']
        well_logs_df = loggings.iloc[:, i*3 : i*3+2]
        well_logs = []
        well_logs_df = well_logs_df.dropna()
        for j in well_logs_df.index:
            log = well_logs_df.loc[j]
            well_logs.append(WellLogging(log.iloc[0], log.iloc[1]))
        
        wells.append(Well(
            well=name,
            x=x,
            y=y,
            bottom=bottom,
            well_logs=well_logs,
            start_date=dates.loc[i]['Бурение']
        ))
    return wells



if __name__ == "__main__":
    print(*read_static_data(), sep='\n')

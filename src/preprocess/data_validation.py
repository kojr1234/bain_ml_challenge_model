from typing import List, Optional, Tuple, Union

import numpy as np
import pandas as pd
from pydantic import BaseModel, ValidationError

class RainfallDataInputSchema(BaseModel):
    date: Optional[str]
    Coquimbo: Optional[float]
    Valparaiso: Optional[float]
    Metropolitana_de_Santiago: Optional[float]
    Libertador_Gral__Bernardo_O_Higgins: Optional[float]
    Maule: Optional[float]
    Biobio: Optional[float]
    La_Araucania: Optional[float]
    Los_Rios: Optional[float]
    # Transported: Optional[str] target variable should not be included
    
class CentralBankDataInputSchema(BaseModel):
    Periodo: Optional[str]
    Imacec_empalmado: Optional[str]
    Imacec_produccion_de_bienes: Optional[str]
    Imacec_minero: Optional[str]
    Imacec_industria: Optional[str]
    Imacec_resto_de_bienes: Optional[str]
    Imacec_comercio: Optional[str]
    Imacec_servicios: Optional[str]
    Imacec_a_costo_de_factores: Optional[str]
    Imacec_no_minero: Optional[str]
    PIB_Agropecuario_silvicola: Optional[str]
    PIB_Pesca: Optional[str]
    PIB_Mineria: Optional[str]
    PIB_Mineria_del_cobre: Optional[str]
    PIB_Otras_actividades_mineras: Optional[str]
    PIB_Industria_Manufacturera: Optional[str]
    PIB_Alimentos: Optional[str]
    PIB_Bebidas_y_tabaco: Optional[str]
    PIB_Textil: Optional[str]
    PIB_Maderas_y_muebles: Optional[str]
    PIB_Celulosa: Optional[str]
    PIB_Refinacion_de_petroleo: Optional[str]
    PIB_Quimica: Optional[str]
    PIB_Minerales_no_metalicos_y_metalica_basica: Optional[str]
    PIB_Productos_metalicos: Optional[str]
    PIB_Electricidad: Optional[str]
    PIB_Construccion: Optional[str]
    PIB_Comercio: Optional[str]
    PIB_Restaurantes_y_hoteles: Optional[str]
    PIB_Transporte: Optional[str]
    PIB_Comunicaciones: Optional[str]
    PIB_Servicios_financieros: Optional[str]
    PIB_Servicios_empresariales: Optional[str]
    PIB_Servicios_de_vivienda: Optional[str]
    PIB_Servicios_personales: Optional[str]
    PIB_Administracion_publica: Optional[str]
    PIB_a_costo_de_factores: Optional[str]
    Impuesto_al_valor_agregado: Optional[str]
    Derechos_de_Importacion: Optional[str]
    PIB: Optional[str]
    Precio_de_la_gasolina_en_EEUU_dolaresm3: Optional[str]
    Precio_de_la_onza_troy_de_oro_dolaresoz: Optional[float]
    Precio_de_la_onza_troy_de_plata_dolaresoz: Optional[float]
    Precio_del_cobre_refinado_BML_dolareslibra: Optional[str]
    Precio_del_diesel_centavos_de_dolargalon: Optional[float]
    Precio_del_gas_natural_dolaresmillon_de_unidades_termicas_britanicas: Optional[float]
    Precio_del_petroleo_Brent_dolaresbarril: Optional[float]
    Precio_del_kerosene_dolaresm3: Optional[str]
    Precio_del_petroleo_WTI_dolaresbarril: Optional[float]
    Precio_del_propano_centavos_de_dolargalon_DTN: Optional[float]
    Tipo_de_cambio_del_dolar_observado_diario: Optional[str]
    Ocupados: Optional[str]
    Ocupacion_en_Agricultura_INE: Optional[str]
    Ocupacion_en_Explotacion_de_minas_y_canteras_INE: Optional[str]
    Ocupacion_en_Industrias_manufactureras_INE: Optional[str]
    Ocupacion_en_Suministro_de_electricidad_INE: Optional[str]
    Ocupacion_en_Actividades_de_servicios_administrativos_y_de_apoyo_INE: Optional[str]
    Ocupacion_en_Actividades_profesionales_INE: Optional[str]
    Ocupacion_en_Actividades_inmobiliarias_INE: Optional[str]
    Ocupacion_en_Actividades_financieras_y_de_seguros_INE: Optional[str]
    Ocupacion_en_Informacion_y_comunicaciones_INE: Optional[str]
    Ocupacion_en_Transporte_y_almacenamiento_INE: Optional[str]
    Ocupacion_en_Actividades_de_alojamiento_y_de_servicio_de_comidas_INE: Optional[str]
    Ocupacion_en_Construccion_INE: Optional[str]
    Ocupacion_en_Comercio_INE: Optional[str]
    Ocupacion_en_Suministro_de_agua_evacuacion_de_aguas_residuales_INE: Optional[str]
    Ocupacion_en_Administracion_publica_y_defensa_INE: Optional[str]
    Ocupacion_en_Enseanza_INE: Optional[str]
    Ocupacion_en_Actividades_de_atencion_de_la_salud_humana_y_de_asistencia_social_INE: Optional[str]
    Ocupacion_en_Actividades_artisticas_INE: Optional[str]
    Ocupacion_en_Otras_actividades_de_servicios_INE: Optional[str]
    Ocupacion_en_Actividades_de_los_hogares_como_empleadores_INE: Optional[str]
    Ocupacion_en_Actividades_de_organizaciones_y_organos_extraterritoriales_INE: Optional[str]
    No_sabe__No_responde_Miles_de_personas: Optional[str]
    Tipo_de_cambio_nominal_multilateral___TCM: Optional[str]
    Indice_de_tipo_de_cambio_real___TCR_promedio_1986_100: Optional[str]
    Indice_de_produccion_industrial: Optional[str]
    Indice_de_produccion_industrial__mineria: Optional[str]
    Indice_de_produccion_industrial_electricidad__gas_y_agua: Optional[str]
    Indice_de_produccion_industrial__manufacturera: Optional[str]
    Generacion_de_energia_electrica_CDEC_GWh: Optional[str]
    Indice_de_ventas_comercio_real_IVCM: Optional[str]
    Indice_de_ventas_comercio_real_no_durables_IVCM: Optional[str]
    Indice_de_ventas_comercio_real_durables_IVCM: Optional[str]
    Ventas_autos_nuevos: Optional[float]

class MilkPriceDataInputSchema(BaseModel):
    Anio: Optional[int]
    Mes: Optional[str]
    Precio_leche: Optional[float]

class MultipleRainfallDataInputs(BaseModel):
    # it will receive a list of dictionary
    # each element is a row of the dataset
    inputs: List[RainfallDataInputSchema]

class MultipleCentralBankDataInputs(BaseModel):
    # it will receive a list of dictionary
    # each element is a row of the dataset
    inputs: List[CentralBankDataInputSchema]

class MultipleMilkPriceDataInputs(BaseModel):
    # it will receive a list of dictionary
    # each element is a row of the dataset
    inputs: List[MilkPriceDataInputSchema]

def validate_inputs(*, 
    rainfall_data: pd.DataFrame,
    centralbank_data: pd.DataFrame,
    milkprice_data: pd.DataFrame) -> tuple[pd.DataFrame, Optional[str]]:
    """
    This function validates the input data column values
    """

    rainfall_errors = None
    try:
        MultipleRainfallDataInputs(
            inputs=rainfall_data.replace({np.nan: None}).to_dict(orient='records')
        )
    except ValidationError as error:
        rainfall_errors = error.args

    centralbank_errors = None
    try:
        MultipleCentralBankDataInputs(
            inputs=centralbank_data.replace({np.nan: None}).to_dict(orient='records')
        )
    except ValidationError as error:
        centralbank_errors = error.args
    
    milkprice_errors = None
    try:
        MultipleMilkPriceDataInputs(
            inputs=milkprice_data.replace({np.nan: None}).to_dict(orient='records')
        )
    except ValidationError as error:
        milkprice_errors = error.args

    return_data = {
        'rainfall': {'data': rainfall, 'errors': rainfall_errors},
        'centralbank': {'data': centralbank_data, 'errors': centralbank_errors},
        'milkprice': {'data': milkprice_data, 'errors': milkprice_errors}
    }

    return return_data
        
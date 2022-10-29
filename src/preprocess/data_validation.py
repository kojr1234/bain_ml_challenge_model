from typing import List, Optional, Tuple, Union, Any

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
    class Config:
        # the schema_extra example here
        # is used for placeholder default in
        # our api docs
        # the schema_extra allows to exnted
        # or override the already existent
        # json schema using the key examples
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "date":"2020-04-01",
                        "Coquimbo":0.5560849673,
                        "Valparaiso":4.6647077922,
                        "Metropolitana_de_Santiago":16.0337751678,
                        "Libertador_Gral__Bernardo_O_Higgins":19.795751938,
                        "Maule":37.3485108153,
                        "Biobio":66.764275266,
                        "La_Araucania":73.8132901752,
                        "Los_Rios":140.0767571059 
                    }
                ]
            }
        }

class MultipleCentralBankDataInputs(BaseModel):
    # it will receive a list of dictionary
    # each element is a row of the dataset
    inputs: List[CentralBankDataInputSchema]
    class Config:
        # the schema_extra example here
        # is used for placeholder default in
        # our api docs
        # the schema_extra allows to exnted
        # or override the already existent
        # json schema using the key examples
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Periodo":"2020-04-01 00:00:00 UTC",
                        "Imacec_empalmado":"988.542.998",
                        "Imacec_produccion_de_bienes":"100.570.487",
                        "Imacec_minero":"986.442.174",
                        "Imacec_industria":"969.425.393",
                        "Imacec_resto_de_bienes":"104.850.643",
                        "Imacec_comercio":"926.889.279",
                        "Imacec_servicios":"100.658.794",
                        "Imacec_a_costo_de_factores":"99.848.482",
                        "Imacec_no_minero":"987.676.061",
                        "PIB_Agropecuario_silvicola":"363.141.386",
                        "PIB_Pesca":"103.928.937",
                        "PIB_Mineria":"124.486.767",
                        "PIB_Mineria_del_cobre":"112.002.235",
                        "PIB_Otras_actividades_mineras":"125.671.822",
                        "PIB_Industria_Manufacturera":"123.809.203",
                        "PIB_Alimentos":"371.654.364",
                        "PIB_Bebidas_y_tabaco":"141.425.146",
                        "PIB_Textil":"138.774.296",
                        "PIB_Maderas_y_muebles":"561.712.194",
                        "PIB_Celulosa":"102.107.754",
                        "PIB_Refinacion_de_petroleo":"709.361.006",
                        "PIB_Quimica":"189.715.716",
                        "PIB_Minerales_no_metalicos_y_metalica_basica":"577.871.238",
                        "PIB_Productos_metalicos":"218.328.917",
                        "PIB_Electricidad":"310.498.611",
                        "PIB_Construccion":"719.814.687",
                        "PIB_Comercio":"96.673.133",
                        "PIB_Restaurantes_y_hoteles":"123.964.781",
                        "PIB_Transporte":"427.830.949",
                        "PIB_Comunicaciones":"421.132.099",
                        "PIB_Servicios_financieros":"744.844.553",
                        "PIB_Servicios_empresariales":"119.801.603",
                        "PIB_Servicios_de_vivienda":"929.186.849",
                        "PIB_Servicios_personales":"113.174.769",
                        "PIB_Administracion_publica":"608.806.973",
                        "PIB_a_costo_de_factores":"104.996.697",
                        "Impuesto_al_valor_agregado":"810.937.543",
                        "Derechos_de_Importacion":"443.485.676",
                        "PIB":"113.580.473",
                        "Precio_de_la_gasolina_en_EEUU_dolaresm3":"14.657.816",
                        "Precio_de_la_onza_troy_de_oro_dolaresoz":1686.32,
                        "Precio_de_la_onza_troy_de_plata_dolaresoz":151.171,
                        "Precio_del_cobre_refinado_BML_dolareslibra":"228.987.118",
                        "Precio_del_diesel_centavos_de_dolargalon":79.49,
                        "Precio_del_gas_natural_dolaresmillon_de_unidades_termicas_britanicas":1.7386,
                        "Precio_del_petroleo_Brent_dolaresbarril":23.34,
                        "Precio_del_kerosene_dolaresm3":"16.176.966",
                        "Precio_del_petroleo_WTI_dolaresbarril":16.52,
                        "Precio_del_propano_centavos_de_dolargalon_DTN":32.56,
                        "Tipo_de_cambio_del_dolar_observado_diario":"853.379.048",
                        "Ocupados":"823.593.079",
                        "Ocupacion_en_Agricultura_INE":"598.610.099",
                        "Ocupacion_en_Explotacion_de_minas_y_canteras_INE":"224.662.856",
                        "Ocupacion_en_Industrias_manufactureras_INE":"809.715.366",
                        "Ocupacion_en_Suministro_de_electricidad_INE":"526.575.846",
                        "Ocupacion_en_Actividades_de_servicios_administrativos_y_de_apoyo_INE":"280.173.856",
                        "Ocupacion_en_Actividades_profesionales_INE":"279.400.485",
                        "Ocupacion_en_Actividades_inmobiliarias_INE":"870.253.865",
                        "Ocupacion_en_Actividades_financieras_y_de_seguros_INE":"189.650.182",
                        "Ocupacion_en_Informacion_y_comunicaciones_INE":"168.809.978",
                        "Ocupacion_en_Transporte_y_almacenamiento_INE":"525.126.797",
                        "Ocupacion_en_Actividades_de_alojamiento_y_de_servicio_de_comidas_INE":"344.474.955",
                        "Ocupacion_en_Construccion_INE":"682.082.615",
                        "Ocupacion_en_Comercio_INE":"152.862.437",
                        "Ocupacion_en_Suministro_de_agua_evacuacion_de_aguas_residuales_INE":"625.883.032",
                        "Ocupacion_en_Administracion_publica_y_defensa_INE":"493.383.376",
                        "Ocupacion_en_Enseanza_INE":"721.169.492",
                        "Ocupacion_en_Actividades_de_atencion_de_la_salud_humana_y_de_asistencia_social_INE":"521.398.817",
                        "Ocupacion_en_Actividades_artisticas_INE":"828.194.928",
                        "Ocupacion_en_Otras_actividades_de_servicios_INE":"274.863.546",
                        "Ocupacion_en_Actividades_de_los_hogares_como_empleadores_INE":"281.386.489",
                        "Ocupacion_en_Actividades_de_organizaciones_y_organos_extraterritoriales_INE":"0",
                        "No_sabe__No_responde_Miles_de_personas":"273.067.521",
                        "Tipo_de_cambio_nominal_multilateral___TCM":"121.110.952",
                        "Indice_de_tipo_de_cambio_real___TCR_promedio_1986_100":"105.982.122",
                        "Indice_de_produccion_industrial":"960.396.492",
                        "Indice_de_produccion_industrial__mineria":"928.533.255",
                        "Indice_de_produccion_industrial_electricidad__gas_y_agua":"100.815.336",
                        "Indice_de_produccion_industrial__manufacturera":"980.837.688",
                        "Generacion_de_energia_electrica_CDEC_GWh":"6181.5",
                        "Indice_de_ventas_comercio_real_IVCM":"757.349.073",
                        "Indice_de_ventas_comercio_real_no_durables_IVCM":"763.378.636",
                        "Indice_de_ventas_comercio_real_durables_IVCM":"731.898.208",
                        "Ventas_autos_nuevos":8906.0
                    }
                ]
            }
        }

class MultipleMilkPriceDataInputs(BaseModel):
    # it will receive a list of dictionary
    # each element is a row of the dataset
    inputs: List[MilkPriceDataInputSchema]
    class Config:
        # the schema_extra example here
        # is used for placeholder in
        # our api
        # the schema_extra allows to exnted
        # or override the already existent
        # json schema using the key examples
        schema_extra = {
            "example": {
                "inputs": [
                    {
                        "Anio":2020,
                        "Mes":"Abr",
                        "Precio_leche":316.25
                    }
                ]
            }
        }

def validate_inputs(*, 
    rainfall_data: pd.DataFrame,
    centralbank_data: pd.DataFrame,
    milkprice_data: pd.DataFrame) -> tuple[pd.DataFrame, Optional[str]]:
    """
    This function validates the input data column values.
    To validate, pydantic provide a number of auxiliary variables
    to ensure the data consistency. If the data values don't match
    the types defined in the schema, pydantic raises an error. 
    Pydantic also has other advantages, such as automatically
    converting strings to numerical if applicable.
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
        'rainfall': {'data': rainfall_data, 'errors': rainfall_errors},
        'centralbank': {'data': centralbank_data, 'errors': centralbank_errors},
        'milkprice': {'data': milkprice_data, 'errors': milkprice_errors}
    }

    return return_data


        
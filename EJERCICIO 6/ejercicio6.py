TDA_PADRON_2023 = {
    "TDA_FECHA": "2023-10-01",
    "TDA_LISTA_PROVINCIAS": [
        {
            "Provincia": "Buenos Aires",
            "TDA_LISTA_VOTANTES": [
                {
                    "DNI": "12345678",
                    "ApellidoNombre": "Martinez Juan",
                    "CodigoLugarVotacion": "L001",
                    "MesaVotacion": 12
                },
                {
                    "DNI": "23456789",
                    "ApellidoNombre": "Gomez Laura",
                    "CodigoLugarVotacion": "L002",
                    "MesaVotacion": 8
                }
            ]
        },
        {
            "Provincia": "Córdoba",
            "TDA_LISTA_VOTANTES": [
                {
                    "DNI": "34567890",
                    "ApellidoNombre": "Fernandez Pablo",
                    "CodigoLugarVotacion": "L003",
                    "MesaVotacion": 22
                }
            ]
        }
    ],
    "TDA_LISTA_LUGARES": [
        {
            "CodigoLugarVotacion": "L001",
            "DireccionLocalidad": {
                "Direccion": "Av. Rivadavia 1000",
                "Localidad": "Ciudad Autónoma de Buenos Aires"
            }
        },
        {
            "CodigoLugarVotacion": "L002",
            "DireccionLocalidad": {
                "Direccion": "Calle Mitre 750",
                "Localidad": "La Plata"
            }
        },
        {
            "CodigoLugarVotacion": "L003",
            "DireccionLocalidad": {
                "Direccion": "Bv. San Juan 850",
                "Localidad": "Córdoba Capital"
            }
        }
    ]
}

# consultar lugar de votacion

def Consultar_Lugar_Votacion(padron, provincia, dni):
    encontrado = False
    registro = {}

    for prov in padron["TDA_LISTA_PROVINCIAS"]:
        if prov["Provincia"] == provincia:
            for votante in prov["TDA_LISTA_VOTANTES"]:
                if votante["DNI"] == dni:
                    encontrado = True
                    codigo_lugar = votante["CodigoLugarVotacion"]
                    mesa = votante["MesaVotacion"]
                    
                    for lugar in padron["TDA_LISTA_LUGARES"]:
                        if lugar["CodigoLugarVotacion"] == codigo_lugar:
                            registro = {
                                "Direccion": lugar["DireccionLocalidad"]["Direccion"],
                                "Localidad": lugar["DireccionLocalidad"]["Localidad"],
                                "Mesa": mesa
                            }
                            break
                    break
            break

    return encontrado, registro


# prueba 


provincia = "Buenos Aires"
dni = "12345678"

encontrado, registro = Consultar_Lugar_Votacion(TDA_PADRON_2023, provincia, dni)

if encontrado:
    print("Votante encontrado:")
    print("Dirección:", registro["Direccion"])
    print("Localidad:", registro["Localidad"])
    print("Mesa:", registro["Mesa"])
else:
    print("Votante no encontrado.")

def calcular_puntaje (item):
    equipo,datos=item
    puntos= 3 * datos['innovacion'] + datos['presentacion']
    if datos['errores']:
        puntos -= 1
    return equipo, puntos

def mostrar_tabla (resultados):
    tabla = sorted(resultados.items(), key=lambda x: x[1]['puntos'], reverse=True)
    print(f"{'Equipo':<10}{'Puntos':<8}{'Innov.':<8}{'Pres.':<8}{'Errores':<10}{'MER':<5}")
    print("-" *50)
    for equipo, stats in tabla:
        print(f"{equipo:<10}{stats['puntos']:<8}{stats['innovacion']:<8}{stats['presentacion']:<8}{stats['errores']:<10}{stats['mer']:<5}")

def equipos_con_errores (ronda):
    return list(map(lambda x: x[0], filter(lambda x: x[1]['errores'], ronda.items())))
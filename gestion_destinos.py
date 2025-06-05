# gestion_destinos.py
destinos = []  # Lista para almacenar destinos

def agregar_destino(ciudad, pais, costo_base):
    if not ciudad or not pais:
        print("Error: Ciudad y país son obligatorios.")
        return
    if costo_base < 0:
        print("Error: El costo no puede ser negativo.")
        return
    destino = {"id": len(destinos) + 1, "ciudad": ciudad, "pais": pais, "costo_base": costo_base}
    destinos.append(destino)
    print(f"Destino guardado: {ciudad}, {pais}")

def listar_destinos():
    if not destinos:
        print("No hay destinos.")
    else:
        for d in destinos:
            print(f"ID: {d['id']}, Ciudad: {d['ciudad']}, País: {d['pais']}, Costo: ${d['costo_base']}")

def modificar_destino(id_destino, ciudad, pais, costo_base):
    if not ciudad or not pais:
        print("Error: Ciudad y país son obligatorios.")
        return
    if costo_base < 0:
        print("Error: El costo no puede ser negativo.")
        return
    for d in destinos:
        if d["id"] == id_destino:
            d["ciudad"] = ciudad
            d["pais"] = pais
            d["costo_base"] = costo_base
            print(f"Destino ID {id_destino} modificado.")
            return
    print("Destino no encontrado.")

def eliminar_destino(id_destino):
    for d in destinos:
        if d["id"] == id_destino:
            destinos.remove(d)
            print(f"Destino ID {id_destino} eliminado.")
            return
    print("Destino no encontrado.")

# gestion_clientes.py
clientes = []  # Lista para almacenar clientes

def agregar_cliente(razon_social, cuit, correo):
    if not razon_social or not cuit or not correo:
        print("Error: Todos los campos son obligatorios.")
        return
    cliente = {"id": len(clientes) + 1, "razon_social": razon_social, "cuit": cuit, "correo": correo}
    clientes.append(cliente)
    print(f"Cliente guardado: {razon_social}")

def listar_clientes():
    if not clientes:
        print("No hay clientes.")
    else:
        for c in clientes:
            print(f"ID: {c['id']}, Razón Social: {c['razon_social']}, CUIT: {c['cuit']}, Email: {c['correo']}")

def modificar_cliente(id_cliente, razon_social, cuit, correo):
    if not razon_social or not cuit or not correo:
        print("Error: Todos los campos son obligatorios.")
        return
    for c in clientes:
        if c["id"] == id_cliente:
            c["razon_social"] = razon_social
            c["cuit"] = cuit
            c["correo"] = correo
            print(f"Cliente ID {id_cliente} modificado.")
            return
    print("Cliente no encontrado.")

def eliminar_cliente(id_cliente):
    for c in clientes:
        if c["id"] == id_cliente:
            clientes.remove(c)
            print(f"Cliente ID {id_cliente} eliminado.")
            return
    print("Cliente no encontrado.")

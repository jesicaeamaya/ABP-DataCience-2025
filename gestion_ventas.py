# gestion_ventas.py
from datetime import datetime, timedelta
from gestion_clientes import clientes
from gestion_destinos import destinos

ventas = []  # Lista para almacenar ventas

def registrar_venta(id_cliente, id_destino, costo):
    if costo < 0:
        print("Error: El costo no puede ser negativo.")
        return
    if not any(c["id"] == id_cliente for c in clientes):
        print("Error: Cliente no encontrado.")
        return
    if not any(d["id"] == id_destino for d in destinos):
        print("Error: Destino no encontrado.")
        return
    venta = {
        "id": len(ventas) + 1,
        "id_cliente": id_cliente,
        "id_destino": id_destino,
        "fecha": datetime.now(),
        "costo": costo,
        "estado": "Activa"
    }
    ventas.append(venta)
    print(f"Venta ID {venta['id']} registrada.")

def listar_todas_ventas():
    if not ventas:
        print("No hay ventas.")
    else:
        for v in ventas:
            print(f"ID: {v['id']}, Cliente ID: {v['id_cliente']}, Destino ID: {v['id_destino']}, Fecha: {v['fecha'].strftime('%Y-%m-%d %H:%M')}, Costo: ${v['costo']}, Estado: {v['estado']}")

def ventas_mas_vendidas():
    if not ventas:
        print("No hay ventas.")
        return
    destinos_count = {}
    for v in ventas:
        if v["estado"] == "Activa":
            destinos_count[v["id_destino"]] = destinos_count.get(v["id_destino"], 0) + 1
    if destinos_count:
        max_destino = max(destinos_count, key=destinos_count.get)
        print(f"Destino más vendido: ID {max_destino}, {destinos_count[max_destino]} veces")

def ventas_ultima_semana():
    semana_pasada = datetime.now() - timedelta(days=7)
    ventas_recientes = [v for v in ventas if v["fecha"] >= semana_pasada and v["estado"] == "Activa"]
    if not ventas_recientes:
        print("No hay ventas en la última semana.")
    else:
        for v in ventas_recientes:
            print(f"ID: {v['id']}, Cliente ID: {v['id_cliente']}, Destino ID: {v['id_destino']}, Fecha: {v['fecha'].strftime('%Y-%m-%d %H:%M')}, Costo: ${v['costo']}")

def ventas_por_anio(anio):
    ventas_anio = [v for v in ventas if v["fecha"].year == anio and v["estado"] == "Activa"]
    if not ventas_anio:
        print(f"No hay ventas en {anio}.")
    else:
        for v in ventas_anio:
            print(f"ID: {v['id']}, Cliente ID: {v['id_cliente']}, Destino ID: {v['id_destino']}, Fecha: {v['fecha'].strftime('%Y-%m-%d %H:%M')}, Costo: ${v['costo']}")

def ventas_por_destino(id_destino):
    if not any(d["id"] == id_destino for d in destinos):
        print("Error: Destino no encontrado.")
        return
    ventas_destino = [v for v in ventas if v["id_destino"] == id_destino and v["estado"] == "Activa"]
    if not ventas_destino:
        print(f"No hay ventas para destino ID {id_destino}.")
    else:
        for v in ventas_destino:
            print(f"ID: {v['id']}, Cliente ID: {v['id_cliente']}, Fecha: {v['fecha'].strftime('%Y-%m-%d %H:%M')}, Costo: ${v['costo']}")

def boton_arrepentimiento(id_venta):
    for v in ventas:
        if v["id"] == id_venta:
            if v["estado"] == "Anulada":
                print("Venta ya anulada.")
                return
            if (datetime.now() - v["fecha"]).total_seconds() <= 300:  # 5 minutos
                v["estado"] = "Anulada"
                print(f"Venta ID {id_venta} anulada.")
            else:
                print("No se puede anular: han pasado más de 5 minutos.")
            return
    print("Venta no encontrada.")

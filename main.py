''' SkyRoute - Sistema de Gestión de Pasajes Aéreos
    Proyecto ABP - Evidencia 3
    Integrantes del grupo:
        Milton Amaya, DNI:30.310.864
        Otto Acosta, DNI:35.764.199
        Jesica Elizabeth Amaya, DNI:27.660.701
        Shunko Rodriguez, DNI:30.151.105
        Rocío Belén Issetta, DNI:39.172.315
        Torres Álvaro Matías, DNI:44.037.240
        
    Cómo ejecutar:
        Abrir terminal y correr: python main.py
'''
from gestion_clientes import agregar_cliente, listar_clientes, modificar_cliente, eliminar_cliente
from gestion_destinos import agregar_destino, listar_destinos, modificar_destino, eliminar_destino
from gestion_ventas import registrar_venta, listar_todas_ventas, ventas_mas_vendidas, ventas_ultima_semana, ventas_por_anio, ventas_por_destino, boton_arrepentimiento

menu = '''
        Bienvenidos a SkyRoute - Sistema de Gestión de Pasajes
        ------------------------------------------------------
        1. Gestionar Clientes
        2. Gestionar Destinos
        3. Gestionar Ventas
        4. Consultar Ventas
        5. Botón de Arrepentimiento
        6. Ver Reporte General
        7. Acerca del Sistema
        8. Salir       
'''
submenu_clientes = '''
        -- GESTIONAR CLIENTES --
        1. Ver Clientes
        2. Agregar Cliente
        3. Modificar Cliente
        4. Eliminar Cliente
        5. Volver al Menú Principal
'''
submenu_destinos = '''
        -- GESTIONAR DESTINOS --
        1. Ver Destinos
        2. Agregar Destino
        3. Modificar Destino
        4. Eliminar Destino
        5. Volver al Menú Principal
'''
submenu_consultas = '''
        -- GESTIONAR CONSULTA DE VENTAS --
        1. Ver todas las ventas
        2. Ventas más vendidas
        3. Ventas de la última semana
        4. Ventas por año
        5. Ver ventas por destino
        6. Volver al Menú Principal
'''

while True:
    print(menu)
    opcion = input('    Seleccione una opción: ')

    if opcion == '1':
        while True:
            print(submenu_clientes)
            opcion = input('    Seleccione una opción: ')

            if opcion == '1':
                listar_clientes()
            elif opcion == '2':
                razon_social = input('Razón social: ')
                cuit = input('CUIT: ')
                correo = input('Correo: ')
                agregar_cliente(razon_social, cuit, correo)
            elif opcion == '3':
                listar_clientes()
                id_cliente = input('ID del cliente a modificar: ')
                try:
                    id_cliente = int(id_cliente)
                    razon_social = input('Nueva razón social: ')
                    cuit = input('Nuevo CUIT: ')
                    correo = input('Nuevo correo: ')
                    modificar_cliente(id_cliente, razon_social, cuit, correo)
                except ValueError:
                    print("Error: ID debe ser un número.")
            elif opcion == '4':
                listar_clientes()
                id_cliente = input('ID del cliente a eliminar: ')
                try:
                    eliminar_cliente(int(id_cliente))
                except ValueError:
                    print("Error: ID debe ser un número.")
            elif opcion == '5':
                break
            else:
                print('Opción inválida.')

    elif opcion == '2':
        while True:
            print(submenu_destinos)
            opcion = input('    Seleccione una opción: ')

            if opcion == '1':
                listar_destinos()
            elif opcion == '2':
                ciudad = input('Ciudad: ')
                pais = input('País: ')
                costo_base = input('Costo base: ')
                try:
                    costo_base = float(costo_base)
                    agregar_destino(ciudad, pais, costo_base)
                except ValueError:
                    print("Error: Costo debe ser un número.")
            elif opcion == '3':
                listar_destinos()
                id_destino = input('ID del destino a modificar: ')
                try:
                    id_destino = int(id_destino)
                    ciudad = input('Nueva ciudad: ')
                    pais = input('Nuevo país: ')
                    costo_base = input('Nuevo costo base: ')
                    costo_base = float(costo_base)
                    modificar_destino(id_destino, ciudad, pais, costo_base)
                except ValueError:
                    print("Error: ID y costo deben ser números.")
            elif opcion == '4':
                listar_destinos()
                id_destino = input('ID del destino a eliminar: ')
                try:
                    eliminar_destino(int(id_destino))
                except ValueError:
                    print("Error: ID debe ser un número.")
            elif opcion == '5':
                break
            else:
                print('Opción inválida.')

    elif opcion == '3':
        listar_clientes()
        listar_destinos()
        id_cliente = input('ID del cliente: ')
        id_destino = input('ID del destino: ')
        costo = input('Costo de la venta: ')
        try:
            id_cliente = int(id_cliente)
            id_destino = int(id_destino)
            costo = float(costo)
            registrar_venta(id_cliente, id_destino, costo)
        except ValueError:
            print("Error: ID y costo deben ser números.")

    elif opcion == '4':
        while True:
            print(submenu_consultas)
            opcion = input('    Seleccione una opción: ')

            if opcion == '1':
                listar_todas_ventas()
            elif opcion == '2':
                ventas_mas_vendidas()
            elif opcion == '3':
                ventas_ultima_semana()
            elif opcion == '4':
                anio = input('Año (ej. 2025): ')
                try:
                    ventas_por_anio(int(anio))
                except ValueError:
                    print("Error: Año debe ser un número.")
            elif opcion == '5':
                listar_destinos()
                id_destino = input('ID del destino: ')
                try:
                    ventas_por_destino(int(id_destino))
                except ValueError:
                    print("Error: ID debe ser un número.")
            elif opcion == '6':
                break
            else:
                print('Opción inválida.')

    elif opcion == '5':
        listar_todas_ventas()
        id_venta = input('ID de la venta a anular: ')
        try:
            boton_arrepentimiento(int(id_venta))
        except ValueError:
            print("Error: ID debe ser un número.")

    elif opcion == '6':
        print("\nReporte General:")
        listar_clientes()
        listar_destinos()
        listar_todas_ventas()

    elif opcion == '7':
        print('Sistema creado por estudiantes de TSCDeIA 2025. v1.r0')

    elif opcion == '8':
        print('Gracias por utilizar SkyRoute. ¡Hasta pronto!')
        break
    else:
        print('Opción inválida.')

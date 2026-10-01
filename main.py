from soluciones.salarios_semanal import calcular_salario_semanal, mostrar_salario, leer_datos

def main():
    horas_trabajadas, pago_por_hora = leer_datos()
    salario_semanal = calcular_salario_semanal(horas_trabajadas, pago_por_hora)
    mostrar_salario(salario_semanal)

if __name__ == "__main__":
    main()
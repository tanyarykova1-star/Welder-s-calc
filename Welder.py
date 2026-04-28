import math

def start_calc():
    # Эта петля (while) заставляет программу работать бесконечно, пока мы не нажмем "нет"
    while True:
        print("\n" + "="*40)
        print("   СУПЕР-КАЛЬКУЛЯТОР СВАРЩИКА v8.0   ")
        print("="*40)
        print("1 - ТРУБА")
        print("2 - ЛИСТ (любая толщина)")
        print("0 - ВЫХОД")
        
        vibor = input("\nВыбери режим: ")
        
        if vibor == "0":
            print("Пока, папа! Удачи на сварке! 🛠️")
            break # Выход из программы

        # Сначала выбираем диаметр электрода, чтобы знать его вес
        print("\nДиаметр электрода УОНИ:")
        print("1. 2.5 мм (легкий)")
        print("2. 3.0 мм (средний)")
        print("3. 4.0 мм (тяжелый)")
        e_choice = input("Выбор: ")
        
        # Словарик весов (в кг)
        weights = {"1": 0.02, "2": 0.033, "3": 0.06}
        e_weight = weights.get(e_choice, 0.033) # Если нажмет не то, будет 3.0мм
        
        # Наш проверенный коэффициент потерь (огарки, брызги)
        k_loss = 2.1 

        if vibor == "1":
            d = float(input("Диаметр трубы (мм): "))
            t = float(input("Толщина стенки (мм): "))
            w_meter = 0.55 if t >= 5 else 0.35
            total_kg = (math.pi * d / 1000) * w_meter * k_loss
            
        elif vibor == "2":
            t = float(input("Толщина листа (мм): "))
            l_mm = float(input("Длина шва (мм): "))
            zazor = float(input("Зазор (мм): "))
            
            if t >= 8:
                # Наша победная формула для разделки кромок
                ploshad = (zazor * t) + (t**2 * 0.414)
                total_kg = (ploshad * l_mm * 0.00785 / 1000) * 1.7 * k_loss
            else:
                ploshad = zazor * t
                total_kg = (ploshad * l_mm * 0.00785 / 1000) * k_loss
        
        # Финальный расчет штук
        rezultat = math.ceil(total_kg / e_weight)

        print("\n" + "-"*35)
        print(f"ИТОГ: {rezultat} шт. (диаметр {e_choice if e_choice in '123' else '3.0'} мм)")
        print(f"Общий вес наплавки: {total_kg:.2f} кг")
        print("-"*35)
        
        # Спрашиваем, нужно ли продолжать
        cont = input("\nХочешь посчитать еще что-то? (да/нет): ").lower()
        if cont != "да":
            print("Хорошего дня! ✨")
            break

# Запуск
start_calc()
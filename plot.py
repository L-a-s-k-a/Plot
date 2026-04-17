import pandas as pd
import matplotlib.pyplot as plt

try:
    # zero_adc_value = pd.read_csv('data.csv')
    # if zero_adc_value.empty:
    #     raise ValueError("CSV файл пуст")
    # zero_adc_value = zero_adc_value.drop('Unnamed: 2', axis = 1)
    # print(zero_adc_value.head())
    
    # Предположим, что нужны первые два числовых столбца
    # x_col_1 = zero_adc_value.columns[0]
    # y_col_1 = zero_adc_value.columns[1]
    
    # Преобразуем столбцы x и y в числа, заменяя ошибки на NaN
    # x = zero_adc_value.apply(pd.to_numeric, errors='coerce')
    # print(x.head())

    # x_mean = x.mean()
    # print(x_mean)
    
    # plt.plot(zero_adc_value[x_col_1], zero_adc_value[y_col_1], 'o-')
    # plt.xlabel(x_col_1)
    # plt.ylabel(y_col_1)
    # plt.title(f'График {y_col_1} от {x_col_1}')
    # plt.grid(True)
    # plt.show()
    
    # motor_adc_value = pd.read_csv('adc_value.csv')
    # if motor_adc_value.empty:
    #     raise ValueError("CSV файл пуст")
    # motor_adc_value = motor_adc_value.drop('Unnamed: 2', axis = 1)
    # print(motor_adc_value.head())
    
    # x_col_2 = motor_adc_value.columns[0]
    # y_col_2 = motor_adc_value.columns[1]
    
    # plt.plot(motor_adc_value[x_col_2], motor_adc_value[y_col_2], 'o-')
    # plt.xlabel(x_col_2)
    # plt.ylabel(y_col_2)
    # plt.title(f'График {y_col_2} от {x_col_2}')
    # plt.grid(True)
    # plt.show()
    
    motor_voltage = pd.read_csv('voltage & filter_voltage.csv')
    if motor_voltage.empty:
        raise ValueError("CSV файл пуст")
    motor_voltage = motor_voltage.drop('Unnamed: 3', axis = 1)
    print(motor_voltage.head())
    dat_in_numeric = motor_voltage.apply(pd.to_numeric, errors='coerce')
    print((dat_in_numeric.mean()).head())
    
    x_col_3 = motor_voltage.columns[0]
    y1_col_3 = motor_voltage.columns[1]
    y2_col_3 = motor_voltage.columns[2]
    
    dat_in_numeric['current_from_non_filtered_voltage'] = (dat_in_numeric.iloc[:, 2] - 1.484) / 0.05 
    dat_in_numeric['current_from_filtered_voltage'] = (dat_in_numeric.iloc[:, 1] - 1.484) / 0.05 
    print(dat_in_numeric.head())
    
    # plt.plot(motor_voltage[x_col_3], motor_voltage[y1_col_3], label='y1_col_3', marker='o')
    # plt.plot(motor_voltage[x_col_3], motor_voltage[y2_col_3], label='y2_col_3', marker='o')
    # plt.xlabel(x_col_3)
    # plt.ylabel('Зависимые переменные')
    # plt.title(f'График {y1_col_3} от {x_col_3}')
    # plt.grid(True)
    # plt.show()
    
    # cur_x = dat_in_numeric[0]
    # cur_y = dat_in_numeric[3]

    plt.plot(dat_in_numeric.iloc[:, 0], dat_in_numeric.iloc[:, 3], 'o-')
    plt.plot(dat_in_numeric.iloc[:, 0], dat_in_numeric.iloc[:, 4], 'o-')
    plt.xlabel(x_col_3)
    plt.ylabel('current')
    plt.title(f'График Current от {x_col_3}')
    plt.grid(True)
    plt.show()
    
except FileNotFoundError:
    print("Файл не найден. Проверьте путь.")
except Exception as e:
    print(f"Ошибка: {e}")
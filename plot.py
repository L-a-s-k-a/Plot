import pandas as pd
import matplotlib.pyplot as plt

try:
    df = pd.read_csv('data.csv')
    if df.empty:
        raise ValueError("CSV файл пуст")
    
    df = df.drop('Unnamed: 2', axis = 1)
    print(df.head())
    # Предположим, что нужны первые два числовых столбца
    x_col = df.columns[0]
    y_col = df.columns[1]
    
    # Преобразуем столбцы x и y в числа, заменяя ошибки на NaN
    x = df.apply(pd.to_numeric, errors='coerce')
    # y = pd.to_numeric(df.columns[1])
    print(x.head())
    # print(y.head())

    # x_mean = x.mean()
    # print(x_mean)
    
    plt.plot(df[x_col], df[y_col], 'o-')
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'График {y_col} от {x_col}')
    plt.grid(True)
    plt.show()
    
except FileNotFoundError:
    print("Файл не найден. Проверьте путь.")
except Exception as e:
    print(f"Ошибка: {e}")
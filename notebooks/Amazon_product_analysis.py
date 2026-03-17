import pandas as pd
import psycopg2

# подключение к базе данных PostgreSQL. Вводим свой пароль и логин
conn = psycopg2.connect(
    dbname="your_dbname",
    user="username",
    password='password',
    host="your_host",
    port="your_port"
)

# читаем данные из таблицы в DataFrame (таблица в Python)
df = pd.read_sql("SELECT * FROM amazon_car_and_motobike;", conn)

# смотрим первые 5 строк, чтобы понять, как выглядят данные
print(df.head())

# Проверка пустых ячеек
print(df.isnull().sum())

# Проверка типов колонок
print(df.dtypes)

df.fillna(0, inplace=True)

print(df.isnull().sum())

# процент скидки
df['discount_percent'] = (df['actual_price'] - df['discount_price']) / df['actual_price'] * 100

# категория рейтинга
df['rating_category'] = pd.cut(df['ratings'], bins=[0,2,4,5], labels=['Low','Medium','High'])

df.to_excel("amazon_car_and_motorbike_clean.xlsx", index=False)

import matplotlib.pyplot as plt
import seaborn as sns

# Распределение рейтингов
sns.histplot(df['ratings'], bins=20)
plt.show()

# Средняя цена по категориям
sns.barplot(x='main_category', y='discount_price', data=df)
plt.show()

# Топ-10 товаров по количеству отзывов
top_products = df.sort_values('no_of_ratings', ascending=False).head(10)
sns.barplot(x='no_of_ratings', y='name', data=top_products)
plt.show()
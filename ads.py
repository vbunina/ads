import pandas as pd
import numpy as np
import seaborn as sns
import scipy.stats as ss

#загрузим данные, проверим число наблюдений и столбцов, типы данных, наличие пропущенных значений, какие уникальные значения встречаются
df_ads = pd.read_csv('https://stepik.org/media/attachments/lesson/384453/conversion.csv')
df_ads.shape
df_ads.dtypes
df_ads.isna().sum()
df_ads['xyz_campaign_id'].nunique()

#построим график распределения числа показов (Impressions – сколько раз пользователи увидели данное объявление) для каждой рекламной кампании в Facebook, прологарифмировав значения
df_impressions =df_ads.groupby('fb_campaign_id') \
.agg({'Impressions': 'sum'})
df_impressions_log = np.log(df_impressions['Impressions'])
sns.distplot(df_impressions_log, kde = False)

#посчитаем CTR, добавим в новый столбец и посмотрим описательную статистику записи с наибольшим CTR
df_ads['CTR'] = df_ads.Clicks / df_ads.Impressions
df_ads['CTR'].idxmax()
df_ads.iloc[150]

#посчитаем CPC, добавим в новый столбец, посчитаем межквартильный размах, округленный до двух знаков после точки
df_ads['CPC'] = df_ads.Spent / df_ads.Clicks
ss.iqr(CPC, nan_policy='omit').round(2)

#визуализируем CPC с разбивкой по полу пользователей, которым были показаны объявления
sns.distplot(df_ads.query("gender == 'M'").CPC.dropna(), bins=20, kde=False)
sns.distplot(df_ads.query("gender == 'F'").CPC.dropna(), bins=20, kde=False)

#посчитаем CR, добавим в новый столбец
df_ads['CR'] = df_ads.Approved_Conversion / df_ads.Clicks

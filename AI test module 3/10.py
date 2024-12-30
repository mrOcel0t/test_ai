import pandas as pd 

file_url = "titanic.csv"
titanic = pd.read_csv(file_url)

results = titanic.groupby('Embarked').Survived.agg(total='count',survived='sum')
results = results.to_dict()
for port in results['total']:
    survival_rate = round(results['survived'][port] / results['total'][port] * 100, 2)
    print(f'В порту{port} шанс выживания составляет {survival_rate}%')

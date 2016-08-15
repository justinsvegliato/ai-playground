import pandas as pd
import statsmodels.api as sm

df = pd.read_csv("http://www.ats.ucla.edu/stat/data/binary.csv")
df.columns = ["admit", "gre", "gpa", "prestige"]

categorical_prestige = pd.get_dummies(df['prestige'], prefix='prestige')
data = df[['admit', 'gre', 'gpa']].join(categorical_prestige.ix[:, 'prestige_2':])
data['intercept'] = 1.0

training_columns = data.columns[1:]
model = sm.Logit(data['admit'], data[training_columns])

result = model.fit()

print result.summary()
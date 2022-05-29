from data_proc import *
from model import make_model

data = read(os.path.join(os.curdir, 'dataset', 'train.csv'))
types = get_data_types(data=data)
match = getfl_match(types, ['Parch', 'Pclass', 'SibSp', 'Age'], ['Sex'])
encoded = encode_data(data, match)
ans = prep_ans(data)

model = make_model([32, 32], len(IN_COUNT))
model.fit(encoded, ans, 8, epochs=5)
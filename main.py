from csv import DictWriter
from data_proc import *
from model import make_model

data = read(os.path.join(os.curdir, 'dataset', 'train.csv'))
types = get_data_types(data=data)
match = getfl_match(types, ['Parch', 'Pclass', 'SibSp', 'Age'], ['Sex', 'Cabin'])
encoded = encode_data(data, match)
ans = prep_ans(data)

model = make_model([64, 64, 64], len(IN_COUNT), 0)
model.fit(encoded, ans, 4, epochs=3)


data = read(os.path.join(os.curdir, 'dataset', 'test.csv'))
types = get_data_types(data=data)
match = getfl_match(types, ['Parch', 'Pclass', 'SibSp', 'Age', 'Cabin'], ['Sex'])
encoded = encode_data(data, match)

with open(os.path.join(os.curdir, 'results', 'res.csv'), 'w', newline='') as output_file:
    f = DictWriter(output_file, ('PassengerId', 'Survived'))
    pred = model.predict(encoded)
    f.writeheader()
    for i, rec in enumerate(pred):
        if rec[0] >= 0.5:
            out = 1
        else:
            out = 0
        f.writerow({'PassengerId':str(i+892), 'Survived': str(out)})

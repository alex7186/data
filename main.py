from titanicpredictor import TitanicPredictor
obj = TitanicPredictor(fitmodel=False)
obj.load_model()

def tprint(s):
    print('->{}'.format(s))
    
print('Введите пол')
sex = str(input()).lower()
if ('же' in sex) or ('ба' in sex):
    sex = 1
else: 
    sex = 0
tprint('Введите возраст')
age = float(input())

tprint('Введите количество родственников')
rel = int(input())
    
ticket_prices = {
    'Первый класс' : 125852,
    'Второй класс' : 50370,
    'Третий класс' : 12556,
}

tprint('Введите стоимость вашего билета')
for key, val in ticket_prices.items():
    tprint('  билет', key, 'начинался от', val, 'р')

pclass = int(input(''))

if ticket_prices['Второй класс']-1000 <=  pclass < ticket_prices['Первый класс']:
    pclass = 2
elif pclass >= ticket_prices['Второй класс']:
    pclass = 1
else:
    pclass = 3

print(sex, age, rel, pclass)
res = obj.predict_res([sex, age, rel, pclass])


if int(res):
    print('выжил')
else:
    print('не выжил')
from flask import Flask, render_template, request, redirect, make_response
from settings.allautoparts import AllAutoPatrs

app = Flask(__name__)
finder = AllAutoPatrs()


@app.route('/')
def index():
    return render_template('find.html')


@app.route('/find', methods=['GET', 'POST'])
def find():
    table = ['артикул', 'наименование запчасти', 'фирма производитель']

    if request.method == 'POST':
        art = request.form.get('find')
    dict = finder.sersh_step1(art)
    context = {'art': dict, 'tables': table}
    # finder.guids = dict[0]
    return render_template('result.html', **context)
    # return f"{context}"

@app.post('/find_step2')
def find_step2():
    table = ['Артикл', 'Бренд','Наименование', 'Наличие', 'срок', 'Цена']
    id_web = request.form.get('id')
    res_find2 = finder.sersh_step2(id_web)
    context = {'tables': table, 'art': res_find2}
    return render_template('result1.html', **context, )

@app.post('/basket')
def basket():
    basket = request.form.get('id_basket')
    res_basket = finder.add_basket(basket)
    return f'{res_basket}'
    
  

if __name__ == "__main__":
    app.run(debug=True)
from flask import Flask, request, render_template, url_for
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


@app.route('/form')
def form():
    return render_template('form.html')


class Quotes(Resource):
    def get(self):
        author: str = (request.form.get('author'))
        quote: str = (request.form.get('quote'))
        return {
            'Elon Musk': {
                'quote': ['Fajnie byłoby umrzeć na Marsie, byle nie rozbić się przy podejściu dolądowania.']
            },
            'Steve Balmer': {
                'quote': ['Mam Maka i czas pracy na bateriach jest fatalny, Mac jest taaaki ciężki. '
                          'Jeśli chcesz długo pracować na komputerze – lepiej zrobić przesiadkę. '
                          'Jeśli chcesz netbooka – lepiej zrobić przesiadkę.'
                          'Jeśli chcesz korzystać z tych samych aplikacji, które ma Mac plus wielu innych –lepiej '
                          'zrobić przesiadkę. '
                          'MacBook Air jest lekki? Podnieście te komputery, które mamy tutaj, są dużo lżejsze!']
            },
            'Steve Jobs': {
                'quote': [
                    'Ci, którzy są wystarczająco szaleni, by myśleć, że są w stanie zmienić świat, są tymi, którzy go '
                    'zmieniają']
            },
            'Bill Gates': {
                'quote': [
                    'Obecnie ludzie od bezpieczeństwa włamują się do maców każdego dnia, wymyślają nowe exploity, '
                    'dzięki którym można całkowicie przejąć kontrolę nad maszyną. Niech ktoś spróbuje coś takiego '
                    'zrobić z Windowsem chociaż raz na miesiąc.']
            },
            author: {
                'quote': [
                    quote
                ]
            }
        }


#
class Quotes1(Resource):
    @app.route('/sand', methods=['GET', 'POST'])
    def post(self):
        author: str = (request.form.get('author'))
        quote: str = (request.form.get('quote'))
        return {
            author: {
                'quote': [
                    quote
                ]
            }
        }


api.add_resource(Quotes1, '/')
# @app.route('/send', methods=['GET', 'POST'])
# def post():
#     return api.add_resource(Quotes, '/')


# api.add_resource(Quotes, '/')

if __name__ == '__main__':
    app.run(debug=True)

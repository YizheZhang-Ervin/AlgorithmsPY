from flask import Blueprint, request, render_template, abort
from Algorithms.main import run

algorithm = Blueprint('algorithm', __name__)


def init_blue(app):
    app.register_blueprint(algorithm)


# index.html
@algorithm.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html', output='', history='', sourcecode='')
    if request.method == 'POST':
        try:
            hist = request.form.get('history')
            alg = request.form.get('alg')
            lis = eval(request.form.get('list'))
            try:
                ele = eval(request.form.get('element'))
            except Exception:
                ele = ''
            if alg != 'BinarySearch':
                output, time, code = run(alg=alg, mess_list=lis)
            else:
                output, time, code = run(alg=alg, ord_list=lis, elem=ele)
            return render_template('index.html', output=output,
                                   history=hist + '\n' + 'Output:'+str(output)+'--Time:'+str(round(time, 10)),
                                   sourcecode=code)
        except Exception:
            return render_template('index.html', output='sth wrong with server or your input',
                                   history='', sourcecode='')

# error handler
@algorithm.errorhandler(404)
def page_not_found(error):
    # use template
    return render_template('404.html'), 404
    # gain response and change
    # resp = make_response(render_template('404.html'), 404)
    # resp.headers['X-Something'] = 'A value'
    # return resp


@algorithm.route('/404')
def other():
    abort(404)

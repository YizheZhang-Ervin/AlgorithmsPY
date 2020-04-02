from flask import Flask
import os
import click
from BackEnd.settings import envs
from BackEnd.views import init_blue


# Init
def create_app(env):
    app = Flask(__name__, static_folder='./FrontEnd/static', template_folder='./FrontEnd/templates')
    # settings
    app.config.from_object(envs.get(env))

    # load extensions
    # init_exts(app)

    # initialize url
    init_blue(app)
    return app

# Run
# formal version of start cmd with parameters
@click.command()
# @click.option('--mode', default="develop", type=click.Choice(["develop", "produce"]), help="--develop/--produce")
@click.option('--host', default='127.0.0.1', type=str, help='x.x.x.x')
@click.option('--port', default='8080', type=str, help='1-65535')
@click.option('--debug', default=True, type=bool, help='True/False')
def run(host, port, debug):
    app.run(host=host, port=port, debug=debug)


# manage
env = os.environ.get('FLASK_ENV')
app = create_app(env)
# manager = Manager(app)
# manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    run()

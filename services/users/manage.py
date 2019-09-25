# services/users/manage.py

import unittest
from flask.cli import FlaskGroup

from project import app

cli = FlaskGroup(app)

@cli.command()

def test():
    """runs the tests without code coverage"""
    tests = unittest.TestLoader().discover('project/tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1



def recreate_db():
    db.drop_all()
    db.create_all()
    db.session_commit()

if __name__ == '__main__':
    cli()

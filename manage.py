#!/usr/bin/env python
import os
from app import create_app
from flask_script import Manager,Shell

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)

manager.add_command('shell', Shell)

if __name__ == '__main__':
    manager.run()

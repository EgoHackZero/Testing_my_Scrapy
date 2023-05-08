from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

from app import app, db


# Инициализация объектов приложения и менеджера миграций
migrate = Migrate(app, db)
manager = Manager(app)

# Добавление команды для миграций в менеджер
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()

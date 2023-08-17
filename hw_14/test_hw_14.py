# На семинаре 13 был создан проект по работе с пользователями (имя, id, уровень).
# Напишите 3-7 тестов pytest для данного проекта.
# Используйте фикстуры.

import pytest
import task_51

# Создание фикстуры для объекта Project с данными из JSON файла
@pytest.fixture(scope="module")
def project():
    return task_51.Project.from_json('users_personal_data.json')

# Создание фикстуры для объекта User с данными Админа
@pytest.fixture(scope="module")
def admin():
    return task_51.User("Niko", 84747, 1)

# Создание фикстуры для объекта User с данными обычного пользователя
@pytest.fixture(scope="module")
def user():
    return task_51.User("Maria", 2, 2)

# Тест на успешный вход в систему Админа
def test_login_admin(project, admin):
    project.login(admin.name, admin.id_)
    assert project.admin == admin

# Тест на неудачный вход в систему обычного пользователя
def test_login_user(project, user):
    with pytest.raises(task_51.AccessError):
        project.login(user.name, user.id_)

# Тест на успешное добавление пользователя Админом
def test_add_user(project, admin):
    project.login(admin.name, admin.id_)
    project.add_user("Ivan", 4, 2)
    assert task_51.User("Ivan", 4, 2) in project.users






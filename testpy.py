import pytest
import app
import os.path

def test_create_database(): # Тест на создание БД
    app.init_db()
    assert os.path.exists(app.db_name) == True

def test_clients(): # Тест на наличие столбцов в Clients
    assert app.Clients.name == True
    assert app.Clients.city == True
    assert app.Clients.address == True

def test_orders(): # Тест на наличие столбцов в Orders
    assert app.Orders.clients == True
    assert app.Orders.amount ==True
    assert app.Orders.date == True
    assert app.Orders.description == True

def test_sum_clients(): # Тест на наличие 10 строк в Clients
    app.fill_db()
    assert len(app.Clients.select()) > 9

def test_sum_orders(): # Тест на наличие 10 строк в Orders
    assert len(app.Orders.select()) > 9
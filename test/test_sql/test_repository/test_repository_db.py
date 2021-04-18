# from repository.db import Database

import json
import pytest

from service.service_sql.service import Service

from repository.repository_sql.models.items import Items

# Importamos Factory con el createObjectITem()
from repository.repository_sql.repo import Factory


@pytest.mark.db_test
def test_add_item_db(session):
    """Test if through session we can add an item

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """

    add_item = Items("Conjured Mana Cake", 5, 8)

    session.add(add_item)
    session.commit()

    assert add_item.name == "Conjured Mana Cake"
    assert add_item.sell_in == 5
    assert add_item.quality == 8


@pytest.mark.db_test
def test_get_items_db(session):
    """Test if through session we can get all items

    Args:
        session (SQLAlchemy Object Session): It's the session object from SQLALchemy Instance
    """

    add_item = Items("Conjured Mana Cake", 5, 8)

    session.add(add_item)
    session.commit()

    # Funciona, pero al parecer no carga los datos que ya están en la base de datos, por lo cual no tiene ninguno, lo que implica que tengo que agregar un nuevo objeto/row
    items_db = [item for item in session.query(Items).all()]

    assert len(items_db) == 1







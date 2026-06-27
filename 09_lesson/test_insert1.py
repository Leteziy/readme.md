from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:1821@localhost:5432/QA126.2"

db = create_engine(db_connection_string)


def test_insert_subject():
    db = create_engine(db_connection_string)
    sql = text("INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:new_subject_title, :new__id)")

    db.execute(sql, new_subject_title='Medecine', new__id=33)

    sql = text("SELECT subject_title FROM subject WHERE subject_id = :new_id")
    result = db.execute(sql, new_id=33)
    new_title = result.fetchone()[0]
    assert new_title == 'Medecine'
    sql_delete = text("DELETE FROM subject WHERE subject_id = :new_id")
    db.execute(sql_delete, new_id=33)

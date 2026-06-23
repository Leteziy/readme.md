from sqlalchemy import create_engine
from sqlalchemy.sql import text


db_connection_string = "postgresql://postgres:1821@localhost:5432/QA126.2"

db = create_engine(db_connection_string)


def test_delete_subject():
    db = create_engine(db_connection_string)
    sql = text("INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:new_subject_title, :new__id)")

    db.execute(sql, new_subject_title='Philosophy', new__id=55)

    sql = text("SELECT * FROM subject")
    rows_after_insert = db.execute(sql).fetchall()
    assert len(rows_after_insert) == 16

    sql_delete = text("DELETE FROM subject WHERE subject_id = :new_id")
    db.execute(sql_delete, new_id=55)

    sql = text("SELECT * FROM subject")
    rows_after_delete = db.execute(sql).fetchall()
    assert len(rows_after_delete) == 15

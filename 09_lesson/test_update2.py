from sqlalchemy import create_engine
from sqlalchemy.sql import text

db_connection_string = "postgresql://postgres:1821@localhost:5432/QA126.2"

db = create_engine(db_connection_string)


def test_update_subject():
    db = create_engine(db_connection_string)
    sql = text("INSERT INTO subject(\"subject_title\", \"subject_id\") VALUES (:new_subject_title, :new__id)")
    db.execute(sql, new_subject_title='Games', new__id=44)

    sql = text("UPDATE subject SET subject_title = :new_subject_title WHERE subject_id = :id")
    db.execute(sql, new_subject_title='Video games', id=44)

    sql = text("SELECT subject_title FROM subject WHERE subject_id = :new_id")
    result = db.execute(sql, new_id=44)
    new_title = result.fetchone()[0]
    assert new_title == 'Video games'

    sql_delete = text("DELETE FROM subject WHERE subject_id = :id")
    db.execute(sql_delete, id=44)

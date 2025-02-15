import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import crud, models, schemas, database

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@pytest.fixture(scope="module")
def db():
    models.Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    models.Base.metadata.drop_all(bind=engine)

def test_create_file(db):
    file_data = schemas.FileCreate(name="test.pdf", path="/test/test.pdf", type="pdf", size=1024)
    file = crud.create_file(db=db, file=file_data)
    assert file.name == "test.pdf"
    assert file.path == "/test/test.pdf"
    assert file.type == "pdf"
    assert file.size == 1024

def test_get_file(db):
    file_data = schemas.FileCreate(name="test.pdf", path="/test/test.pdf", type="pdf", size=1024)
    file = crud.create_file(db=db, file=file_data)
    fetched_file = crud.get_file(db=db, file_id=file.id)
    assert fetched_file.id == file.id
    assert fetched_file.name == "test.pdf"
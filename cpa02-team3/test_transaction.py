import pytest
from Transaction import Transaction, to_cat_dict_list

@pytest.fixture
def dbfile(tmpdir):
    ''' create a database file in a temporary file system '''
    return tmpdir.join('test_tracker.db')

@pytest.fixture
def empty_db(dbfile):
    ''' create an empty database '''
    db = Transaction(dbfile)
    yield db


@pytest.fixture
def small_db(empty_db):
    ''' create a small database, and tear it down later'''
    tran1 = {'amount': 15, 'category': 'fruit', 'date': '2000-08-25', 'desc':'apples'}
    tran2 = {'amount': 35, 'category': 'fruit', 'date': '2001-09-25', 'desc':'pears'}
    tran3 = {'amount': 105, 'category': 'fruit', 'date': '2000-08-25', 'desc':'bannana'}
    id1=empty_db.add(tran1)
    id2=empty_db.add(tran2)
    id3=empty_db.add(tran3)
    yield empty_db
    empty_db.delete(id3)
    empty_db.delete(id2)
    empty_db.delete(id1)

@pytest.fixture
def med_db(small_db):
    ''' create a database with 10 more elements than small_db'''
    rowids=[]
    # add 10 categories
    for i in range(10):
        s = str(i)
        d = '200'+s+'-0'+s+'-0'+s
        tran = {'amount': i, 'category': s, 'date': d, 'desc':s}
        rowid = small_db.add(tran)
        rowids.append(rowid)

    yield small_db

    # remove those 10 categories
    for j in range(10):
        small_db.delete(rowids[j])

# Eric
'''Testing select_cat method '''
@pytest.mark.select_cat
def test_select_cat(med_db):
    # Adding test category
    cat_test = {'amount': '',
                'category': 'Testing select_cat',
                'date': '',
                'desc': ''}
    
    # Category should be empty due to testing category
    rowid = Transaction.add(med_db,cat_test)

    # reading back all items from the category
    cat_return = med_db.select_cat(cat_test['category'])
    
    # Seeing if the correct category was added to
    assert len(cat_return) - 1 == 0
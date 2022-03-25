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
    # add 10 transactions
    for i in range(10):
        s = str(i)
        d = '200'+s+'-0'+s+'-0'+s
        tran = {'amount': i, 'category': s, 'date': d, 'desc':s}
        rowid = small_db.add(tran)
        rowids.append(rowid)

    yield small_db

    # remove those 10 transactions
    for j in range(10):
        small_db.delete(rowids[j])

@pytest.mark.simple
def test_to_cat_dict():
    ''' teting the to_cat_dict function '''
    a = to_cat_dict_list(((20,15,'fruit' '2000-08-25', 'apples'),(25,16,'fruits' '2000-08-24', 'appl')))
    assert a[0]['item_num']==20
    assert a[1]['item_num']==25
    assert a[1]['amount']==16
    assert a[0]['date']=='2000-08-25'
    assert a[0]['desc']=='apples'
    assert len(a[0].keys())==5


@pytest.mark.add
def test_add(med_db):
    ''' add a category to db, the select it, then delete it'''

    cat0 = {'amount': 30, 'category': 'beans', 'date': '2000-08-09', 'desc':'beaaaans'}
    cats0 = med_db.select_all()
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()
    assert len(cats1) == len(cats0) + 1
    cat1 = med_db.select_one(rowid)
    assert cat1['amount']==cat0['amount']
    assert cat1['category']==cat0['category']
    assert cat1['date']==cat0['date']
    assert cat1['desc']==cat0['desc']



@pytest.mark.delete
def test_delete(med_db):
    ''' add a category to db, delete it, and see that the size changes'''
    # first we get the initial table
    cats0 = med_db.select_all()

    # then we add this transaction to the table and get the new list of rows
    cat0 = {'amount': 30, 'category': 'beans', 'date': '2000-08-09', 'desc':'beaaaans'}
    rowid = med_db.add(cat0)
    cats1 = med_db.select_all()

    # now we delete the transaction and again get the new list of rows
    med_db.delete(rowid)
    cats2 = med_db.select_all()

    assert len(cats0)==len(cats2)
    assert len(cats2) == len(cats1)-1

@pytest.mark.update
def test_update(med_db):
    ''' add a category to db, updates it, and see that it changes'''

    # then we add this transaction to the table and get the new list of rows
    cat0 = {'name':'testing_add',
            'desc':'see if it works',
            }
    rowid = med_db.add(cat0)

    # now we upate the transactions
    cat1 = {'name':'new cat','desc':'new desc'}
    med_db.update(rowid,cat1)

    # now we retrieve the transaction and check that it has changed
    cat2 = med_db.select_one(rowid)
    assert cat2['name']==cat1['name']
    assert cat2['desc']==cat1['desc']

# Eric
'''Testing select_cat method '''
@pytest.mark.select_cat
def test_select_cat(med_db):
    # Adding test category
    cat_test = {'amount': '',
                'category': 'Testing select_cat',
                'date': '',
                'desc': ''}
    
    # transactions should be empty due to testing category
    rowid = Transaction.add(med_db,cat_test)

    # reading back all items from the category
    cat_return = med_db.select_cat(cat_test['category'])
    
    # Seeing if the correct category was added to
    assert len(cat_return) - 1 == 0

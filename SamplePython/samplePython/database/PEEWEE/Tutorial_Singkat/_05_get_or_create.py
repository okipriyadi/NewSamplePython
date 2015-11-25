#!/usr/bin/env python

"""
Sometimes we need to use a model in peewee that we want to get from DB or create if it doesn't exist.
We have get_or_create and create_or_get for that.
But what if it don't really want the instance of the model? We simply want to create it (for logging purposes maybe)?
Is there a faster method than these two, assuming we will be inserting a lot of duplicate records?
I usually simply do:
 try:
     Model.create(...)
 except:
     pass
but is it the fastest?

This script tests a few possibilities and the results are:
fopina@TEST:~/tmp$ pip install peewee psycopg2
fopina@TEST:~/tmp$ for i in $(seq 5); do echo Test $i; ./peewee_pgsql_test.py postgres://test:test@172.16.118.128/test; done

Test 1
try_insert : 2.62834000587
get_or_create : 2.59686303139
get_or_create2 : 2.47503304482
get_or_create3 : 2.23236203194
get_or_create4 : 2.80767011642
create_or_get : 6.0398709774

Test 2
try_insert : 2.63586997986
get_or_create : 2.61891508102
get_or_create2 : 2.49721193314
get_or_create3 : 2.11195588112
get_or_create4 : 2.24556899071
create_or_get : 5.74026894569

Test 3
try_insert : 2.7051820755
get_or_create : 2.58048796654
get_or_create2 : 2.46140909195
get_or_create3 : 2.07919001579
get_or_create4 : 2.18738508224
create_or_get : 5.48429989815

Test 4
try_insert : 2.58274102211
get_or_create : 2.60744810104
get_or_create2 : 2.47490596771
get_or_create3 : 2.09399795532
get_or_create4 : 2.2156419754
create_or_get : 5.53600502014
Test 5
try_insert : 2.5695078373
get_or_create : 3.04075193405
get_or_create2 : 3.71266698837
get_or_create3 : 3.15286421776
get_or_create4 : 3.40215706825
create_or_get : 11.1691100597

So it seems doing a select only by the primary key and inserting if it fails is the fastest,
but very slightly compared to try_insert or get_or_create, with get_or_create having the advantage
of actually retrieving the instance in case you do need to use it in the future :)
"""
from peewee import (
    Proxy, Model, CharField, IntegerField,
)
from playhouse.db_url import connect
import sys
import timeit


database_proxy = Proxy()


class TestModel(Model):
    id = IntegerField(primary_key=True)
    field1 = CharField()
    field2 = CharField()
    field3 = CharField()

    class Meta:
        database = database_proxy


def create_tables(db):
    db.create_tables([TestModel])


def try_insert():
    try:
        TestModel.create(
            id=1,
            field1='A',
            field2='B',
            field3='C',
        )
    except:
        pass


def get_or_create():
    """
    First iteration should be slower than try_insert (fail a .get and then insert versus just insert)
    All other iterations will depend on times from successful get() versus unsuccessful insert()...
    """

    TestModel.get_or_create(
        id=1,
        defaults={
            'field1': 'A',
            'field2': 'B',
            'field3': 'C',
        }
    )


def get_or_create2():
    """
    get_or_create should do this basically, same times expected
    """

    try:
        TestModel.get(
            TestModel.id == 1,
        )
    except TestModel.DoesNotExist:
        TestModel.create(
            id=1,
            field1='A',
            field2='B',
            field3='C',
        )


def get_or_create3():
    """
    what if we do a get() only for the id?
    does it reduce the times significantly?
    """

    try:
        TestModel.select(TestModel.id).where(TestModel.id == 1)[0]
    except IndexError:
        TestModel.create(
            id=1,
            field1='A',
            field2='B',
            field3='C',
        )


def get_or_create4():
    """
    same as get_or_create3, but using a less pythonic strategy: check before create instead of create and apologize
    """

    if TestModel.select(TestModel.id).where(TestModel.id == 1).count() == 0:
        TestModel.create(
            id=1,
            field1='A',
            field2='B',
            field3='C',
        )


def create_or_get():
    """
    As this is a test for performance when we simply want to insert
    create_or_get does not make sense, as it will be the same as
    try_insert() test PLUS a get()!
    Including it to compare performance versus get_or_create
    """

    TestModel.create_or_get(
        id=1,
        field1='A',
        field2='B',
        field3='C',
    )


def testit(number):
    tests = [
        try_insert,
        get_or_create,
        get_or_create2,
        get_or_create3,
        get_or_create4,
        create_or_get,
    ]

    for test in tests:
        TestModel.delete().execute()
        print test.func_name, ':', timeit.timeit(test, number=number)


def main():
    # DB_URL = 'postgres://user:password@HOST:PORT/DB'
    if len(sys.argv) < 2:
        print 'Usage: %s DB_URL' % sys.argv[0]
        sys.exit(-1)

    db = connect(sys.argv[1])
    db.autorollback = True
    database_proxy.initialize(db)
    try:
        create_tables(db)
    except:
        pass
    testit(5000)


if __name__ == '__main__':
    main()



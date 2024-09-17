import pytest
from sqlite_lib import connect, close, run_query_select
from sqlite_lib import members_count

# Fixture to connect to the database before each test and close it after
@pytest.fixture
def db_connection():
    connect('ecomm.db')
    yield
    close()  

# Test for "Bronze" membership
def test_bronze_members(db_connection):
    expected_query = 'SELECT COUNT(*) FROM ecomm WHERE "Membership Type" = "Bronze";'
    expected = run_query_select(expected_query)[0][0]

    assert members_count("Bronze") == expected

def test_silver_members(db_connection):
    expected_query = 'SELECT COUNT(*) FROM ecomm WHERE "Membership Type" = "Silver";'
    expected = run_query_select(expected_query)[0][0]

    assert members_count("Silver") == expected

def test_gold_members(db_connection):
    expected_query = 'SELECT COUNT(*) FROM ecomm WHERE "Membership Type" = "Gold";'
    expected = run_query_select(expected_query)[0][0]

    assert members_count("Gold") == expected

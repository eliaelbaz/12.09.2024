import pytest
from sqlite_lib import connect, close, run_query_select
from sqlite_lib import members_count  # ייבוא הפונקציה

# Fixture to connect to the database before each test and close it after
@pytest.fixture
def db_connection():
    connect('ecomm.db')  # התחברות למסד הנתונים
    yield
    close()  # ניתוק ממסד הנתונים אחרי הטסט

# Test for "Bronze" membership
def test_bronze_members(db_connection):
    # חישוב הציפייה (expected) באמצעות שאילתת SQL
    expected_query = 'SELECT COUNT(*) FROM ecomm WHERE "Membership Type" = "Bronze";'
    expected = run_query_select(expected_query)[0][0]

    # בדיקת הפונקציה members_count לקטגוריית Bronze
    assert members_count("Bronze") == expected

# Test for "Silver" membership
def test_silver_members(db_connection):
    expected_query = 'SELECT COUNT(*) FROM ecomm WHERE "Membership Type" = "Silver";'
    expected = run_query_select(expected_query)[0][0]

    assert members_count("Silver") == expected

# Test for "Gold" membership
def test_gold_members(db_connection):
    expected_query = 'SELECT COUNT(*) FROM ecomm WHERE "Membership Type" = "Gold";'
    expected = run_query_select(expected_query)[0][0]

    assert members_count("Gold") == expected

"""
ETL-Query script
"""

from mylib.extract import extract
from mylib.transform_load import load
from mylib.query import run_crud_operations

# Extract
print("Extracting data...")
extract()

# Transform and load
print("Transforming data...")
load()

# Query
print("Querying data...")
run_crud_operations()

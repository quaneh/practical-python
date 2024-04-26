# fileparse.py
#
# Exercise 3.3
import csv

def parse_csv(file, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    rows = csv.reader(file, delimiter=delimiter)
    # Read the file headers (if any)
    headers = next(rows) if has_headers else []  
    records = []
    
    if select:
        if not has_headers:
            raise RuntimeError('select argument requires column headers')
        indices = [ headers.index(column) for column in select ]
        headers = select

    for n, row in enumerate(rows, start=1):
        # Handle missing rows
        if not row:
            continue
        # Handle column selection
        if select:
            row = [row[index] for index in indices]
            
        # Handle typecasting
        if types:
            try:
                row = [func(val) for func, val in zip(types, row)]
            except ValueError as e:
                if not silence_errors:
                    print(f'Row {n}: Couldnt convert {row}')
                    print(f'Row {n}: Reason {e}')
                continue
        if headers:    
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)

    return records
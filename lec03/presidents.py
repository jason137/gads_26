#!/usr/bin/env python

# problem 9
# Use the files presidents.tsv and pres_parties.tsv to find total time in office
# by party (hint: you may find the builtin Python datetime library useful).

import pandas as pd
from datetime import datetime as dt

PRES_FILE = '~/gits/gads_26/datasets/presidents.tsv'
PARTIES_FILE = '~/gits/gads_26/datasets/pres_parties.tsv'

PRES_NAMES =  ['name', 'dob', 'term_start', 'term_end', 'dod']
PARTY_NAMES = ['name', 'party']

DATE_FORMAT = '%B %d, %Y'

def convert_date(date_str):

    try:
        return dt.strptime(date_str, DATE_FORMAT).date()
    except TypeError:
        return dt.today().date()

def main():

    # load & join datasets
    pres_df = pd.read_csv(PRES_FILE, sep='\t', names=PRES_NAMES, header=0)
    party_df = pd.read_csv(PARTIES_FILE, sep='\t', names=PARTY_NAMES, header=0)
    party_df['name'] = pres_df.name     # slight cheat: make join key consistent
    df = pres_df.merge(party_df, how='outer')

    # calculate term lengths for each president
    df['term_start_dt'] = df.term_start.apply(convert_date)
    df['term_end_dt'] = df.term_end.apply(convert_date)
    df['term_length'] = df.term_end_dt - df.term_start_dt

    # perform grouping
    grouped_df = df.groupby('party').term_length.sum()
    print(grouped_df)

if __name__ == '__main__':
    pd.set_option('display.width', None)
    main()

# check this link out for datetime details
# https://docs.python.org/3.5/library/datetime.html#strftime-strptime-behavior

# NOTE removed index column from presidents.tsv!
# NOTE can convert days to years
# YEAR = datetime.timedelta(days=365.25) --> divide days / YEAR

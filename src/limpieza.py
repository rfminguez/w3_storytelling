import re
import pandas as pd

def drop_nan_by_field(df, field):
    '''
    receives: a pandas dataframe and a field to check for null values.
    returns: a dataframe without the rows that contain a null value in the field.
    '''
    return df.dropna(subset=[field])


def divide_csv_field(df, field):
    '''
    receives: a dataframe and the name of a field with multiple values separated with commas.
    returns: a dataframe with each individual value inside the field separated in a row.
    '''
    return df.set_index(df.columns.drop(field,1).tolist())[field].str.split(',', expand=True).stack().reset_index().rename(columns={0:field})


def normalize_us_data(df):
    '''
    notice: it is a function created ad-hoc for this dataset.
    receives: a dataframe.
    returns: a dataframe with the data in the column Country that references to the EEUU normalized.
    '''
    return df['Country'].apply(lambda c: "United States" if c.startswith("US:") else c)


def df_select_columns(df, *columns):
    '''
    receives: a dataframe and a set of columns.
    returns: a dataframe that contains only those columns.
    '''
    return df[list(columns)]


def remove_whitespaces(df, field):
    '''
    receives: a dataframe and the name of a field.
    returns: a daraframe with the spaces removed to the left and right of this field in all rows of the dataframe.
    '''
    return df[field].apply(lambda s: s.strip())


def normalize_keyword_field(keyword):
    '''
    notice: this function was created ad-hoc for the data in this dataframe.
    receives: a keyword.
    returns: a normalized keyword if it matches any of the regular expressions in the conditions or the keyword if it does not.
    '''

    if re.match(r"(stimulus|financial|economic)", keyword):
        return "economic stimulus"
    if re.match(r"international traveller screening.*", keyword):
        return "international traveller screening"
    if keyword in ['traveller testing', 'test travellers']:
        return "international traveller screening"
    if re.match(r"international traveller quarantine.*", keyword):
        return "international traveller quarantine"
    if re.match(r"(international|outbound) travel[^\s]* ban.*", keyword):
        return "international travel ban"
    if re.match(r"(nursery )?(school|university) closure.*", keyword):
        return "school or university closure"
    if keyword in ["public announcement", "blanket announcement", "general advice", "blanket text messaging", "information sms", "coronavirus education activities", "activism for stricter measures", "health declaration system"]:
        return "public announcement"
    if re.match(r"remote medical treatment.*", keyword):
        return "remote medical treatment"
    if re.match(r"^.*remote work.*", keyword):
        return "remote work"
    if re.match(r"^.*remote schooling.*", keyword):
        return "remote schooling"
    if re.match(r"religious activity.*", keyword):
        return "religious activity limitation"
    if re.match(r"social distancing.*", keyword):
        return "social distancing"
    if re.match(r".*nonessential.*", keyword):
        return "nonessential business suspension"

    return keyword

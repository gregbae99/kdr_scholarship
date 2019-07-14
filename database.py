import sys
import pandas as pd
import numpy as np


class Database(object):
    def __init__(self, csv=None):
        self.static = {
            'What is your name?': 'Name',
            'What year are you in?': 'Year',
            'What is your major?': 'Major',
            'If applicable - what is your 2nd major?': 'Major 2',
            'If applicable - what is your 3rd major?': 'Major 3',
            'What is your minor? ': 'Minor',
            'What classes are you taking this semester?': 'Current Classes',
            'Most important class taken': 'Past Class 1',
            'Grade received for most important class': 'Grade Class 1',
            '2nd Most important class taken': 'Past Class 2',
            'Grade received for 2nd most important class': 'Grade Class 2',
            '3rd Most important class taken': 'Past Class 3',
            'Grade received for 3rd most important class': 'Grade Class 3',
            '4th Most important class taken ': 'Past Class 4',
            'Grade received for 4th most important class': 'Grade Class 4',
            '5th Most important class taken': 'Past Class 5',
            'Grade received for 5th most important class': 'Grade Class 5',
        }

        self.df = pd.read_csv(csv, na_filter=False).rename(self.static, axis='columns')
        self.df['Class #1'] = self.df['Class #1'].str.upper()
        self.df['Class #2'] = self.df['Class #2'].str.upper()
        self.df['Class #3'] = self.df['Class #3'].str.upper()
        self.df['Class #4'] = self.df['Class #4'].str.upper()
        self.df['Class #5'] = self.df['Class #5'].str.upper()
        self.df['Class #6'] = self.df['Class #6'].str.upper()
        self.df['Class #7'] = self.df['Class #7'].str.upper()
        self.df['Past Class 1'] = self.df['Past Class 1'].str.upper()
        self.df['Past Class 2'] = self.df['Past Class 2'].str.upper()
        self.df['Past Class 3'] = self.df['Past Class 3'].str.upper()
        self.df['Past Class 4'] = self.df['Past Class 4'].str.upper()
        self.df['Past Class 5'] = self.df['Past Class 5'].str.upper()

    def brother_info(self):
        """

        :return: Name as Index and Year, Major, Major 2, Major 3, Minor as columns
        """
        return self.df[['Name', 'Year', 'Major', 'Major 2', 'Major 3', 'Minor']].set_index('Name').sort_index()

    def major_name(self):
        """
            Idea is to return Major (including Major 2, Major 3) as Index and list of names as Value
        :return: pd Dataframe
        """
        uq_majors = [e for e in pd.unique(self.df[['Major', 'Major 2', 'Major 3']].values.ravel('K')).tolist()
                     if e not in ('None', '')]
        major = {k: [] for k in uq_majors}
        for uq_major in uq_majors:
            major[uq_major].extend(self.df.loc[self.df['Major'] == uq_major, ['Name']].values.flatten().tolist())
            major[uq_major].extend(self.df.loc[self.df['Major 2'] == uq_major, ['Name']].values.flatten().tolist())
            major[uq_major].extend(self.df.loc[self.df['Major 3'] == uq_major, ['Name']].values.flatten().tolist())

        return pd.DataFrame.from_dict(major, orient='index').sort_index()

    def past_classes(self):
        """
            Idea is to return Past classes (all 5 past classes) as Index, and list of names as value sorted by higher grades received
        :return: pd Series
        """
        pass

    def current_classes(self):
        """

        :return: a pd Series with classes as index and a string of names concatenated with ', ' as value
        """
        uq_classes = [c for c in pd.unique(self.df[['Class #1', 'Class #2', 'Class #3', 'Class #4', 'Class #5',
                                                    'Class #6', 'Class #7']].values.ravel('K')).tolist()
                      if c not in ('None', '')]
        classes = {k: [] for k in uq_classes}
        for uq_class in uq_classes:
            classes[uq_class].extend(self.df.loc[self.df['Class #1'] == uq_class, ['Name']].values.flatten().tolist())
            classes[uq_class].extend(self.df.loc[self.df['Class #2'] == uq_class, ['Name']].values.flatten().tolist())
            classes[uq_class].extend(self.df.loc[self.df['Class #3'] == uq_class, ['Name']].values.flatten().tolist())
            classes[uq_class].extend(self.df.loc[self.df['Class #4'] == uq_class, ['Name']].values.flatten().tolist())
            classes[uq_class].extend(self.df.loc[self.df['Class #5'] == uq_class, ['Name']].values.flatten().tolist())
            classes[uq_class].extend(self.df.loc[self.df['Class #6'] == uq_class, ['Name']].values.flatten().tolist())
            classes[uq_class].extend(self.df.loc[self.df['Class #7'] == uq_class, ['Name']].values.flatten().tolist())
        return pd.DataFrame.from_dict(classes, orient='index').sort_index()


def main():
    csv = 'KDR Scholarship Fall 2019.csv' or sys.argv[0]
    db = Database(csv)
    print(db.brother_info())
    print('--------------------------------')
    print(db.current_classes())
    print('--------------------------------')
    print(db.major_name())
    print('--------------------------------')


if __name__ == '__main__':
    main()

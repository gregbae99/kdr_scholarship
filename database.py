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
        self.df = pd.read_csv(csv).replace(np.nan, '', regex=True).rename(self.static, axis='columns')
        self.df['Current Classes'] = self.df['Current Classes'].str.upper()
        self.df['Past Class 1'] = self.df['Past Class 1'].str.upper()
        self.df['Past Class 2'] = self.df['Past Class 2'].str.upper()
        self.df['Past Class 3'] = self.df['Past Class 3'].str.upper()
        self.df['Past Class 4'] = self.df['Past Class 4'].str.upper()
        self.df['Past Class 5'] = self.df['Past Class 5'].str.upper()

    def brother_info(self):
        """

        :return: Name as Index and Year, Major, Major 2, Major 3, Minor as columns
        """
        return self.df[['Name', 'Year', 'Major', 'Major 2', 'Major 3', 'Minor']].set_index('Name')

    def major_name(self):
        """
            Idea is to return Major (including Major 2, Major 3) as Index and list of names as Value
        :return: pd Series
        """
        pass

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
        current = {}
        class_df = self.df[['Name', 'Current Classes']].set_index('Name').to_dict()
        for key, value in class_df.items():
            for name, classes in value.items():
                for e_class in classes.split(','):
                    if e_class not in current:
                        current[e_class] = [name]
                    else:
                        current[e_class].append(name)

        for key, value in current.items():
            current[key] = ', '.join(value)
        return pd.Series(current)


def main():
    csv = sys.argv[0] or 'KDR Scholarship Fall 2019.csv'
    db = Database(csv)
    print(db.brother_info())
    print('--------------------------------')
    print(db.current_classes())
    print('--------------------------------')



if __name__ == '__main__':
    main()

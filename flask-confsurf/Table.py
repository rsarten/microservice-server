import numpy as np
import pandas as pd

class Table(object):
    def __init__(self, vars=['Sex']):
        full_surf = pd.read_csv("data/census-2006-surf.csv")
        self.all_variables = list(full_surf)

        self.variables = ['meshblock']
        for var in vars:
            self.variables.append(var)

        self.surf = full_surf[self.variables]
        self.groupByMeshblock()


    def groupByMeshblock(self):
        self.surf = pd.DataFrame({'count': self.surf.groupby(self.variables).size()})\
            .unstack(fill_value=0).\
            stack().\
            reset_index()


    def addTotalsRows(self):
        mb_totals = self.surf.groupby(['meshblock']).sum().reset_index()
        sub_totals = {'meshblock': mb_totals['meshblock'], 'count': mb_totals['count']}
        for variable in self.variables[1:]:
            sub_totals[variable] = 'Total'

        sub_totals_df = pd.DataFrame(sub_totals)
        surf = pd.concat([self.surf, sub_totals_df])
        variables = self.variables.append('count')
        self.surf = surf[variables].sort_values(self.variables)


    def confidentialise(self):
        if not self.checkPassRule1():
            self.surf.loc[self.surf['count'] < 6, 'count'] = -1
        elif not self.checkPassRule2():
            number_of_cells = len(self.variables[1:-1])
            self.surf.loc[self.surf['count']/number_of_cells <= 2, 'count'] = -1

        self.surf.loc[self.surf['count'] >= 0, 'count'] = self.surf['count'].apply(self.randomRound)
        self.surf['count'] = self.surf['count'].apply(str)
        self.surf.loc[self.surf['count'] == '-1', 'count'] = "..C"


    def checkPassRule1(self):
        if len(self.variables[1:]) > 1:
            return False
        return True


    def checkPassRule2(self):
        number_of_cells = len(self.variables[1:-1])
        means = pd.DataFrame({'means': self.surf['count']/number_of_cells})
        return (means['means'] > 2).all()


    def randomRound(self, count):
        rand_base = np.random.randint(1 ,4)
        rounded_count = int(3 * round(float(count) / 3))
        if rand_base < 3:
            return rounded_count
        else:
            return rounded_count+3 if count-rounded_count > 0 else rounded_count-3


    def getSURF(self):
        return self.surf


    def getSURFAsDict(self):
        return self.surf.to_dict('records')


    def getMetadata(self):
        return self.all_variables

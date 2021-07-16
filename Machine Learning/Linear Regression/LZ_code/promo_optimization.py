import numpy as np
from fbprophet import Prophet
import itertools
import pandas as pd


class OptimizePromotions:
    def optimize_promos(self, n, freq, week=False, year=False, daily=False):
        self.forecast(n, freq, week=week, year=year, daily=daily)

        if len(self.reg.seasonal_features) > 0 and len(self.reg.product_features) > 0:
            self.init_seasonal_inputs()
            self.init_product_inputs(lp=25)
            base_inputs = pd.concat(
                [self.seasonal_dataset, self.product_dataset], axis=1)
        elif len(self.reg.seasonal_features) == 0 and len(self.reg.product_features) > 0:
            self.init_product_inputs(lp=25)
            base_inputs = pd.concat([self.product_dataset], axis=1)
        elif len(self.reg.seasonal_features) > 0 and len(self.reg.product_features) == 0:
            self.init_seasonal_inputs()
            base_inputs = pd.concat([self.seasonal_dataset], axis=1)
        else:
            base_inputs = pd.DataFrame([])
        all_promo_dict = dict.fromkeys(self.reg.promotional_features, 0)
        available_promos = [item for item in list(self.promos)]
        range_of_promo_values = []
        for promo in available_promos:
            if promo.mechanic == 'Boolean':
                range_of_promo_values.append([0, 1])
            elif promo.mechanic == 'Percentage':
                range_of_promo_values.append([0, promo.value])
            elif promo.mechanic == 'Variable':
                range_of_promo_values.append([0, promo.value])
            else:
                print('Mechanic not specified')

        combinations = list(itertools.product(*range_of_promo_values))
        best_inputs = pd.DataFrame(
            [], columns=self.reg.features+self.reg.target)
        for date in self.forecast_data['ds'][-self.m.n:].apply(lambda x: x.to_pydatetime()):
            max_sales = 0
            for comb in combinations:
                i = 0
                for promo in available_promos:
                    all_promo_dict[promo.name] = comb[i]
                    i = i+1

                promo_input = pd.DataFrame(
                    pd.DataFrame(all_promo_dict, index=[date]))
                if len(base_inputs) != 0:
                    base_input = pd.DataFrame(base_inputs.loc[date]).T
                    inputs = pd.concat([base_input, promo_input], axis=1)
                else:
                    inputs = promo_input
                sales = self.reg.predict(np.array(inputs))
                if sales > max_sales:
                    max_sales = sales
                    max_inputs = inputs
            max_inputs[self.reg.target] = max_sales
            best_inputs = pd.concat([best_inputs, max_inputs])
        self.best_inputs = best_inputs
        return self.best_inputs

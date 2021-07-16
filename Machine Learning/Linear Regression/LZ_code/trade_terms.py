import pandas as pd


class TradeKPIS:
    def __init__(self):
        self.list_price = 13.82
        self.case_rate_allowance = 0
        self.scan_rate_unit = 2.40
        self.cogs = 6.831
        self.lump_sum = 0
        self.everyday_price = 16.04

    def calculate_manufacturer(self, forecasted_volume, projected_cons, weekly_base, n_weeks, feature_price):
        revenue = self.list_price * forecasted_volume
        volume = forecasted_volume
        incr_volume = projected_cons - (weekly_base*n_weeks)
        incr_revenue = incr_volume*self.list_price
        total_trade_spend = (self.case_rate_allowance*forecasted_volume) + \
            (self.scan_rate_unit*projected_cons)+self.lump_sum
        net_revenue = revenue - total_trade_spend
        trade_spend_per_case = total_trade_spend/forecasted_volume
        spend_per_inc_uom = total_trade_spend/incr_volume
        trade_spend_percent = (total_trade_spend/revenue)*100
        total_profit = revenue - total_trade_spend - \
            (self.cogs*forecasted_volume)
        profit_per_case = total_profit/forecasted_volume
        profit_margin_percent = (total_profit/revenue)*100
        profit_margin_wfb = "N/A"
        incr_profit = incr_revenue - \
            total_trade_spend - (self.cogs*incr_volume)
        profit_per_incr_case = incr_profit/incr_volume
        roi = (incr_profit/total_trade_spend)*100
        required = {'revenue': revenue, 'volume': volume, 'incr_volume': incr_volume, 'incr_revenue': incr_revenue, 'total_trade_spend': total_trade_spend, 'net_revenue': net_revenue, 'trade_spend_per_case': trade_spend_per_case,
                    'spend_per_inc_uom': spend_per_inc_uom, 'trade_spend_percent': trade_spend_percent, 'total_profit': total_profit, 'profit_per_case': profit_per_case, 'profit_margin_percent': profit_margin_percent, 'profit_margin_wfb': profit_margin_wfb, 'incr_profit': incr_profit, 'profit_per_incr_case': profit_per_incr_case, 'roi': roi}
        df = pd.DataFrame.from_dict(required, orient='index')
        # print(df)
        return df

    def calculate_retailer(self, forecasted_volume, projected_cons, weekly_base, n_weeks, feature_price):
        forward_buy = forecasted_volume-projected_cons
        revenue = (projected_cons*feature_price) + \
            (forward_buy*self.everyday_price)
        volume = forecasted_volume
        incr_volume = projected_cons - (weekly_base*n_weeks)
        incr_revenue = projected_cons*feature_price - \
            (weekly_base*self.everyday_price)
        total_trade_spend = (self.case_rate_allowance*forecasted_volume) + \
            (self.scan_rate_unit*projected_cons)+self.lump_sum
        net_revenue = revenue - total_trade_spend
        trade_spend_per_case = total_trade_spend/forecasted_volume
        spend_per_inc_uom = total_trade_spend/incr_volume
        trade_spend_percent = (total_trade_spend/revenue)*100
        total_profit = revenue - total_trade_spend - \
            (self.cogs*forecasted_volume)
        profit_per_case = total_profit/forecasted_volume
        profit_margin_percent = (total_profit/revenue)*100
        profit_margin_wfb = "N/A"
        incr_profit = incr_revenue - \
            total_trade_spend - (self.cogs*incr_volume)
        profit_per_incr_case = incr_profit/incr_volume
        roi = (incr_profit/total_trade_spend)*100
        required = {'revenue': revenue, 'volume': volume, 'incr_volume': incr_volume, 'incr_revenue': incr_revenue, 'total_trade_spend': total_trade_spend, 'net_revenue': net_revenue, 'trade_spend_per_case': trade_spend_per_case,
                    'spend_per_inc_uom': spend_per_inc_uom, 'trade_spend_percent': trade_spend_percent, 'total_profit': total_profit, 'profit_per_case': profit_per_case, 'profit_margin_percent': profit_margin_percent, 'profit_margin_wfb': profit_margin_wfb, 'incr_profit': incr_profit, 'profit_per_incr_case': profit_per_incr_case, 'roi': roi}
        df = pd.DataFrame.from_dict(required, orient='index')
        return df


if __name__ == "__main__":
    test = TradeKPIS()
    print(test.calculate_manufacturer(440, 418, 126, 2, 14.49))
    print(test.calculate_retailer(440, 418, 126, 2, 14.49))

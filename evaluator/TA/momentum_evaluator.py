import talib

from evaluator.TA.TA_evaluator import MomentumEvaluator, PriceStrings


# https://mrjbq7.github.io/ta-lib/func_groups/momentum_indicators.html

# ADX --> trend_strength
class ADXMomentumEvaluator(MomentumEvaluator):
    def __init__(self):
        super().__init__()

    # TODO : temp analysis
    def eval(self):
        adx_v = talib.ADX(self.data[PriceStrings.STR_PRICE_HIGH.value],
                          self.data[PriceStrings.STR_PRICE_LOW.value],
                          self.data[PriceStrings.STR_PRICE_CLOSE.value])

        last = adx_v.tail(1).values

        # An ADX above 30 on the scale indicates there is a strong trend
        if last > 30:
            pass

        # When ADX drops below 18, it often leads to a sideways or horizontal trading pattern
        elif last < 18:
            pass


class RSIMomentumEvaluator(MomentumEvaluator):
    def __init__(self):
        super().__init__()
        self.pertinence = 2

    # TODO : temp analysis
    def eval(self):
        rsi_v = talib.RSI(self.data[PriceStrings.STR_PRICE_CLOSE.value])

        # get the last 10 values of RSI
        last_values = rsi_v.tail(10).values

        first = last_values[0]
        last = last_values[-1]

        rsi_eval = self.eval_note

        # Difference between the last 10 candles
        if first > last:
            rsi_eval -= (first - last)
        else:
            rsi_eval += (last - first)

        if last > 50:
            rsi_eval += (last - 50)
        else:
            rsi_eval -= (50 - last)

        # 2 : modifications
        self.eval_note += rsi_eval / (2 * 100)


class OBVMomentumEvaluator(MomentumEvaluator):
    def __init__(self):
        super().__init__()

    def eval(self):
        obv_v = talib.OBV(self.data[PriceStrings.STR_PRICE_CLOSE.value],
                          self.data[PriceStrings.STR_PRICE_VOL.value])
        first = obv_v.iloc[0, 0]
        last = obv_v.iloc[-1, 0]

        if first - last > 0:
            pass


# William's % R --> overbought / oversold
class WilliamsRMomentumEvaluator(MomentumEvaluator):
    def __init__(self):
        super().__init__()

    def eval(self):
        willr_v = talib.WILLR(self.data[PriceStrings.STR_PRICE_HIGH.value],
                              self.data[PriceStrings.STR_PRICE_LOW.value],
                              self.data[PriceStrings.STR_PRICE_CLOSE.value])
        first = willr_v.iloc[0, 0]
        last = willr_v.iloc[-1, 0]

        if first - last > 0:
            pass


# TRIX --> percent rate-of-change trend
class TRIXMomentumEvaluator(MomentumEvaluator):
    def __init__(self):
        super().__init__()

    def eval(self):
        trix_v = talib.TRIX(self.data[PriceStrings.STR_PRICE_CLOSE.value])
        first = trix_v.iloc[0, 0]
        last = trix_v.iloc[-1, 0]

        if first - last > 0:
            pass


class MACDMomentumEvaluator(MomentumEvaluator):
    def __init__(self):
        super().__init__()

    def eval(self):
        macd_v = talib.MACD(self.data[PriceStrings.STR_PRICE_CLOSE.value])


class ChaikinOscillatorMomentumEvaluator(MomentumEvaluator):
    def __init__(self):
        super().__init__()

    def eval(self):
        pass


class StochasticMomentumEvaluator(MomentumEvaluator):
    def __init__(self):
        super().__init__()

    def eval(self):
        slowk, slowd = talib.STOCH(self.data[PriceStrings.STR_PRICE_HIGH.value],
                                   self.data[PriceStrings.STR_PRICE_LOW.value],
                                   self.data[PriceStrings.STR_PRICE_CLOSE.value])
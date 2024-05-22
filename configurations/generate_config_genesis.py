# -*- coding: utf-8 -*-
"""
# Vesu Pool Configuration

This notebook allows for the preparation of a configuration file from which new Vesu pools can be created. A pool configuration consists of three parameter sets:

- Pool parameters: parameters that apply to the entire pool
- Asset parametesr: parameters that apply to an asset in the pool
- Pair parameters: parameters that apply to a lending pair in the pool

While developers are free to create and configure Vesu pools at their own liking, in this notebook we assume that the basic configuration is provided as an input and derive certain risk parameters programmatically.

# Input Parameters

These parameters represent the basic configuration of a Vesu pool including the enabled supply assets and lending pairs.
"""

import pandas as pd

pool_parameters = {
    "owner": "0x0",                # no owner
    "fee_recipient": "0x0",        # no fee
    "recovery_period": 2592000,    # 30 days in seconds
    "subscription_period": 1209600 # 30 days in seconds
}

asset_parameters = [
  {
    "asset_name": "ethereum",
    "token": {
        "address": "0x049d36570d4e46f48e99674bd3fcc84644ddd6b96f7c741b1562b82f9e004dc7",
        "name": "Ether",
        "symbol": "ETH",
        "decimals": 18,
        "is_legacy": False
    },
    "oracle": {
        "address": "0x2a85bd616f912537c50a49a4076db02c00b29b2cdc8a197ce92ed1837fa875b",
        "pragma_key": "ETH/USD",
        "timeout": 14400,
        "number_of_sources": 4
    },
    "v_token": {
        "v_token_name": "Vesu Ether",
        "v_token_symbol": "vETH"
    },
    "debt_cap": 50000000,
    "floor": 100,
    "max_utilization": 0.95,
    "target_utilization": 0.8,
    "min_target_utilization": 0.78,
    "max_target_utilization": 0.82,
    "min_full_utilization_rate": 0.005,
    "max_full_utilization_rate": 2,
    "initial_full_utilization_rate": 0.5,
    "zero_utilization_rate": 0.001,
    "rate_half_life": 86400,
    "target_rate_percent": 0.2,
    "fee_rate": 0
  },
  {
    "asset_name": "wrapped-bitcoin",
    "token": {
        "address": "0x03fe2b97c1fd336e750087d68b9b867997fd64a2661ff3ca5a7c771641e8e7ac",
        "name": "Wrapped BTC",
        "symbol": "WBTC",
        "decimals": 8,
        "is_legacy": False
    },
    "oracle": {
        "address": "0x2a85bd616f912537c50a49a4076db02c00b29b2cdc8a197ce92ed1837fa875b",
        "pragma_key": "WBTC/USD",
        "timeout": 14400,
        "number_of_sources": 4
    },
    "v_token": {
        "v_token_name": "Vesu Wrapped BTC",
        "v_token_symbol": "vWBTC"
    },
    "debt_cap": 50000000,
    "floor": 100,
    "max_utilization": 0.95,
    "target_utilization": 0.8,
    "min_target_utilization": 0.78,
    "max_target_utilization": 0.82,
    "min_full_utilization_rate": 0.005,
    "max_full_utilization_rate": 2,
    "initial_full_utilization_rate": 0.5,
    "zero_utilization_rate": 0.001,
    "rate_half_life": 86400,
    "target_rate_percent": 0.2,
    "fee_rate": 0
  },
  {
    "asset_name": "usd-coin",
    "token": {
        "address": "0x053c91253bc9682c04929ca02ed00b3e423f6710d2ee7e0d5ebb06f3ecf368a8",
        "name": "USD Coin",
        "symbol": "USDC",
        "decimals": 6,
        "is_legacy": False
    },
    "oracle": {
        "address": "0x2a85bd616f912537c50a49a4076db02c00b29b2cdc8a197ce92ed1837fa875b",
        "pragma_key": "USDC/USD",
        "timeout": 14400,
        "number_of_sources": 4
    },
    "v_token": {
        "v_token_name": "Vesu USD Coin",
        "v_token_symbol": "vUSDC"
    },
    "debt_cap": 50000000,
    "floor": 100,
    "max_utilization": 0.95,
    "target_utilization": 0.8,
    "min_target_utilization": 0.78,
    "max_target_utilization": 0.82,
    "min_full_utilization_rate": 0.005,
    "max_full_utilization_rate": 2,
    "initial_full_utilization_rate": 0.5,
    "zero_utilization_rate": 0.001,
    "rate_half_life": 86400,
    "target_rate_percent": 0.2,
    "fee_rate": 0
  },
  {
    "asset_name": "tether",
    "token": {
        "address": "0x068f5c6a61780768455de69077e07e89787839bf8166decfbf92b645209c0fb8",
        "name": "Tether USD",
        "symbol": "USDT",
        "decimals": 6,
        "is_legacy": False
    },
    "oracle": {
        "address": "0x2a85bd616f912537c50a49a4076db02c00b29b2cdc8a197ce92ed1837fa875b",
        "pragma_key": "USDT/USD",
        "timeout": 14400,
        "number_of_sources": 4
    },
    "v_token": {
        "v_token_name": "Vesu Tether USD",
        "v_token_symbol": "vUSDT"
    },
    "debt_cap": 50000000,
    "floor": 100,
    "max_utilization": 0.95,
    "target_utilization": 0.8,
    "min_target_utilization": 0.78,
    "max_target_utilization": 0.82,
    "min_full_utilization_rate": 0.005,
    "max_full_utilization_rate": 2,
    "initial_full_utilization_rate": 0.5,
    "zero_utilization_rate": 0.001,
    "rate_half_life": 86400,
    "target_rate_percent": 0.2,
    "fee_rate": 0
  },
  {
    "asset_name": "wrapped-steth",
    "token": {
        "address": "0x042b8f0484674ca266ac5d08e4ac6a3fe65bd3129795def2dca5c34ecc5f96d2",
        "name": "Starknet Wrapped Staked Ether",
        "symbol": "wstETH",
        "decimals": 18,
        "is_legacy": False
    },
    "oracle": {
        "address": "0x2a85bd616f912537c50a49a4076db02c00b29b2cdc8a197ce92ed1837fa875b",
        "pragma_key": "WSTETH/USD",
        "timeout": 14400,
        "number_of_sources": 4
    },
    "v_token": {
        "v_token_name": "Vesu Wrapped Staked Ether",
        "v_token_symbol": "vWSTETH"
    },
    "debt_cap": 50000000,
    "floor": 100,
    "max_utilization": 0.95,
    "target_utilization": 0.8,
    "min_target_utilization": 0.78,
    "max_target_utilization": 0.82,
    "min_full_utilization_rate": 0.005,
    "max_full_utilization_rate": 2,
    "initial_full_utilization_rate": 0.5,
    "zero_utilization_rate": 0.001,
    "rate_half_life": 86400,
    "target_rate_percent": 0.2,
    "fee_rate": 0
  },
  {
    "asset_name": "starknet",
    "token": {
        "address": "0x04718f5a0fc34cc1af16a1cdee98ffb20c31f5cd61d6ab07201858f4287c938d",
        "name": "Starknet Token",
        "symbol": "STRK",
        "decimals": 18,
        "is_legacy": False
    },
    "oracle": {
        "address": "0x2a85bd616f912537c50a49a4076db02c00b29b2cdc8a197ce92ed1837fa875b",
        "pragma_key": "STRK/USD",
        "timeout": 14400,
        "number_of_sources": 4
    },
    "v_token": {
        "v_token_name": "Vesu Starknet",
        "v_token_symbol": "vSTRK"
    },
    "debt_cap": 50000000,
    "floor": 100,
    "max_utilization": 0.95,
    "target_utilization": 0.8,
    "min_target_utilization": 0.78,
    "max_target_utilization": 0.82,
    "min_full_utilization_rate": 0.005,
    "max_full_utilization_rate": 2,
    "initial_full_utilization_rate": 0.5,
    "zero_utilization_rate": 0.001,
    "rate_half_life": 86400,
    "target_rate_percent": 0.2,
    "fee_rate": 0
  }
]

asset_params = pd.DataFrame(asset_parameters)

pair_parameters = [
  {
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "usd-coin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "tether",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "wrapped-steth",
    "liquidation_discount": 0.95,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "starknet",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "ethereum",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "usd-coin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "tether",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "wrapped-steth",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "starknet",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "ethereum",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "tether",
    "liquidation_discount": 0.95,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "wrapped-steth",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "starknet",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "tether",
    "collateral_asset_name": "ethereum",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "tether",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "tether",
    "collateral_asset_name": "usd-coin",
    "liquidation_discount": 0.95,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "tether",
    "collateral_asset_name": "wrapped-steth",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "tether",
    "collateral_asset_name": "starknet",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "ethereum",
    "liquidation_discount": 0.95,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "usd-coin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "tether",
    "liquidation_discount": 0.9,
    "risk_level_factor": 5
  },
  {
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "starknet",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "starknet",
    "collateral_asset_name": "ethereum",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "starknet",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "starknet",
    "collateral_asset_name": "usd-coin",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "starknet",
    "collateral_asset_name": "tether",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  },
  {
    "debt_asset_name": "starknet",
    "collateral_asset_name": "wrapped-steth",
    "liquidation_discount": 0.9,
    "risk_level_factor": 3
  }
]

pair_params = pd.DataFrame(pair_parameters)

"""# Compute Risk Parameters

We use BProtocol/RiskDAO's _Smart LTV_ formula [1] to derive the Max LTVs for the various lending pairs in a Vesu pool.

This model relies on the assumption of log-normal price movements and is calibrated to an asset's price volatility, available DEX liquidity and (maximal) liquidation amounts.

The model offers a simplified, yet intuitive and practical, approach to deriving appropriate risk parameters for a Vesu pool. The model further allows for the assessment of market risk given a pool's loan-to-value ratio and market conditions.

[1] https://github.com/Risk-DAO/Reports/blob/main/a-smart-contract-ltv-formula.pdf
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install requests

"""## Fetch prices

We use the CoinGecko API to fetch daily prices for the various assets in a pool.

Since pairwise prices are not available for all lending pairs, we compute those using the USD prices. E.g. for the ETH/WBTC pair the price is computed as

$$p(\verb'ETH/WBTC') = \frac{p(\verb'ETH/USD')}{p(\verb'WBTC/USD')}$$

Furthermore, note that a Coingecko pro-account is needed in order to access an appropriate history of asset price data.
"""

import requests
import pandas as pd
from google.colab import userdata

# static params
cg_key = userdata.get('cg_key')               # fetch CG pro account API key
url = 'https://pro-api.coingecko.com/api/v3/' # CG pro endpoint
currency = 'usd'                              # denote prices in USD
days = 'max'                                  # max price history
interval = 'daily'                            # daily prices

# request function
def fetch_prices(coin):
  request = f'coins/{coin}/market_chart'
  params = {
          'x_cg_pro_api_key': cg_key,
          'vs_currency': f'{currency}',
          'days': f'{days}',
          'interval': f'{interval}'
  }
  response = requests.get(url + request, params = params)

  # error handling
  if response.status_code == 200:
          print(f'Successfully retrieved data for {coin}')
          data = response.json()
  else:
          print(f'Failed to retrieve data for {coin}')

  # convert to dataframe
  df = pd.DataFrame(data['prices'])
  df.columns = ['date',coin]
  df['date'] = pd.to_datetime(df['date'], unit = 'ms')
  df.set_index('date', drop = True, inplace=True)
  return df

# fetch data
coins = ['ethereum','wrapped-bitcoin','usd-coin','tether','wrapped-steth',
         'starknet']
data = list(map(fetch_prices, coins))

# join datasets
prices = data[0].join(data[1:6], how='outer')

# extract period
start_date = '2022-01-01' # start of availability of all but STRK data
end_date   = '2024-04-30'
prices = prices.query('date >= @start_date and date <= @end_date')

# export as csv (optional)
# prices.sort_index(ascending=False).to_csv('cg_prices.csv')

"""## Compute Volatility

We use a pessimistic volatility measure representing the "worst-case" volatility. This "worst-case" volatility is measured by the maximal daily price decline (negative log-return).
"""

from itertools import permutations
import numpy as np

# compute pairwise prices
prices_pairwise = pd.DataFrame()
for p in permutations(prices.columns,2):
        title = p
        prices_pairwise[title] =  prices[p[0]]/prices[p[1]]

# compute log returns
returns = np.log(prices_pairwise / prices_pairwise.shift(1))

# volatility (daily, worst-case)
volatility = returns.min(axis="rows").abs()

"""## Fetch DEX liquidity

We fetched the DEX liquidity from https://avnu.fi frontend.

For a more robust and automated estimations, this should be based on an API and values should be averaged over an apropriate period.
"""

liquidity_data = [
  {
    "depth": 0.1,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 2600000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "usd-coin",
    "liquidity": 1700000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "tether",
    "liquidity": 1900000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 2700000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "starknet",
    "liquidity": 1300000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "ethereum",
    "liquidity": 1700000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "usd-coin",
    "liquidity": 1200000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "tether",
    "liquidity": 1300000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 1900000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "starknet",
    "liquidity": 800000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "ethereum",
    "liquidity": 1200000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 1000000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "tether",
    "liquidity": 2500000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 2000000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "starknet",
    "liquidity": 1500000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "tether",
    "collateral_asset_name": "ethereum",
    "liquidity": 1000000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "tether",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 800000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "tether",
    "collateral_asset_name": "usd-coin",
    "liquidity": 4200000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "tether",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 800000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "tether",
    "collateral_asset_name": "starknet",
    "liquidity": 1200000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "ethereum",
    "liquidity": 1900000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 2000000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "usd-coin",
    "liquidity": 1300000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "tether",
    "liquidity": 1800000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "starknet",
    "liquidity": 900000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "ethereum",
    "liquidity": 2200000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 1400000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "usd-coin",
    "liquidity": 2300000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "tether",
    "liquidity": 2000000
  },
  {
    "depth": 0.1,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 2000000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 2500000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "usd-coin",
    "liquidity": 1200000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "tether",
    "liquidity": 1000000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 2500000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "ethereum",
    "collateral_asset_name": "starknet",
    "liquidity": 1100000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "ethereum",
    "liquidity": 1400000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "usd-coin",
    "liquidity": 900000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "tether",
    "liquidity": 800000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 1300000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-bitcoin",
    "collateral_asset_name": "starknet",
    "liquidity": 700000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "ethereum",
    "liquidity": 1000000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 800000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "tether",
    "liquidity": 1900000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 1500000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "usd-coin",
    "collateral_asset_name": "starknet",
    "liquidity": 1100000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "tether",
    "collateral_asset_name": "ethereum",
    "liquidity": 900000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "tether",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 700000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "tether",
    "collateral_asset_name": "usd-coin",
    "liquidity": 4000000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "tether",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 1200000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "tether",
    "collateral_asset_name": "starknet",
    "liquidity": 900000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "ethereum",
    "liquidity": 1800000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 1700000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "usd-coin",
    "liquidity": 1000000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "tether",
    "liquidity": 800000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "wrapped-steth",
    "collateral_asset_name": "starknet",
    "liquidity": 700000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "ethereum",
    "liquidity": 1500000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "wrapped-bitcoin",
    "liquidity": 900000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "usd-coin",
    "liquidity": 1300000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "tether",
    "liquidity": 1100000
  },
  {
    "depth": 0.05,
    "debt_asset_name": "starknet",
    "collateral_asset_name": "wrapped-steth",
    "liquidity": 1200000
  }
]

liquidity = pd.DataFrame(liquidity_data)

"""## Compute Max Loan-to-Value

The SmartLTV formula is

$$\verb'LTV' = e^{-\frac{1}{r}\frac{\sigma}{\sqrt{l/d}}}-\beta$$

Where:

* $\sigma$ - Pair's price volatility
* $\beta$ - Pair's liquidation bonus
* $l$ - Available dex liquidity for the pair with a price impact of $\beta$
* $d$ - Targeted total debt in the respective asset
* $\verb'LTV'$ - Pair's loan-to-value ratio
"""

# Computed LTVs are appended to the pair_parameters dictionary
for p in pair_parameters:
  debt_asset_name = p["debt_asset_name"]
  collateral_asset_name = p["collateral_asset_name"]
  discount = np.round(1 - p["liquidation_discount"],2)
  debt_cap = asset_params.query('asset_name == @debt_asset_name').debt_cap.iloc[0]
  liq = liquidity.query("collateral_asset_name == @collateral_asset_name and debt_asset_name == @debt_asset_name and depth == @discount").liquidity.iloc[0]
  vola = volatility[(collateral_asset_name, debt_asset_name)]
  exponent = (1/p["risk_level_factor"]) * (vola / np.sqrt(liq / debt_cap))
  ltv = np.exp(- exponent) - discount
  p["max_ltv"] = np.round(ltv,2)
  p["shutdown_ltv"] = 1

"""# Write pool configuration to file"""

import json

# Convert per-annum to per-second interest rates
# Note we format as a decimal string as otherwise python writes in scientific
def to_per_second(per_annum_rate):
  per_second_rate = (1+per_annum_rate)**(1/31104000) - 1
  return f'{per_second_rate:.18f}'

for a in asset_parameters:
  a["min_full_utilization_rate"] = to_per_second(a["min_full_utilization_rate"])
  a["max_full_utilization_rate"] = to_per_second(a["max_full_utilization_rate"])
  a["initial_full_utilization_rate"] = to_per_second(a["initial_full_utilization_rate"])
  a["zero_utilization_rate"] = to_per_second(a["zero_utilization_rate"])

# Add asset addresses to pair parameters
for p in pair_parameters:
  debt_asset_name = p["debt_asset_name"]
  collateral_asset_name = p["collateral_asset_name"]
  p["debt_asset"] = (asset_params.query('asset_name == @debt_asset_name').token.iloc[0])["address"]
  p["collateral_asset"] = (asset_params.query('asset_name == @collateral_asset_name').token.iloc[0])["address"]

# Combine parameters in single json
parameters = {
    "asset_parameters": asset_parameters,
    "pair_parameters": pair_parameters,
    "pool_parameters": pool_parameters
}

# Convert and write JSON object to file
with open("config_genesis_sn_main.json", "w") as outfile:
    json.dump(parameters, outfile, indent=2)

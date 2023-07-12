import math

"""
seconds_per_year = 31556926
seconds_per_epoch = 384
epochs_per_year = seconds_per_year / seconds_per_epoch
base_reward_factor = 64
gwei_per_eth = 31622



When the staking ratio increases, it  means that more ETH is being staked compared to the total supply. 
This can lead to a decrease in the staking rewards per ETH, resulting in a lower APR. 
Conversely, when the staking ratio decreases, the rewards per ETH may increase, leading to a higher APR.
"""




import math

#Current amount of eth staked on beaconchain
totalStaked = 19574465

APR_15 = math.exp(31556926 / 384 * 64 / 31622 / totalStaked ** 0.5) - 1

increase_eth = totalStaked * 0.5
totalStaked_50 = totalStaked + increase_eth

APR_50 = math.exp(31556926 / 384 * 64 / 31622 / totalStaked_50 ** 0.5) - 1

print(f"Current Staking APR: {APR_15* 100:.2f}%")
print(f"APR with 50% Staking Ratio Increase : {APR_50 * 100:.2f}%")


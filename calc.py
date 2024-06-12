import requests

def get_network_info():
    try:
        blockreward_response = requests.get('https://api.spectre-network.org/info/blockreward?stringOnly=false', headers={'accept': 'application/json'})
        blockreward = blockreward_response.json().get('blockreward')

        hashrate_response = requests.get('https://api.spectre-network.org/info/hashrate?stringOnly=false', headers={'accept': 'application/json'})
        network_hashrate = hashrate_response.json().get('hashrate')  # in TH/s

        return blockreward, network_hashrate
    except Exception as e:
        print(f"An error occurred while fetching network info: {e}")
        return None, None

def rewards_in_range(blockreward, blocks):
    return blockreward * blocks

def get_mining_rewards(blockreward, percent_of_network):
    rewards = dict()
    rewards['second'] = rewards_in_range(blockreward, 1) * percent_of_network
    rewards['minute'] = rewards_in_range(blockreward, 60) * percent_of_network
    rewards['hour'] = rewards_in_range(blockreward, 60*60) * percent_of_network
    rewards['day'] = rewards_in_range(blockreward, 60*60*24) * percent_of_network
    rewards['week'] = rewards_in_range(blockreward, 60*60*24*7) * percent_of_network
    rewards['month'] = rewards_in_range(blockreward, 60*60*24*(365.25/12)) * percent_of_network
    rewards['year'] = rewards_in_range(blockreward, 60*60*24*365.25) * percent_of_network
    return rewards

if __name__ == "__main__":
    blockreward, network_hashrate_ths = get_network_info()
    if blockreward is not None and network_hashrate_ths is not None:
        own_hashrate_khs = float(input("Enter your mining hashrate in kH/s: "))

        own_hashrate_ths = own_hashrate_khs / 1_000_000_000  # Convert kH/s to TH/s
        percent_of_network = own_hashrate_ths / float(network_hashrate_ths)
        network_hashrate_mhs = float(network_hashrate_ths) * 1_000_000  # Convert TH/s to MH/s

        blocks_per_day = 86_400  # Number of blocks per day
        total_SPR_per_day = blocks_per_day * blockreward

        print(f"Current Network Hashrate: {network_hashrate_mhs:.2f} MH/s")
        print(f"Total Network SPR Mined per Day: {total_SPR_per_day:.2f} SPR")
        print(f"Your Portion of the Network Hashrate: {percent_of_network:.9f} ({percent_of_network*100:.9f}%)")

        rewards = get_mining_rewards(blockreward, percent_of_network)
        for period, reward in rewards.items():
            print(f"Estimated mining reward per {period}: {reward:.6f} SPR")

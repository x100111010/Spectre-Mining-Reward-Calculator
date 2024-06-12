# Spectre Mining Reward Calculator

A Python script to calculate estimated mining rewards for the Spectre Network. This script fetches the current block reward and network hashrate from the Rest API and calculates the estimated rewards for various time intervals based on the user's hashrate.

## Features

- Fetches the current block reward from the Rest API.
- Fetches the current network hashrate from the Rest API.
- Converts user hashrate from kH/s to TH/s.
- Calculates the user's portion of the network hashrate.
- Calculates total network coins mined per day.
- Displays the current network hashrate, total network coins mined per day, and the user's portion of the network hashrate.
- Estimates mining rewards for the following time intervals:
  - Per second
  - Per minute
  - Per hour
  - Per day
  - Per week
  - Per month
  - Per year

## Usage

1. Ensure you have Python installed on your system.
2. Clone this repository.
3. Install the required dependencies using pip.
4. Run the script and input your mining hashrate when prompted.

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/x100111010/Spectre-Mining-Reward-Calculator.git
    cd Spectre-Mining-Reward-Calculator
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

### Running the Script

```sh
python calc.py
```

When prompted, enter your mining hashrate in kH/s. The script will output the current network hashrate, total network coins mined per day, your portion of the network hashrate, and estimated mining rewards for different time intervals.

## License

This project is licensed under the MIT License.
```

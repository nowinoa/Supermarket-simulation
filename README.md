# Supermarket Checkout and Lottery Simulation

## Description

This Python program simulates a supermarket checkout system, managing multiple checkout lanes, processing customer queues, and implementing a lottery system. It is designed to mimic a real-world supermarket environment, where customers with varying basket sizes are assigned to either regular or self-service lanes based on their items, and are eligible for a lottery depending on the size of their basket.  

### Key Features:

- **Lane Assignment**:  
  - Customers with fewer than 10 items are prioritized for **self-service lanes** unless those lanes are saturated.  
  - Customers with 10 or more items are directed to **regular lanes**, with new lanes opening dynamically if needed.  

- **Checkout Process**:  
  - Each customer has a checkout time based on their basket size and the type of lane:  
    - **Regular Lane**: 4 seconds per item.  
    - **Self-Service Lane**: 6 seconds per item.  
  - During each 30-second simulation interval, customers' checkout times are reduced.  
  - Customers are removed from the lane once their checkout time reaches 0.  

- **Lane Management**:  
  - Lanes dynamically **open and close** based on customer demand:  
    - One **regular lane** (L1, L2, L3, or L4) and **self-service lane** (L5) will always remain open to ensure availability.  
    - If all other lanes are full or closed, these will be re-opened to accommodate new customers.  
    - Lanes without customers will automatically close.  

- **Lottery System**:  
  - Customers with 10 or more items automatically qualify for a lottery ticket.  

## Installation

1. Clone the repository to your local machine:  

   ```bash  
   git clone https://github.com/nowinoa/Supermarket-simulation.git
   cd supermarket-simulation

2. Ensure you have Python 3.7+ installed.

3. Install dependencies (pip install ...):
    - unittest
    - random
    - time
    - datetime

## Usage

### Running the Simulation
To test the simulation, you will need to run the file `supermarket.py`. Enter ``` python supermarket.py ```

The output will be shown every 30s and it will include:
- Total number of customers
- Time since the simulation started
- Customers: id, items in the basket, checkout time in seconds and lottery ticket assignation. 
- Lanea: lane id, status, customers assigned represented by '*', and the first customer on the line (for the self-service will show the users using it).

## Credits
Created by <a href="https://github.com/nowinoa">Ainhoa Prada</a>.
The following third-party assets were used:

* React
* Bootstrap
* Font Awesome

## License
This project is under MIT license
        
## Questions
For any questions or issues feel free to contact me at: apt.code14@gmail.com

To explore more about my projects visit my profile :point_right: <a href="https://github.com/nowinoa">:computer:</a>

© 2024 Ainhoa Prada. Confidential and Proprietary. All Rights Reserved.

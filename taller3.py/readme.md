General Idea
The function register_sales() is designed to interactively record sales. Each sale has:


- A product name,


- A unit price,


- A quantity sold.


Every sale is stored as a dictionary inside a list. The function keeps asking for new sales until the user decides to stop, and then it returns the complete list.

Step-by-Step Flow
1) Start of the function

- A list sales is created to hold all the sales.

- A variable another is set to 'y' so the loop starts.

2) Looping

- The program enters a while loop that continues as long as the user answers 'y' when asked if they want to register another sale.

3) User input

- The program asks for the product name, unit price, and quantity.

- It uses try/except blocks to handle invalid inputs:

- If the price isn’t a valid number, it defaults to 0.0.

- If the quantity isn’t a valid integer, it defaults to 0.

4) Saving the sale

- A dictionary is created like this:

{'product': product, 'price': price, 'quantity': quantity}

- That dictionary is added to the sales list.

5) Confirmation

- The program prints a message confirming the sale, showing the quantity, product, and formatted price.

6) Ask to continue

- The user is asked if they want to register another sale (y/n).

- If they type 'y', the loop repeats. If 'n', the loop ends.

7) Return

- When the loop ends, the function returns the full list of sales.

Example Run
If you enter:


Enter product name: Apple
Enter unit price: 1.5
Enter quantity sold: 10
Do you want to register another sale? (y/n): y
Enter product name: Banana
Enter unit price: 2
Enter quantity sold: 5
Do you want to register another sale? (y/n): n


The function will return:


[
    {'product': 'Apple', 'price': 1.5, 'quantity': 10},
    {'product': 'Banana', 'price': 2.0, 'quantity': 5}
]

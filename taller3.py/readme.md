# register_sales()

The **`register_sales()`** function allows you to interactively record sales.  
Each sale includes:

- Product name  
- Unit price  
- Quantity sold  

Sales are stored as dictionaries inside a list. The process continues until the user decides to stop.

---

## Step-by-Step Flow

1. **Function start**
   - A list `sales` is created to store all sales.
   - A variable `another = 'y'` is initialized to start the loop.

2. **Looping**
   - As long as the user answers `'y'`, the program keeps registering sales.

3. **User input**
   - The program asks for:
     - Product name
     - Unit price
     - Quantity sold
   - Input validation with `try/except`:
     - If the price is invalid → defaults to `0.0`.
     - If the quantity is invalid → defaults to `0`.

4. **Saving the sale**
   - A dictionary is created:
     ```python
     {'product': product, 'price': price, 'quantity': quantity}
     ```
   - The dictionary is appended to the `sales` list.

5. **Confirmation**
   - A message confirms the sale:
     ```
     Sale registered: 10 Apple at $1.50
     ```

6. **Continue or stop**
   - The user is asked if they want to register another sale (`y/n`).
   - `'y'` → loop continues.  
   - `'n'` → loop ends.

7. **Return**
   - When finished, the function returns the complete list of sales.

---

## Example Run

Enter product name: Apple
Enter unit price: 1.5
Enter quantity sold: 10
Do you want to register another sale? (y/n): y
Enter product name: Banana
Enter unit price: 2
Enter quantity sold: 5
Do you want to register another sale? (y/n): n

### Returned result:
```python
[
    {'product': 'Apple', 'price': 1.5, 'quantity': 10},
    {'product': 'Banana', 'price': 2.0, 'quantity': 5}
]

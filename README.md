# Online Food Ordering System

The Online Food Ordering System is a platform that allows users to place food orders from a variety of restaurants and have them delivered to their doorstep. This system is organized into the following modules:

1. **User Management**
2. **Restaurant Management**
3. **Order Management**
4. **Payment Management**
5. **Discount & Offers Management**

## User Management

The User Management module is responsible for handling user accounts and includes the following functions:

- **Register**: New users can register for an account by providing their personal details, contact information, and payment details.
- **Login**: Registered users can log in to their account.
- **View Profile**: Users can view and update their profile information.
- **Change Password**: Users can change their password.

## Restaurant Management

The Restaurant Management module is responsible for managing restaurants and their menus. It includes the following functions:

- **Add Restaurant**: System admin can add new restaurants to the platform by providing restaurant details such as name, address, contact information, and menu items.
- **Update Restaurant**: System admin can update the details of existing restaurants, including menu items.
- **Delete Restaurant**: System admin can delete existing restaurants from the platform.

## Order Management

The Order Management module handles the order process and includes the following functions:

- **Place Order**: Users can place an order by selecting a restaurant, choosing items from the menu, and providing delivery details.
- **Track Order**: Users can track the status of their order, including estimated delivery time and the delivery person's contact details.
- **Cancel Order**: Users can cancel an order before it is delivered.

## Payment Management

The Payment Management module is responsible for handling the payment process and includes the following functions:

- **Calculate Total**: This function calculates the total amount for the order, including taxes and delivery charges.
- **Payment Gateway Integration**: It integrates a payment gateway to facilitate online payments.
- **View Payment History**: Users can view their payment history.

## Discount & Offers Management

The Discount & Offers Management module handles the discount and offer process with the following functions:

- **Check Discount**: It checks the total price of an ordered food of an individual customer. If the total price of food is greater than Rs.350, a discount of 25% is applied.
- **Check Offers**: This function checks whether the chosen restaurant provides offers. If offers are applicable for the customer's chosen restaurant, they are included in the bill calculation.

## Steps to Run this Projects.

1. **Prerequisites**:
   - Ensure you have Python installed on your system.

2. **Clone the Project**:
   - Clone the project's repository from a version control system like GitHub, or download the project's source code if available.

3. **Navigate to the Project Directory**:
   - Use the `cd` command to navigate to the project directory where your main Python script is located.

4. **Run the Project**:
   - Run the main Python script that serves as the entry point to your project.

   ```
   python main.py
   ```

   Replace `main.py` with the actual name of your main script.

5. **Interact with the Project**:
   - After running the script, you can interact with the project based on the available functions and features provided by the OOP code.

6. **Customization (Optional)**:
   - If needed, you can customize the project by modifying the code within your Python script. Make changes to the OOP classes and methods to add or modify features.

7. **Testing**:
   - Thoroughly test the project to ensure that it functions as expected and handles various scenarios.

Since this approach is based on OOP principles and does not involve a database or web framework.

### Important Points

1. All modules are built using object-oriented programming (OOP) principles, such as encapsulation, inheritance, and polymorphism.
2. Exception handling is used to ensure that the system gracefully handles errors.
3. Necessary validations are implemented throughout the system to maintain data integrity and security.

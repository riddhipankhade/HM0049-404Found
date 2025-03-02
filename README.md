# HM0049-404Found
# EduMarket

EduMarket is a web application designed for students to buy and sell educational resources online, such as textbooks, stationery, and other learning materials. This platform creates a convenient and cost-effective marketplace, especially for college students. Enhanced categorical search features help students find specific products as per their needs quickly and efficiently.

---

## Table of Contents
1. [Host Locally](#host-locally)
2. [Usage](#usage)
3. [Frameworks Used](#frameworks-used)
4. [Contributors](#contributors)

---

## Host Locally
Follow these steps to host EduMarket locally on your machine:

### Step 1: Download the Zip File
- Download the project repository as a zip file from GitHub.

### Step 2: Extract the Zip File
- Extract the downloaded zip file to your desired location.

### Step 3: Open the Project in VS Code
- Open the extracted folder in Visual Studio Code (VS Code).

### Step 4: Open the Terminal
- Open the terminal in VS Code using `Ctrl + ` (backtick) or navigate to `Terminal > New Terminal`.

### Step 5: Navigate to the Project Directory
- Change to the project directory using the `cd` command:
  ```bash
  cd student_marketplace
  
### Step 6: Install Necessary Modules
- Install the required Python modules (e.g., Flask, SQLAlchemy) using pip:
  ```bash
  pip install flask sqlalchemy

### Step 7: Run the Application
- Run the application using the following command:
 ```bash
    python app.py
```
- Once server starts, you will see a local hosting link(e.g., http://127.0.0.1:5000).

### Step 8: Access the Application 
- Open your browser and paste in the provided local hosting link (e.g., http://127.0.0.1:5000) to access EduMarket.

## Usage

EduMarket is designed to be simple and intuitive for students to buy and sell educational resources. Here's how you can use the application:

### 1. Home Page
- The home page looks like this:
![Screenshot 2025-03-02 101453](https://github.com/user-attachments/assets/526b5fb3-1442-40f9-813a-498fdc672436)

- From here, you can browse available products in diffrent categories or navigate to the login/signup page.

### 2. Log In or Sign Up
- If you already have an account, click **Log In** on the navigation bar. If you're new, click **Register** to create an account.
![Screenshot 2025-03-02 103639](https://github.com/user-attachments/assets/a4ec9628-016d-4517-871e-151582976818)
![Screenshot 2025-03-02 103707](https://github.com/user-attachments/assets/793362ab-ae9e-47d9-b4b5-1f1fe4fe30a7)

### 3. Buy Products
- After logging in, you can browse products on the home page or use the search bar to find specific items.
- To buy a product, contact the owner using the provided contact details on the product page.
![Screenshot 2025-03-02 103715](https://github.com/user-attachments/assets/4f59c777-cd9d-448f-8f26-7163e36ac086)

### 4. Sell Products
- To sell a product, click the **Sell Product** button on the navigation bar and you will be directed to a page shown below.
![Screenshot 2025-03-02 103755](https://github.com/user-attachments/assets/effe21a5-6359-4ae4-ae35-ca3354d720c5)

- Fill out the form with details about the product (e.g., name, description, price, category) and submit it.

### 5. Product Listing Page
- Once you post a product, it will appear on the home page
- Other users can now view and purchase your product.

---
## Frameworks Used

### Tech Stack
#### Backend:
- **Flask**: Python web framework for handling server-side logic.
- **Flask-SQLAlchemy**: ORM (Object-Relational Mapper) for database management.
- **Flask-Login**: Handles user authentication (login, logout, and session management).

#### Frontend:
- **HTML**: For structuring the web pages.
- **CSS**: For styling the application.
  - **Bootstrap 5.3**: Used for responsive and modern UI design.
- **Jinja2**: Templating engine for rendering dynamic content.

#### Database:
- **SQLite**: Lightweight database used for storing user and product data.
  - Managed using **Flask-SQLAlchemy**.

---
## Contributors

This project was developed by:
- Riddhi Pankhade
- Kshitij Kediya
- Arya Patange

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
  ![Home Page]({image})
- From here, you can browse available products in diffrent categories or navigate to the login/signup page.

### 2. Log In or Sign Up
- If you already have an account, click **Log In** on the navigation bar. If you're new, click **Sign Up** to create an account.
  ![Log In or Sign Up]({image pointing at the log in or register on the nav bar})

### 3. Buy Products
- After logging in, you can browse products on the home page or use the search bar to find specific items.
- To buy a product, contact the owner using the provided contact details on the product page.

### 4. Sell Products
- To sell a product, click the **Post Product** button on the navigation bar.
  ![Post Product Button]({ss of the button and the post product page})
- Fill out the form with details about the product (e.g., name, description, price, category) and submit it.

### 5. Product Listing Page
- Once you post a product, it will appear on the home page like this:
  ![Product Listing Page]({home page with the products you added})
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

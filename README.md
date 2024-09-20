# Product API

## Description
A simple Django application that provides an API for managing products. This application allows you to create and retrieve a list of products.

## Features
- Create a new product via a POST request.
- Retrieve a list of all products via a GET request.
- Simple frontend with a form to add products and display them in a table.

## Technologies Used
- Django
- Django REST Framework
- SQLite (default database)
- HTML, CSS, JavaScript (for the frontend)

## Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/product-api.git
   cd product-api
2. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
4. Apply database migrations:
   ```bash
   python manage.py migrate
5. Run the development server:
   ```bash
   python manage.py runserver
6. Open your browser and go to http://127.0.0.1:8000/api/products/ to access the application.
   
   
## API Endpoints
### Create a new product
- http://127.0.0.1:8000/api/products/create/
### Retrieve a list of all products 
- http://127.0.0.1:8000/api/products/list/ 

## Usage
Use the provided HTML form to add a new product, which will then be displayed in a table.
   
   

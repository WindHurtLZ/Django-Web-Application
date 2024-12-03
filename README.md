# Django_Web_Application

> Web Dashboard and User Interface for Advanced Bike-Sharing System

This repository contains the source code for the **Web Dashboard** and **User Interface** of an advanced bike-sharing system. The project is developed using **Django**, leveraging the **oneM2M IoT standard** and **DECT NR+ technology** to address key challenges in traditional bike-sharing systems, such as energy inefficiency, communication issues, and scalability limitations.

---

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Directory Structure](#directory-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

The **Web Dashboard** serves as the management hub, providing operators with tools to monitor and manage the bike fleet, while the **User Interface** offers a user-friendly platform for customers to rent bikes effortlessly. Key highlights include:
- **Real-time Map**: Tracks bike locations and historical movement.
- **Speed Monitoring**: Displays live speed updates for fleet management.
- **Mesh Network Visualization**: Monitors DECT NR+ network performance.
- **Streamlined Bike Rental**: Simplified user experience for renting bikes and secure payment processing.

---

## Features

- **Device Management**: Automates device resource registration with the oneM2M server.
- **CRUD Operations**: Full support for managing devices via the dashboard.
- **Real-Time Monitoring**: Map and widgets display live fleet data.
- **User Authentication**: Role-based access for staff and customers.
- **Payment Integration**: Secure payment system for bike rentals.
- **Mesh Network Insights**: Visualize device connectivity and signal strength.

---

## Technologies Used

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (default), easily configurable for other databases.
- **IoT Standards**: oneM2M TS-0023, DECT NR+ technology.
- **Hosting**: AWS for oneM2M-compliant server.

---

## Directory Structure

```plaintext
Django_Web_Application/
│
├── apps/
│   ├── auth/          # User authentication module
│   ├── home/          # Homepage and dashboard components
│   ├── management/    # Device and fleet management
│   ├── widgets/       # Reusable dashboard widgets
│   └── mock/          # Mock data for testing purposes
│
├── core/              # Core project configurations
├── static/            # Static files (CSS, JS, images)
├── templates/         # HTML templates
│   ├── accounts/      # User login, signup, and profile pages
│   ├── home/          # Dashboard templates
│   ├── layouts/       # Common layout templates
│   ├── management/    # Device management templates
│   └── widgets/       # Widget-specific templates
│
├── init/              # Initial setup scripts
├── constant/          # Project constants and settings
├── .gitignore         # Git ignore file
├── manage.py          # Django management script
└── README.md          # Project documentation
```

---

## Installation

Follow these steps to set up the project locally:

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)
- Django (pre-installed via `requirements.txt`)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Django_Web_Application.git
   cd Django_Web_Application
   ```

2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open the app in your browser at `http://127.0.0.1:8000`.

---

## Usage

### For Operators (Web Dashboard)
- Access the dashboard to monitor and manage the fleet.
- Use the widgets for real-time updates on speed, location, and mesh network status.

### For Customers (User Interface)
- Rent bikes by entering the bike's unique ID.
- Make secure payments to unlock bikes and start rides.

---

## Contributing

Contributions are welcome! Please follow these steps to contribute:
1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add feature-name"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the [MIT License](LICENSE).

---

## Contact

For questions or suggestions, please contact:
- [Name](mail)

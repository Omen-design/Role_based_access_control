# RBAC (registration)
- RBAC stands for Role based access control system
-folder (RBAC)
-main project(registration)
-app name(app1)

## Overview
RBAC stands for Role-Based Access Control System. This project implements an RBAC system that manages user access based on their assigned roles. The application includes three types of roles: **Admin**, **User**, and **Moderator**.
Each role has specific permissions that dictate what actions users can perform within the system.

## Project Details
The system has three types of roles assigned to users:
- **Admin**: Full control over user management and API access.
- **User**: Can create and manage their own APIs.
- **Moderator**: Oversees user activity and can provide feedback.

### Admin actions
- Can add users.
- Add API’s
- Remove Users.
- Update Users.
- Remove API
- Update API
- View API

### User actions
- Add API’s
- Update API’s.
- Map API’s to users.
- View API’s.

### moderator action
- View APIs
- Update User Roles
- Monitor User Activity
- Flag Content
- Provide Feedback

### Fulfills below conditions
1. Add user: Add user and map the role for the user and the API’s the user can access.
2. Remove user: Remove user and the mapping of the role and API’s the user can access.
3. Update user: Update the role and the mapping of the API’s the user can access.
4. Add API: Create new API. A database entry in the Django app and the access to it.
5. Remove API: Remove the API and if there are any users mapped to the API an error
should be thrown.
6. Update API: Update the API in the database.
7. View API: List the API’s mapped against the user.
8. For all the above 7 there has to be different API’s created in the Django Application and the web
interface should be displaying and taking the input for it.
9. If the user is not authorized for the role to access the API then 401 UnAuthorized Exception
should be returned.
  
## Installation Instructions
To set up this project locally, please follow these steps:
**Clone the repository**:
   ```bash
   git clone https://github.com/Omen-design/Role_based_access_control/tree/master
   cd RBAC-registration
1. Create a virtual environment:
 run these commands in terminal
  python -m venv venv
  source venv/bin/activate 

2.Install dependencies:
  Make sure you have Python installed. Then run:
  pip install -r requirements.txt

3. start a project
 run command 
 django-admin startproject registration

4. create a new app
  django-admin startapp app1

5. make migrations 
   python manage.py runserver

6. migrate them
   python manage.py migrate

7. create superuser of dbsqlite database
   python manage.py createsuperuser

8. Start the server
   python manage.py runserver

## Steps to Test RBAC Functionality
1. Identify User Roles and Permissions
2. Create Test User Accounts:
3. Define Test Scenarios:
    Develop various test scenarios to cover both positive and negative cases:
    Positive Scenarios: Verify that users with the correct roles can perform their designated actions (e.g., Admin can add users, Users can add APIs).
    Negative Scenarios: Ensure that users cannot perform actions outside their permissions(e.g., a User should not be able to remove another User).
4. Execute Test Cases:
   For each test scenario, perform the following actions:
   Admin Actions: Log in as an Admin and attempt to add, update, and remove users and APIs. Check if these actions succeed.
   User Actions: Log in as a User and attempt to add, update, and view their APIs. Verify that they can only map APIs to themselves.
   Moderator Actions: Log in as a Moderator and check if they can view APIs and monitor user activity without additional permissions.

5. Monitor Access Control
6. Check Error Handling
7. Validate Results
8. Document Findings
9. Review Security Policies

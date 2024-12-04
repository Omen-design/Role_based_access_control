# RBAC (registration)
- RBAC stands for Role based access control system

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
   git clone https://github.com/Omen-design/Role_based_access_control.git
   cd RBAC-registration
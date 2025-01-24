

# FlyOnTraveller

## Overview
This project is a comprehensive web application built using the Django framework, focused on property management. It includes features such as user authentication, property listings, search and filter functionalities, and a blog module.

## Features
- User Authentication and Profile Management
- Property Listings
- Search and Filter Properties
- Property Details
- Blog Posts
- Rich Text Editing
- Interactive Frontend
- About Section

## Technologies Used
- Backend: Python, Django
- Frontend: HTML, CSS, JavaScript, jQuery, AOS, Summernote
- Database: SQLite
- Deployment: Heroku

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/sihamfich/FlyOnTravelergit
   ```
2. Navigate to the project directory:
   ```sh
   cd your-repo
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Run the development server:
   ```sh
   python manage.py runserver
   ```

## API Documentation

### Base URL
```
https://flyone-27c553b7de46.herokuapp.com/api/
```

### Authentication

#### Register
**Endpoint**: `/rest-auth/registration/`  
**Method**: `POST`  
**Description**: Register a new user.  
**Request Body**:
```json
{
  "username": "string",
  "email": "string",
  "password1": "string",
  "password2": "string"
}
```
**Response**:
```json
{
  "key": "string"
}
```

#### Login
**Endpoint**: `/rest-auth/login/`  
**Method**: `POST`  
**Description**: Log in a user and obtain a token.  
**Request Body**:
```json
{
  "username": "string",
  "password": "string"
}
```
**Response**:
```json
{
  "key": "string"
}
```

### Property Listings

#### List Properties
**Endpoint**: `/Property/api/list/`  
**Method**: `GET`  
**Description**: Retrieve a list of all properties.  
**Response**:
```json
[
  {
    "id": "integer",
    "Name": "string",
    "Description": "string",
    "Price": "integer",
    "Location": "string",
    "Category": "string",
    "Main_Image": "url",
    "created_at": "datetime",
    "slug": "string"
  },
  ...
]
```

#### Create Property
**Endpoint**: `/Property/api/list/`  
**Method**: `POST`  
**Description**: Create a new property listing.  
**Request Body**:
```json
{
  "Name": "string",
  "Description": "string",
  "Price": "integer",
  "Location": "integer",
  "Category": "integer",
  "Main_Image": "file"
}
```
**Response**:
```json
{
  "id": "integer",
  "Name": "string",
  "Description": "string",
  "Price": "integer",
  "Location": "integer",
  "Category": "integer",
  "Main_Image": "url",
  "created_at": "datetime",
  "slug": "string"
}
```

#### Retrieve Property
**Endpoint**: `/Property/api/list/{id}/`  
**Method**: `GET`  
**Description**: Retrieve details of a specific property.  
**Response**:
```json
{
  "id": "integer",
  "Name": "string",
  "Description": "string",
  "Price": "integer",
  "Location": "integer",
  "Category": "integer",
  "Main_Image": "url",
  "created_at": "datetime",
  "slug": "string"
}
```

#### Update Property
**Endpoint**: `/Property/api/list/{id}/`  
**Method**: `PUT`  
**Description**: Update details of a specific property.  
**Request Body**:
```json
{
  "Name": "string",
  "Description": "string",
  "Price": "integer",
  "Location": "integer",
  "Category": "integer",
  "Main_Image": "file"
}
```
**Response**:
```json
{
  "id": "integer",
  "Name": "string",
  "Description": "string",
  "Price": "integer",
  "Location": "integer",
  "Category": "integer",
  "Main_Image": "url",
  "created_at": "datetime",
  "slug": "string"
}
```

#### Delete Property
**Endpoint**: `/Property/api/list/{id}/`  
**Method**: `DELETE`  
**Description**: Delete a specific property.  
**Response**:
```json
{
  "message": "Property deleted successfully."
}
```

### Blog Posts

#### List Blog Posts
**Endpoint**: `/Blog/api/list/`  
**Method**: `GET`  
**Description**: Retrieve a list of all blog posts.  
**Response**:
```json
[
  {
    "id": "integer",
    "Title": "string",
    "Description": "string",
    "Content": "string",
    "CreatedDate": "datetime",
    "Image": "url",
    "Category": "string",
    "Tags": ["string", ...],
    "slug": "string"
  },
  ...
]
```

#### Retrieve Blog Post
**Endpoint**: `/Blog/api/list/{id}/`  
**Method**: `GET`  
**Description**: Retrieve details of a specific blog post.  
**Response**:
```json
{
  "id": "integer",
  "Title": "string",
  "Description": "string",
  "Content": "string",
  "CreatedDate": "datetime",
  "Image": "url",
  "Category": "string",
  "Tags": ["string", ...],
  "slug": "string"
}
```

#### Search Blog Posts
**Endpoint**: `/Blog/api/list/search/{query}/`  
**Method**: `GET`  
**Description**: Search for blog posts by title or description.  
**Response**:
```json
[
  {
    "id": "integer",
    "Title": "string",
    "Description": "string",
    "Content": "string",
    "CreatedDate": "datetime",
    "Image": "url",
    "Category": "string",
    "Tags": ["string", ...],
    "slug": "string"
  },
  ...
]
```


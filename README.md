# Django Blog Application Experiment (to understand few things.)

## Overview

This is a simple blog application built with Django. The application allows users to log in using their email, mobile number, and a PIN. Registration is handled exclusively by the super admin via the Django admin panel. Users can create and manage their own blog posts, while the super admin has additional capabilities.

  ### Requirements

  1. **User Login and Registration**: Develop a Django blog application with a login feature for users, where registration is handled solely by the admin via the Django admin panel. The login form should have three fields: email, mobile, and a PIN (digits only, saved in plain text).
  2. **Blog Post Structure**: Blog posts should include the author’s email, a timestamp, and a heading with a character limit of 150. An optional 4-line summary field (up to 400 characters) should be placed between the heading and the post content. If the summary is null, it won’t appear in the production front end.
  3. **Blog Post Ordering**: The blog posts should be displayed in date order on the front end.
  4. **Admin Panel Capabilities**: In the Django admin panel, provide superusers with a section to view all authors, including the titles and URLs of the posts each author has created. Other users should only be able to view, edit, or delete their own posts.
  5. **Front-end Styling**: Ensure the login page and blog posts on the front end are styled using Bootstrap 5.0 components for a visually appealing interface.
  6. **User Roles and Management**: The superuser is the only role with full management capabilities over users and blog posts. Other users can only manage their own posts.
  7. **Logging and Tracking**: Implement logging and tracking for admin actions, including the creation of posts and users.
  8. **Future Enhancements**: No immediate plans for future enhancements like password encryption or user registration directly from the front end.
  9. **Super Admin Capabilities**: Super admin can add users : email, mobile and PIN in django admin. These users can then login from front using same access details to post blogs from admin

## Features

- **User Authentication:**
  - Users log in using their email, mobile number, and PIN.
  - Registration is managed by the super admin through the Django admin panel.

- **Blog Posts:**
  - Each post includes an author's email, a date-time stamp, a heading (up to 150 characters), and an optional summary (up to 400 characters).
  - If the summary is null, it will not appear in the front-end display.
  - Blog posts are ordered by date on the front end.

- **Admin Capabilities:**
  - The super admin can add users with email, mobile, and PIN via the Django admin panel.
  - The super admin can view all authors and see how many posts each author has created, including the titles and URLs of these posts.
  - Regular users can only view, edit, or delete their own posts.

- **Styling:**
  - The application uses Bootstrap 5 for a modern and responsive UI.

- **Logging:**
  - Admin actions, such as creating posts or users, are logged for tracking purposes.

## Setup Instructions

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/django-blog-app.git
   cd django-blog-app

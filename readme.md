# 📘 ModernBlog – A Full-Stack Django Blogging Platform

ModernBlog is a **production-ready blogging platform** built using **Django**, designed for **multi-author publishing**, **role-based access control**, **search**, **pagination**, **newsletter subscription**, and a **custom dashboard**.

This project follows **real-world Django architecture**, clean code practices, and scalable design — suitable for startups, portfolios, and SaaS-based content platforms.

---

## 🚀 Project Overview

ModernBlog allows:

- 👥 **Readers** to browse blogs, search content, and subscribe to newsletters  
- ✍️ **Authors** to write and manage their own blogs  
- 🛡 **Admins** to review, publish, edit, and delete posts  
- ⚙️ **Superusers** to manage everything from the Django Admin Panel  

The system cleanly separates **authentication**, **authorization**, and **content workflows**.

---

## ✨ Features

### 🔐 Authentication & Authorization
- User Registration & Login
- Session-based authentication
- Role-based access using Django Groups
- Permissions controlled via decorators and template logic

### 📝 Blog System
- Create, edit, delete blog posts
- Unique slug generation using `slugify`
- Draft & Published workflow
- Featured posts
- Category-wise filtering

### 📂 Categories
- Dynamic category navigation (via context processor)
- Category listing pages
- Footer category links redirect to category blogs

### 🔍 Search
- Search across:
  - Title
  - Short description
  - Content
- Clean UI for search results

### 📄 Pagination
- Page-based pagination
- Works with category and search pages
- SEO-friendly URLs

### 💬 Comments
- Authenticated users can comment
- Comment count shown per blog
- Human-readable timestamps (`timesince`)

### 📩 Newsletter Subscription
- Email validation
- Confirmation email sent
- Subscribe button hides after successful subscription
- Logged-in user email auto-filled

### 🧑‍💻 Custom Dashboard
- Sidebar-based UI
- Manage categories and posts
- Role-restricted access
- Clean admin-like experience without using Django Admin

---

## 🛠 Tech Stack

**Backend**
- Python 3.10+
- Django 5.x
- SQLite (development)
- PostgreSQL-ready (production)

**Frontend**
- HTML5
- Bootstrap 5
- Font Awesome
- Django Templates
- Crispy Forms + Bootstrap5

**Other Tools**
- Django ORM
- Django Auth System
- Email (SMTP)
- Context Processors
- Django Paginator
- Git & GitHub

---

# 📘 ModernBlog – A Full-Stack Django Blogging Platform

ModernBlog is a **production-ready blogging platform** built using **Django**, designed for **multi-author publishing**, **role-based access control**, **search**, **pagination**, **newsletter subscription**, and a **custom dashboard**.

This project follows **real-world Django architecture**, clean code practices, and scalable design — suitable for startups, portfolios, and SaaS-based content platforms.

---

## 🚀 Project Overview

ModernBlog allows:

- 👥 **Readers** to browse blogs, search content, and subscribe to newsletters  
- ✍️ **Authors** to write and manage their own blogs  
- 🛡 **Admins** to review, publish, edit, and delete posts  
- ⚙️ **Superusers** to manage everything from the Django Admin Panel  

The system cleanly separates **authentication**, **authorization**, and **content workflows**.

---

## ✨ Features

### 🔐 Authentication & Authorization
- User Registration & Login
- Session-based authentication
- Role-based access using Django Groups
- Permissions controlled via decorators and template logic

### 📝 Blog System
- Create, edit, delete blog posts
- Unique slug generation using `slugify`
- Draft & Published workflow
- Featured posts
- Category-wise filtering

### 📂 Categories
- Dynamic category navigation (via context processor)
- Category listing pages
- Footer category links redirect to category blogs

### 🔍 Search
- Search across:
  - Title
  - Short description
  - Content
- Clean UI for search results

### 📄 Pagination
- Page-based pagination
- Works with category and search pages
- SEO-friendly URLs

### 💬 Comments
- Authenticated users can comment
- Comment count shown per blog
- Human-readable timestamps (`timesince`)

### 📩 Newsletter Subscription
- Email validation
- Confirmation email sent
- Subscribe button hides after successful subscription
- Logged-in user email auto-filled

### 🧑‍💻 Custom Dashboard
- Sidebar-based UI
- Manage categories and posts
- Role-restricted access
- Clean admin-like experience without using Django Admin

---

## 🛠 Tech Stack

**Backend**
- Python 3.10+
- Django 5.x
- SQLite (development)
- PostgreSQL-ready (production)

**Frontend**
- HTML5
- Bootstrap 5
- Font Awesome
- Django Templates
- Crispy Forms + Bootstrap5

**Other Tools**
- Django ORM
- Django Auth System
- Email (SMTP)
- Context Processors
- Django Paginator
- Git & GitHub

---

## 🔑 User Roles & Permissions

| Role        | Permissions |
|------------|-------------|
| Superuser  | Full access (Admin + Dashboard) |
| Author     | Create and manage own posts |
| User       | Read, comment, subscribe |
| Guest      | Read-only |

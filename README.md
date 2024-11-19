# Python Reflex Learning Project

A experimental web application built with Python Reflex framework to explorer and learn its features and capabilities.

## Overview

This project is a simple frontend and its integration capabilities with third-party services.

It currently implements basic page routing and user authentication built with [Clerk](https://clerk.com/).

## Key Features

- Page Routing
- User Authentication
  - Clerk SDK integration
- Wrapping React components
  - Framer Motion (https://motion.dev)
  - React Icons (https://react-icons.github.io/react-icons/)
  - Spline (https://spline.design)

## Setup

1. Install dependencies

```bash
uv install
```

2. Configure environment variables

```bash
cp .env.example .env
# add clerk publishable key and secret key to .env
```

3. Run the application

```bash
source .venv/bin/activate
reflex run
```

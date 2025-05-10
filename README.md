# IT_Asset_managemet_System

A modern, web-based IT Asset Management System designed to help organizations efficiently track, manage, and maintain their IT assets. The system provides a comprehensive solution for asset lifecycle management, maintenance scheduling, and reporting.

## Features

  => Comprehensive Asset Tracking
  - Track all IT assets with detailed information
  - Manage asset status (Available, In Use, Maintenance, Decommissioned)
  - Categorize assets by type (Laptops, Desktops, Servers, etc.)

  => User Authentication & Authorization
  - Secure login system
  - Role-based access control
  - Admin dashboard for system management

  => Maintenance Management
  - Schedule and track maintenance activities
  - Record maintenance history
  - Set maintenance reminders
  - Track warranty information

  => Reporting & Analytics
  - Generate asset reports
  - View asset utilization statistics
  - Track maintenance history
  - Export reports in various formats

 => Asset Assignment
  - Assign assets to users
  - Track asset assignments
  - Record assignment history
  - Monitor asset usage

## Tech Stack

- **Frontend**: React with Vite
- **Backend**: Python FastAPI
- **Database**: PostgreSQL
- **Authentication**: JWT
- **UI Framework**: Material-UI
- **State Management**: Redux Toolkit

## Getting Started

### Prerequisites

- Node.js (v18 or higher)
- Python 3.9+
- PostgreSQL 13+
- npm or yarn

### Installation

1. Clone the repository
2. Install backend dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```
3. Install frontend dependencies:
   ```bash
   cd frontend
   npm install
   ```
4. Set up environment variables:
   - Create `.env` file in backend directory
   - Configure database connection
   - Set up JWT secret key
   - Configure frontend environment variables

### Running the Application

1. Start the backend server:
   ```bash
   cd backend
   uvicorn app.main:app --reload
   ```
2. Start the frontend development server:
   ```bash
   cd frontend
   npm run dev
   ```

## Project Structure

```
asset-management-clean/
├── backend/           # FastAPI backend server
│   ├── app/          # Application code
│   ├── config/       # Configuration files
│   └── tests/        # Test files
├── frontend/          # React frontend application
│   ├── src/          # Source code
│   ├── public/       # Static assets
│   └── vite.config.js # Vite configuration
└── docs/             # Documentation
```

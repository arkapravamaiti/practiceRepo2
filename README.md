# Employee Search API

A comprehensive employee and document search system that integrates **Python**, **SQL**, **Elasticsearch**, and **GitHub** to provide powerful search capabilities for organizational data.

## 🚀 Project Overview

This mini-project demonstrates how to connect multiple technologies:
- **FastAPI** - Modern Python web framework for building APIs
- **SQL Database** - Store structured employee and document data
- **Elasticsearch** - Enable fast, intelligent search with semantic capabilities
- **GitHub Integration** - Version control and collaborative development

## 📋 What You Need to Provide

### 1. System Requirements
- **Python 3.8+** installed on your system
- **Git** for version control
- **Code Editor** (VS Code recommended)

### 2. Database Setup
Choose one of the following database options:

#### Option A: SQLite (Easiest - for development)
```bash
# No additional installation required
# Database file will be created automatically
```

#### Option B: PostgreSQL (Recommended for production)
```bash
# Install PostgreSQL
# Windows: Download from https://www.postgresql.org/download/windows/
# macOS: brew install postgresql
# Ubuntu: sudo apt-get install postgresql postgresql-contrib

# Create database and user
sudo -u postgres psql
CREATE DATABASE employee_db;
CREATE USER your_username WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE employee_db TO your_username;
```

#### Option C: MySQL (Alternative)
```bash
# Install MySQL
# Windows: Download from https://dev.mysql.com/downloads/mysql/
# macOS: brew install mysql
# Ubuntu: sudo apt-get install mysql-server

# Create database and user
mysql -u root -p
CREATE DATABASE employee_db;
CREATE USER 'your_username'@'localhost' IDENTIFIED BY 'your_password';
GRANT ALL PRIVILEGES ON employee_db.* TO 'your_username'@'localhost';
```

### 3. Elasticsearch Setup
Choose one of the following Elasticsearch options:

#### Option A: Elastic Cloud (Recommended)
1. Sign up at [Elastic Cloud](https://cloud.elastic.co/)
2. Create a new deployment
3. Choose your region (closest to your location)
4. Note down the **Cloud ID** and **Endpoint URL**
5. Create an **API Key** from the deployment management page

#### Option B: Local Elasticsearch (for development)
```bash
# Download and install Elasticsearch
# https://www.elastic.co/downloads/elasticsearch

# Start Elasticsearch service
# Windows: bin\elasticsearch.bat
# macOS/Linux: bin/elasticsearch

# Default URL: http://localhost:9200
# Default credentials: elastic/changeme
```

### 4. GitHub Setup
1. Create a **GitHub account** if you don't have one
2. Create a **new repository** for this project
3. Generate a **Personal Access Token** (Settings → Developer settings → Personal access tokens)
4. Clone the repository to your local machine

### 5. Environment Configuration
Create a `.env` file in the project root with your specific values:

```env
# Database Configuration
DATABASE_URL=postgresql://username:password@localhost/employee_db
# OR for SQLite: DATABASE_URL=sqlite:///./employees.db

# Elasticsearch Configuration
ELASTIC_URL=https://your-deployment-id.es.region.gcp.elastic.cloud:443
ELASTIC_API_KEY=your_api_key_from_elastic_cloud

# GitHub Configuration (optional)
GITHUB_TOKEN=your_github_personal_access_token
GITHUB_REPO=your-username/employee-search-api
```

## 🛠️ Installation & Setup

### Step 1: Clone and Setup Project
```bash
# Clone the repository
git clone https://github.com/your-username/employee-search-api.git
cd employee-search-api

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Configure Environment
```bash
# Copy environment template
cp .env.example .env

# Edit .env file with your actual values
# Use your preferred text editor
code .env  # VS Code
# or
nano .env  # Terminal editor
```

### Step 3: Initialize Database and Search
```bash
# Run data synchronization script
python -m app.sync_data

# This will:
# - Create database tables
# - Add sample data
# - Create Elasticsearch indices
# - Sync data to Elasticsearch
```

### Step 4: Start the Application
```bash
# Start the FastAPI server
python -m app.main
# or
uvicorn app.main:app --reload

# Application will be available at:
# http://localhost:8000
```

## 📊 Data You Need to Provide

### Employee Data
Replace the sample data in `app/sync_data.py` with your actual employee information:

```python
employees = [
    Employee(
        name="Your Employee Name",
        department="Their Department",
        role="Their Job Role",
        email="their.email@company.com"
    ),
    # Add more employees...
]
```

### Document Data
Add your company documents, policies, or knowledge base content:

```python
docs = [
    Document(
        title="Employee Handbook",
        text="Your actual handbook content..."
    ),
    Document(
        title="IT Security Policy",
        text="Your security policy content..."
    ),
    # Add more documents...
]
```

### Data Import Options
You can import data from various sources:

#### From CSV files:
```python
import pandas as pd

# Import employees from CSV
df = pd.read_csv('employees.csv')
for _, row in df.iterrows():
    Employee(
        name=row['name'],
        department=row['department'],
        role=row['role'],
        email=row['email']
    )
```

#### From Excel files:
```python
df = pd.read_excel('employees.xlsx')
# Process similar to CSV
```

#### From existing databases:
```python
# Connect to legacy database and migrate data
# Implementation depends on your source database
```

## 🔧 API Endpoints

Once running, your API will provide these endpoints:

### Health Check
- `GET /` - Basic health check
- `GET /health` - Detailed health status

### Employee Management
- `GET /employees` - List all employees (with pagination)
- `GET /employees/{id}` - Get specific employee
- `GET /search/employees?q=search_term` - Search employees

### Document Management
- `GET /documents` - List all documents (with pagination)
- `GET /search/documents?q=search_term` - Search documents

### API Documentation
- `GET /docs` - Interactive API documentation (Swagger UI)
- `GET /redoc` - Alternative API documentation

## 🔍 Testing the Search

### Test Employee Search
```bash
# Search for employees by name
curl "http://localhost:8000/search/employees?q=Alice"

# Search with department filter
curl "http://localhost:8000/search/employees?q=manager&department=HR"
```

### Test Document Search
```bash
# Search documents
curl "http://localhost:8000/search/documents?q=remote work policy"
```

## 📁 Project Structure

```
employee-search-api/
│
├── app/
│   ├── __init__.py           # Python package initialization
│   ├── database.py           # Database configuration and connection
│   ├── models.py             # SQLAlchemy data models
│   ├── es_utils.py           # Elasticsearch utilities and search functions
│   ├── sync_data.py          # Data synchronization between SQL and Elasticsearch
│   └── main.py               # FastAPI application and API endpoints
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (create from .env.example)
├── .env.example              # Environment variables template
├── .gitignore                # Git ignore file
└── README.md                 # This file
```

## 🔒 Security Considerations

### Production Deployment
1. **Environment Variables**: Never commit `.env` file to version control
2. **Database Security**: Use strong passwords and limit database access
3. **API Security**: Implement authentication and rate limiting
4. **HTTPS**: Use SSL certificates in production
5. **Elasticsearch Security**: Enable authentication and encryption

### GitHub Integration Security
1. **Personal Access Tokens**: Use tokens with minimal required permissions
2. **Repository Access**: Keep sensitive data in private repositories
3. **Secrets Management**: Use GitHub Secrets for CI/CD pipelines

## 🚀 Deployment Options

### Local Development
```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### Production Deployment
```bash
# Using Gunicorn (recommended for production)
pip install gunicorn
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Docker Deployment
```dockerfile
# Create Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "app.main:app", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "--bind", "0.0.0.0:8000"]
```

### Cloud Deployment
- **Heroku**: Easy deployment with buildpacks
- **AWS**: EC2, ECS, or Lambda deployment
- **Google Cloud**: App Engine or Cloud Run
- **Azure**: App Service or Container Instances

## 🔧 Customization Options

### Adding New Fields
1. Update `models.py` to add new database fields
2. Update `es_utils.py` to include fields in search index
3. Update `sync_data.py` to handle new data
4. Update API endpoints in `main.py`

### Advanced Search Features
1. **Autocomplete**: Implement search suggestions
2. **Faceted Search**: Add filters and aggregations
3. **Geolocation**: Add location-based search
4. **Machine Learning**: Implement search result ranking

### Frontend Integration
Create a web interface using:
- **React**: Modern frontend framework
- **Vue.js**: Progressive framework
- **Angular**: Full-featured framework
- **HTML/CSS/JavaScript**: Simple web interface

## 📝 Troubleshooting

### Common Issues

#### Database Connection Errors
```bash
# Check database service is running
# Verify connection string in .env
# Ensure database exists and user has permissions
```

#### Elasticsearch Connection Errors
```bash
# Verify Elasticsearch is running
# Check ELASTIC_URL and credentials
# Test connection: curl -X GET "localhost:9200"
```

#### Import Errors
```bash
# Ensure virtual environment is activated
# Install missing dependencies: pip install -r requirements.txt
# Check Python path and module structure
```

### Debugging Tips
1. **Check Logs**: Application logs provide detailed error information
2. **Test Connections**: Use health check endpoints to verify service status
3. **Validate Data**: Ensure your sample data matches the model structure
4. **Environment Variables**: Double-check all configuration values

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and commit: `git commit -m 'Add feature'`
4. Push to branch: `git push origin feature-name`
5. Submit a pull request

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

If you encounter issues:

1. **Check Documentation**: Review this README and code comments
2. **Search Issues**: Look for similar problems in GitHub issues
3. **Create Issue**: Submit a new issue with detailed information
4. **Community Support**: Ask questions in discussions section

## 🎯 Next Steps

After getting the basic system running, consider:

1. **Add Authentication**: Implement user login and access control
2. **Create Frontend**: Build a web interface for search
3. **Advanced Analytics**: Add search analytics and reporting
4. **Performance Optimization**: Implement caching and indexing strategies
5. **Monitoring**: Add logging, metrics, and alerting
6. **Testing**: Create comprehensive test suite
7. **Documentation**: Generate API documentation and user guides

## 🌟 Features to Implement

- [ ] User authentication and authorization
- [ ] Advanced search filters and sorting
- [ ] Search result highlighting
- [ ] Autocomplete and search suggestions
- [ ] File upload and indexing
- [ ] Real-time data synchronization
- [ ] Search analytics and reporting
- [ ] Mobile-responsive web interface
- [ ] Integration with external systems
- [ ] Backup and disaster recovery

---

**Happy Searching! 🔍**
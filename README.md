# LinkedIn Jobs Scraper

This is a Python project for collecting job data from LinkedIn using the `linkedin-jobs-scraper` library and Selenium.

## Prerequisites

Before you begin, ensure you have Python and pip installed on your system. If not, you can download Python from [python.org](https://www.python.org/downloads/) and follow the installation instructions for your operating system.

## Installation Steps

### 1. Clone the Repository

Clone the repository from GitHub using the following command:

<pre>git clone https://github.com/LuthfiAjax/linkedin-jobs-scrapping.git</pre>

### 2. Navigate to the Project Directory

Change to the project directory you just cloned:

<pre>cd linkedin-jobs-scrapping</pre>

### 3. Create and Activate a Virtual Environment

Create a new virtual environment for this project:

<pre>python -m venv myenv</pre>

Activate the virtual environment:

- **For macOS/Linux:**

<pre>source myenv/bin/activate</pre>

- **For Windows:**

<pre>myenv\Scripts\activate</pre>

### 4. Install Dependencies

Install all the required dependencies using `pip`:

<pre>pip install -r requirements.txt</pre>

### 5. Configure and Run the Scraper

Before running the scraper, make sure to configure `linkedin_scraper.py` as needed. Then, run the Python file to start the scraping:

<pre>python linkedin_scraper.py</pre>

## Explanation

- `linkedin_scraper.py` is the main file that runs the scraping process. Ensure you configure settings within it according to your needs.

## Troubleshooting

If you encounter issues while running the scraper, ensure:

1. Your virtual environment is activated.
2. All dependencies are correctly installed.
3. Your Python and pip versions are compatible with the project's requirements.

If you still face difficulties, check the error logs for more details or visit the [GitHub issues page](https://github.com/LuthfiAjax/linkedin-jobs-scrapping/issues) for assistance.

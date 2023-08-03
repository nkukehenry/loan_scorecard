import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Function to create a database connection
def get_database_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

# Function to calculate SMS score
def calculate_sms_score(sms_data):
    # Your SMS scoring logic here
    pass

# Function to calculate phone type score
def calculate_phone_type_score(phone_type_data):
    # Your phone type scoring logic here
    pass

# Function to calculate loan score
def calculate_loan_score(loan_data):
    # Your loan scoring logic here
    pass

# Function to calculate overall score
def calculate_overall_score(sms_score, phone_type_score, loan_score):
    # Calculate overall score with more weight on loan_score if it exists
    # If loan_score is None, give more weight to sms_score and phone_type_score
    overall_score = (loan_score if loan_score is not None else 0.7 * sms_score + 0.3 * phone_type_score)
    return overall_score

# Function to get user-related data from the database
def get_user_data_from_db(user_id):
    connection = get_database_connection()
    cursor = connection.cursor()

    # Fetch SMS data for the given user
    cursor.execute("SELECT sms_data FROM sms_table WHERE user_id = %s", (user_id,))
    sms_data = cursor.fetchone()[0]

    # Fetch phone type data for the given user
    cursor.execute("SELECT phone_type_data FROM phone_type_table WHERE user_id = %s", (user_id,))
    phone_type_data = cursor.fetchone()[0]

    # Fetch loan data for the given user
    cursor.execute("SELECT loan_data FROM loan_table WHERE user_id = %s", (user_id,))
    loan_data = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return sms_data, phone_type_data, loan_data

# Main function to calculate scores and return overall score
def calculate_credit_score(user_id):
    # Fetch user-related data from the database
    sms_data, phone_type_data, loan_data = get_user_data_from_db(user_id)

    # Calculate individual scores
    sms_score = calculate_sms_score(sms_data)
    phone_type_score = calculate_phone_type_score(phone_type_data)
    loan_score = calculate_loan_score(loan_data) if loan_data else None

    # Calculate overall score
    overall_score = calculate_overall_score(sms_score, phone_type_score, loan_score)

    return overall_score

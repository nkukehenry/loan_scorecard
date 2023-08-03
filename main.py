import os
from credit_score import calculate_credit_score



if __name__ == "__main__":
    # User ID
    user_id = "1"

    # Calculate overall credit score for the given user ID
    overall_score = calculate_credit_score(user_id)

    # Print the overall score
    print("Overall Credit Score for User ID {}: {}".format(user_id, overall_score))



from constants import NUMBER_OF_FRAGMENTS
from utilities import display_matrix,numerical_form_of,\
        get_scoring_matrix, pointwise_product, list_as_precedence_matrix,\
        sum_of_upper_triangle



'''
User was queried for response to scrambling test of size NUMBER_OF_FRAGMENTS,
then student gave response, then evaluation matrix was shown, then
student's score was shown as a percentage.
'''

# (Entry): Student queried for response to scrambling test
# of size NUMBER_OF_FRAGMENTS, then student gave response response_list

print("\n\nStudent response in {0} integers, separated by commas: ".
      format(NUMBER_OF_FRAGMENTS))
response_ = raw_input()######taking response as input
response_list = response_.split(',')###skip the blank

# (Score): The student's score is on the console, rounded to 1 decimal

student_response_matrix = list_as_precedence_matrix(response_list)  ### intializing the function to other variable
scoring_matrix = get_scoring_matrix() ### intializing the function to other variable
student_score_matrix = pointwise_product(student_response_matrix, scoring_matrix) ## usingthe function pointwise_product function to compute the matrix multiplication of student_response_matrix andscoring_matrix
student_score = 100 * (sum_of_upper_triangle(student_score_matrix)) / (sum_of_upper_triangle(scoring_matrix)) ###then compute the percentage by the calculating the value is matrix
print("Your score is {0}%".format(str(round(student_score, 1))))#####display the result


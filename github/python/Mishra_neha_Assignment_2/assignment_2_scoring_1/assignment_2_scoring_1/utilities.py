from constants import NUMBER_OF_FRAGMENTS ###importing the variable from other file

##### Code for creating function display_matrix ##########
def display_matrix(a_matrix):
    for i in range(0, NUMBER_OF_FRAGMENTS): #### for 0 to number of fragments
        print(str(a_matrix[i])) #### display the corresponding matrix

##### Code for creating function get_scoring_matrix ##########

def get_scoring_matrix():
    scoring_matrix = []
    scoring_file = open("Scoring Matrix")###opening the scoring matrix the read file line by line
    i=0
    while( i<=NUMBER_OF_FRAGMENTS):
        content_of_line = scoring_file.readline()
        content_list = content_of_line.split('   ')##for blankspaces
        numerical_form = numerical_form_of(content_list[1:])
        scoring_matrix.append(numerical_form)
        i += 1
    del scoring_matrix[0]
    return scoring_matrix


##### Code for creating function numerical_form_of ##########
def numerical_form_of(a_list):
    return [int(a_list[i]) for i in range(len(a_list))] #### return the list with the corresponding integers


##### Code for creating function pointwise_product ##########
def pointwise_product(a_matrix, a_second_matrix): ### define function
    m = [[0 for _ in range(7)] for _ in range(7)]## intializing the matrix to null value
    for i in range(0, NUMBER_OF_FRAGMENTS):  ## for every i(row) starting from 0 to number_fragments
        for j in range(0, NUMBER_OF_FRAGMENTS): ##for every i(column) starting from 0 to number_fragments
            m[i][j] = (a_matrix[i][j] * a_second_matrix[i][j])  ## m[i][j]= multiplication of two matrix (a_matrix and a_second_matrix)
    return m

########### Code for creating function list_as_precedence_matrix (student response is calculated)#########
def list_as_precedence_matrix(a_response):  ### define function
    return_matrix = [[0 for row in range(NUMBER_OF_FRAGMENTS)] ## intializing the matrix to null value
                     for column in range(NUMBER_OF_FRAGMENTS)]

    for index_of_first in range(len(a_response) - 1): ### for loop  index_of_first till length of (a_response-1)
        for index_of_second in range(index_of_first + 1, len(a_response)):
            value1, value2 = int(a_response[index_of_first]), int(a_response[index_of_second])
            if value1 < value2: ## if the value1 < value 2 fro eg value1=3 and value2=4
                return_matrix[value1 - 1][value2 - 1] = 1 ##return_matrix (the index of (value1 -1)(value2 -1)) will be initilaize to 1
    return return_matrix ###then return return_matrix

############ Code for creating function sum_of _upper_triangle ##############
def sum_of_upper_triangle(a_matrix):
    sum_returned = 0   ##### initializing to zero so that it doesnot any garabage value
    for row in range(NUMBER_OF_FRAGMENTS): ### for loop for getting into row from 0 to number of fragments
        for column in range(row + 1, NUMBER_OF_FRAGMENTS): ###  for loop for getting into column starting row+1 to number_of fragments
            sum_returned += a_matrix[row][column] ####### sum of a_matrix is assign to sum_returned variable
    return (sum_returned) ### return the value

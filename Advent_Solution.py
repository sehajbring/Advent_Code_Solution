# Sehajveer Bring
import os
# This method reads the file and converts it into a list of integers
def readFileToList(file_path):
    num_list = []
    file_read = open(file_path, "r+").readlines()
    for i in file_read:
        temp = []
        for element in i.strip().split(" "):
            temp.append(int(element))
        num_list.append(temp)
    return num_list


# This method checks if the given array of numbers is safe or not by checking if it is in ascending or descending order 
#   and if the difference between adjacent numbers is between 1 and 3 inclusive
def checkSafety(arr):
    assending = True
    descending = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            assending = False

        if arr[i] < arr[i+1]:
            descending = False
        if abs(arr[i] - arr[i+1]) > 3 or abs(arr[i] - arr[i+1]) < 1:
            return False
    return assending or descending


# This is the main method that reads the file, checks for safe reports and prints the results
if __name__ == "__main__":
    num_list = []
    dir_path = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(dir_path, "List_of_Numbers\\Numbers_File.txt")
    num_list = readFileToList(file_path)

    total_safe_reports = 0
    for i in num_list:
        if checkSafety(i):
            total_safe_reports += 1

    total_safe_reports_part_2 = 0
    for i in num_list:
        for j in range(len(num_list)):
            if checkSafety(i[:j] + i[j+1:]):
                total_safe_reports_part_2 += 1
                break

    print("The total number of safe reports is:", total_safe_reports)
    print("The total number of safe reports after removing one level is:", total_safe_reports_part_2)
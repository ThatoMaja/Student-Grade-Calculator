import pandas as pd 
import tkinter as tk 
from tkinter import filedialog, messagebox 
import threading 
import unittest 
from io import StringIO 
""" 
Overall grade calculation for the students in terms of thee assessment weighting. 
csv_data is a parameter which is a path to the SCV file that has the student grades. 
""" 
#This function calculates the overall grades for each student according to their 
assessment marks. 
def calculate_grades(csv_data): 
grades_data = pd.read_csv(csv_data) #This line of code loads the CSV file and reads 
the CSV data into the dataframe 
required_columns = ['Module Name', 'Quiz', 'Project', 'Final Exam', 'Practical'] #This 
defines and validates the data to ensure that all the columns that are required are there. 
if not all(column in grades_data.columns for column in required_columns): 
raise ValueError(f"The following columns: {required_columns} have to be present in 
the CSV file)") 
Page | 4  
Page | 5  
 
         
    if grades_data[required_columns[1:]].isnull().any().any(): #Validates the data in terms 
of ensuring thhat there are no missing values in the assessment table/columns 
        raise ValueError("The assessment columns in the CSV file have missing values.") 
    
    #States the weights for each type of assessment     
    weights = { 
        'Quiz': 0.10, 
        'Project': 0.20, 
        'Final Exam': 0.50, 
        'Practical': 0.20 
        } 
     
    #Calculates the overall marks according to the weighting that was provided 
    grades_data['Overall Grade'] = ( 
        grades_data['Quiz'] * weights['Quiz'] + 
        grades_data['Project'] * weights['Project'] + 
        grades_data['Final Exam'] * weights['Final Exam'] + 
        grades_data['Practical'] * weights['Practical'] 
        ) 
 
    return  grades_data 
 
Page | 6  
 
#This function handles the process regarding the files that have to be uploaded 
def upload_csv_file(): 
    csv_data = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")]) #This line 
opens the file dialog in order to select the CSV file 
    if csv_data: 
        try: 
            global calculated_grades_data  
            thread = threading.Thread(target=upload_and_calculate_grades, 
args=(csv_data,)) #A new thread is created to upload and calculate grades 
            thread.start() 
        except Exception as e: 
             
            messagebox.showerror("Error", str(e)) #Show an error message if there's an 
invalid attempt 
 
#This function uploads and calculates the grades in a seperate thread             
def upload_and_calculate_grades(csv_data): 
    global calculated_grades_data 
    try: 
        calculated_grades_data = calculate_grades(csv_data) #Calculate the grades from 
the CSV file data 
        csv_data_entry.delete(0, tk.END) #Update the CSV file file path entry into our GUI 
        csv_data_entry.insert(0, csv_data) 
Page | 7  
 
        messagebox.showinfo("Success", "CSV file was uploaded and grades are 
calculated successfully!") #Display a success message to confirm to the user that the file 
has been uploaded and processed  
    except Exception as e: 
        messagebox.showerror("Error", str(e)) #Display error message if invalid entry 
 
#This function displays the calculated grades via the text widget 
def display_grades(): 
    if calculated_grades_data is not None: 
        grades_text.delete("1.0", tk.END) #Clears the text widget 
        grades_text.insert(tk.END, calculated_grades_data.to_string(index=False)) 
#Inserts the calculated grades inside the text widget 
    else: 
    
        messagebox.showwarning("Warning", "You have to load a CSV file first!") #This will 
display if the CSV file has not been loaded 
 
root = tk.Tk() #Initializes main window 
root.title("Eduvos Student Grade Calculator") 
 
#Widgets for the GUI   
csv_data_label = tk.Label(root, text="CSV file path:") 
csv_data_label.grid(row=0, column=0, padx=10, pady=10, sticky="e") 
 
csv_data_entry = tk.Entry(root, width=50) 
csv_data_entry.grid(row=0, column=1, padx=10, pady=10) 
load_button = tk.Button(root, text="Load CSV File", command=upload_csv_file) 
load_button.grid(row=0, column=2, padx=10, pady=10) 
calculate_button = tk.Button(root, text="Calculate Grades", command=display_grades) 
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10) 
grades_text = tk.Text(root, width=80, height=20) 
grades_text.grid(row=2, column=0, columnspan=3, padx=10, pady=10) 
root.mainloop() #Begins the mainloop event 
#UNIT TESTING 
import pandas as pd 
import unittest 
from io import StringIO 
from TestGradeCalculation import calculate_grades 
class TestGradeCalculation(unittest.TestCase): 
Page | 8  
Page | 9  
 
     
    def setUp(self): 
        self.data = StringIO("""Module Name, Quiz, Project, Final Exam, Practical  
                             Mathematics for Programing, 80, 90, 85, 95 
                             Python Programming, 70, 85, 80, 90 
                             Research Studies, 75, 80, 70, 85 
                             IT and Communication, 95, 78, 80, 82 
                             """) 
        self.df = pd.read_csv(self.data) 
         
    def test_grade_calculation(self): 
         
        self.df.to.csv('test_grades.csv', index=False) 
 
        calculated_grades_data = calculate_grades('test_grades.csv') 
         
        expected_grades = [ 
            80 * 0.10 + 90 * 0.20 + 85 * 0.50 + 95 * 0.20, 
            70 * 0.10 + 85 * 0.20 + 80 * 0.50 + 90 * 0.20, 
            75 * 0.10 + 80 * 0.20 + 70 * 0.50 + 85 * 0.20, 
            95 * 0.10 + 78 * 0.20 + 80 * 0.50 + 82 * 0.20] 
         
        #Check whether the calculated overall grades are correct 
Page | 10  
 
        for i, expected_grade in enumerate(expected_grades): 
             
            self.assertAlmostEqual(calculated_grades_data.loc[i, 'Overall Grade'], 
expected_grade) 
     
    def test_missing_columns(self): 
        #Data with missing columns 
         
        data = StringIO("""Module Name, Quiz, Project, Final Exam, Practical  
                             Mathematics for Programing, 80, 90, 85, 
                             Python Programming, 70, 85, 80,  
                             Research Studies, 75, 80, 70,  
                             IT and Communication, 95, 78, 80,  
                             """) 
        df = pd.read_csv(data) 
    df.to_csv('test_grades_missing_columns.csv', index=False) 
     
        with self.assertRaises(ValueError): 
        calculate_grades('test_grades_missing_columns.csv') 
         
    def test_missing_values(self): 
        #Data with missing values 
        data = StringIO("""Module Name, Quiz, Project, Final Exam, Practical  
Page | 11  
 
                             Mathematics for Programing, 80, 90, 85, 
                             Python Programming, 70, 80, 90 
                             Research Studies, 75, 80, 70, 85 
                             IT and Communication, 95, 78, 80, 82 
                             """) 
        df.to_csv('test_grades_missing_values.csv', index=False) 
         
        with self.assertRaises(ValueError): 
            calculate_grades('test_grades_missing_values.csv') 
             
if __name__ == '__main__': 
    unittest.main(argv=['first-arg-is-ignored'], exit=False) 
 

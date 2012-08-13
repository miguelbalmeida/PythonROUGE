import PythonROUGE

guess_summary_file = 'Example/Guess_Summ_1.txt'
ref_summary_file_list = ['Example/Ref_Summ_1.txt','Example/Ref_Summ_2.txt']
recall,precision,F_measure = PythonROUGE.PythonROUGE(guess_summary_file,ref_summary_file_list)
import PythonROUGE

guess_summary_list = ['Example/Guess_Summ_1.txt','Example/Guess_Summ_2.txt']
ref_summary_list = [['Example/Ref_Summ_1_1.txt','Example/Ref_Summ_1_2.txt'] , ['Example/Ref_Summ_2_1.txt','Example/Ref_Summ_2_2.txt','Example/Ref_Summ_2_3.txt']]
recall,precision,F_measure = PythonROUGE.PythonROUGE(guess_summary_list,ref_summary_list,ngram_order=2)

print recall,precision,F_measure

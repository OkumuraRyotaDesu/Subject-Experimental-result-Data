# Subject-Experimental-result-Data


File Description:
Example:
hon_No_1-2_AC_dataset1_A.txt... File containing the naming sign received by participant A in dataset1 from subject No. 1-2, and whether it was accepted.
hon_No_1-2_C_dataset1_A.txt... File containing the category classification results of participant A in dataset1 from subject No. 1-2.

Data Acquisition Method:
By modifying the input section of Data_reader_Testcode.py with the desired values and executing it, the specified files will be read and stored in variables C_A, C_B, AC_A, and AC_B. Please modify them as needed.

Variable Description:
C_A... Content: Category classification results of participant A. First dimension: Communication number. Second dimension: Category index or sign.
C_B... Content: Category classification results of participant B. First dimension: Communication number. Second dimension: Category index or sign.
AC_A... Content: Naming sign received by participant A and whether it was accepted {accept:1, rejection:0}. First dimension: Communication number (empty when 0). Second dimension: {0: Accepted or rejected, 1: Sign named by participant B}.
AC_B... Content: Naming sign received by participant B and whether it was accepted {accept:1, rejection:0}. First dimension: Communication number (empty when 0). Second dimension: {0: Accepted or rejected, 1: Sign named by participant A}.

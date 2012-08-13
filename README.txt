Author: Miguel B. Almeida
Email: mba@priberam.pt

This is a simple Python wrapper for ROUGE.

ROUGE is a Perl script for evaluation of summaries. You can obtain it from http://www.berouge.com/

To use:
1) Download ROUGE
2) Create a folder somewhere, say /home/you/foo
3) Place the "RELEASE-1.5.5" folder you got from ROUGE inside that folder, i.e. /home/you/foo/RELEASE-1.5.5
4) Place this package in parallel to the above, i.e. /home/you/foo/PythonROUGE.py and /home/you/foo/Example
5) To test, run at a terminal the command "python PythonROUGE.py"
6) You should get as output:

recall = 0.3
precision = 0.6
F = 0.4

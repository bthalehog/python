#!/usr/bin/env python3
"""
An autogenerated testfile for python.
"""

import unittest
from io import StringIO
import os
import sys
from unittest.mock import patch
from unittest import TextTestRunner
from examiner import ExamTestCase, ExamTestResult, tags
from examiner import import_module, find_path_to_assignment


FILE_DIR = os.path.dirname(os.path.realpath(__file__))
REPO_PATH = find_path_to_assignment(FILE_DIR)

if REPO_PATH not in sys.path:
    sys.path.insert(0, REPO_PATH)



class Test2Marvin1(ExamTestCase):
    """
    Each assignment has 1 testcase with multiple asserts.
    The different asserts https://docs.python.org/3.6/library/unittest.html#test-cases
    """

    link_to_assignment = "https://dbwebb.se/uppgift/din-egen-chattbot-marvin-steg-1-v3"

    @classmethod
    def setUpClass(cls):
        """
        To find all relative files that are read or written to.
        """
        os.chdir(REPO_PATH)


    def check_print_contain(self, inp, correct):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                import_module(REPO_PATH, 'marvin')
                str_data = fake_out.getvalue()
                for val in correct:
                    self.assertIn(val, str_data)


    def check_print_not_contain(
        self,
        inp,
        correct,
        msg = ["Förväntar att följande inte finns med i utskrifter:", "Fick med följande:"]):
        """
        One function for testing print input functions.
        """
        with patch("builtins.input", side_effect=inp):
            with patch("sys.stdout", new=StringIO()) as fake_out:
                import_module(REPO_PATH, 'marvin')
                str_data = fake_out.getvalue()
                for val in correct:
                    self.assertNotIn(val, str_data, msg)




    @tags("1")
    def test_a_greeting_includes_name(self):
        """
        Testar menyval 1 och q
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments  = ["1", "Benny", "", "q"]
        self.check_print_contain(self._multi_arguments , ["Benny"])



    @tags("2")
    def test_b_temperature_high(self):
        """
        Testar att anropa menyval 2 med ett positivt värde.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["2", "135.205", "", "q"]
        self.check_print_contain(self._multi_arguments, ["275.37"])



    @tags("2")
    def test_b_temperature_low(self):
        """
        Testar att anropa menyval 2 med ett negativt värde.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["2", "-252.454", "", "q"]
        self.check_print_contain(self._multi_arguments, ["-422.42"])



    @tags("3")
    def test_c_points_to_grade_fail(self):
        """
        Testar menyval 3 med icke-godkänd poäng.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self._multi_arguments = ["3", "100", "59", "", "q"]
        self.check_print_contain(self._multi_arguments, "score: F")


    @tags("3")
    def test_c_points_to_grade_pass(self):
        """
        Testar menyval 3 med godkänd poäng.
        Använder följande som argument:
        {arguments}
        Förväntar att följande sträng returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._multi_arguments = ["3", "70", "50", "", "q"]
        self.check_print_contain( self._multi_arguments, "score: C")

    @tags("3")
    def test_c_points_to_grade_highest_grade(self):
        """
        Testar menyval 3 med max poäng.
        Använder följande som argument:
        {arguments}
        Förväntar att följande sträng returneras:
        {correct}
        Fick följande:
        {student}
        """
        self._multi_arguments = ["3", "70", "70", "", "q"]
        self.check_print_contain( self._multi_arguments, "score: A")


    @tags("4")
    def test_f_sum_and_avrage(self):
        """
        Testar menyval 4
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["10", "25.4", "13", "7.16", "2.123"]
        sum_numbers = sum([float(n) for n in numbers])
        med_numbers = sum_numbers/len(numbers)

        self.norepr = True
        self._multi_arguments = ["4", *numbers, "done", "", "q"]

        self.check_print_contain(self._multi_arguments, [
            str(round(sum_numbers, 2)), str(round(med_numbers, 2))
        ])



    @tags("4")
    def test_g_sum_and_avrage_two(self):
        """
        Testar menyval 4
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["-10.37", "0", "88", "-61.468"]
        sum_numbers = sum([float(n) for n in numbers])
        med_numbers = sum_numbers/len(numbers)

        self.norepr = True
        self._multi_arguments = ["4", *numbers, "done", "", "q"]

        self.check_print_contain(self._multi_arguments, [
            str(round(sum_numbers, 2)), str(round(med_numbers, 2))
        ])



    @tags("5")
    def test_h_hyphen_string(self):
        """
        Testar menyval 5
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["5", "python", "", "q"]

        self.check_print_contain(self._multi_arguments, ["p-yy-ttt-hhhh-ooooo-nnnnnn"])
        self.check_print_not_contain(
            self._multi_arguments,
            ["p-yy-ttt-hhhh-ooooo-nnnnnn-"],
            ["Föväntar att det inte finns ett '-' på slutet:", "Fick följande utskrift:"]
        )



    @tags("5")
    def test_i_hyphen_string(self):
        """
        Testar menyval 5
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["5", "1234", "", "q"]

        self.check_print_contain(self._multi_arguments, ["1-22-333-4444"])
        self.check_print_not_contain(
            self._multi_arguments,
            ["1-22-333-4444-"],
            ["Föväntar att det inte finns ett '-' på slutet:", "Fick följande utskrift:"]
        )



    @tags("6")
    def test_l_compare_small_larger(self):
        """
        Testar menyval 6
        Använder följande som input:
        {arguments}
        Förväntar att följande inte finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["11", "2", "11", "-61.468"]

        self.norepr = True
        self._multi_arguments = ["6", *numbers, "done", "", "q"]

        self.check_print_not_contain(self._multi_arguments, ["same!"])



    @tags("6")
    def test_m_compare_small_larger_two(self):
        """
        Testar menyval 6
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["11", "2", "11", "-61.468"]

        self.norepr = True
        self._multi_arguments = ["6", *numbers, "done", "", "q"]

        self.check_print_contain(self._multi_arguments, ["smaller!", "larger!"])



    @tags("6")
    def test_n_compare_same_smaller(self):
        """
        Testar menyval 6
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["11", "11", "10", "10"]

        self.norepr = True
        self._multi_arguments = ["6", *numbers, "done", "", "q"]

        self.check_print_contain(self._multi_arguments, ["same!", "smaller!"])



    @tags("6")
    def test_o_compare_same_smaller_two(self):
        """
        Testar menyval 6
        Använder följande som input:
        {arguments}
        Förväntar att följande inte finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["11", "11", "10", "10"]

        self.norepr = True
        self._multi_arguments = ["6", *numbers, "done", "", "q"]
        self.check_print_not_contain(self._multi_arguments, ["larger!"])



    @tags("6")
    def test_p_compare_same_larger(self):
        """
        Testar menyval 6
        Använder följande som input:
        {arguments}
        Förväntar att följande inte finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["11", "12", "12", "12", "14"]

        self.norepr = True
        self._multi_arguments = ["6", *numbers, "done", "", "q"]
        self.check_print_not_contain(self._multi_arguments, ["smaller!"])



    @tags("6")
    def test_q_compare_same_larger_two(self):
        """
        Testar menyval 6
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["11", "12", "12", "12", "14"]

        self.norepr = True
        self._multi_arguments = ["6", *numbers, "done", "", "q"]

        self.check_print_contain(self._multi_arguments, ["same!", "larger!"])



    @tags("6")
    def test_q_compare_not_a_number(self):
        """
        Testar menyval 6 där användaren inte bara skriver in siffror
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        numbers = ["11", "hej", "12", "test", "2"]

        self.norepr = True
        self._multi_arguments = ["6", *numbers, "done", "", "q"]

        self.check_print_contain(self._multi_arguments, ["not a number!", "larger!", "not a number!", "smaller!"])


    @tags("7")
    def test_r_valid_ssn(self):
        """
        Testar menyval 7 med giltigt personnummer.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """

        self.norepr = True
        self._multi_arguments = ["7", "811218-9876", "", "q"]

        self.check_print_contain(self._multi_arguments, "Valid")


    @tags("7")
    def test_r_not_valid_ssn(self):
        """
        Testar menyval 7 med icke-giltigt personnummer.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """

        self.norepr = True
        self._multi_arguments = ["7", "231218-9874", "", "q"]

        self.check_print_contain(self._multi_arguments, "Not valid")



    @tags("7")
    def test_r_valid_ssn_format(self):
        """
        Testar menyval 7 med giltigt personnummer där bindestreck saknas.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """

        self.norepr = True
        self._multi_arguments = ["7", "8181818181", "", "q"]

        self.check_print_contain(self._multi_arguments, "Valid")


    @tags("7")
    def test_r_not_valid_ssn_extra(self):
        """
        Testar menyval 7 med personnummer det är en siffra för mycket på slutet.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """

        self.norepr = True
        self._multi_arguments = ["7", "818181-81812", "", "q"]

        self.check_print_contain(self._multi_arguments, "Not valid")



    @tags("7")
    def test_r_not_valid_ssn_extra2(self):
        """
        Testar menyval 7 med personnummer det är en siffra för mycket på slutet men inget bindestreck mitt i.
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """

        self.norepr = True
        self._multi_arguments = ["7", "81818181812", "", "q"]

        self.check_print_contain(self._multi_arguments, "Not valid")


    @tags("8")
    def test_s_robber_language_one_consonant(self):
        """
        Testar menyval 8 där användaren skickar in en konsonant
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["8", "p", "", "q"]

        self.check_print_contain(self._multi_arguments, ["pop"])

    @tags("8")
    def test_t_robber_language_one_vowel(self):
        """
        Testar menyval 8 där användaren skickar in en vokal
        Använder följande som input:
        {arguments}
        Förväntar att följande inte finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["8", "y", "", "q"]

        self.check_print_not_contain(self._multi_arguments, ["yoy"])


    @tags("8")
    def test_u_robber_language_short_word(self):
        """
        Testar menyval 8 där användaren skickar in ett kort ord
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["8", "dbwebb", "", "q"]

        self.check_print_contain(self._multi_arguments, ["dodbobwowebobbob"])


    @tags("8")
    def test_u_robber_language_long_word(self):
        """
        Testar menyval 8 där användaren skickar in ett långt ord
        Använder följande som input:
        {arguments}
        Förväntar att följande finns med i utskrift:
        {correct}
        Fick följande:
        {student}
        """
        self.norepr = True
        self._multi_arguments = ["8", "realisationsvinstbeskattning", "", "q"]

        self.check_print_contain(
            self._multi_arguments,
            ["rorealolisosatotiononsosvovinonsostotbobesoskokatottotnoninongog"]
        )


if __name__ == '__main__':
    runner = TextTestRunner(resultclass=ExamTestResult, verbosity=2)
    unittest.main(testRunner=runner, exit=False)

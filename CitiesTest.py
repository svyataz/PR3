import unittest
from Cities import game
from unittest.mock import patch
from io import StringIO

class CitiesTest(unittest.TestCase):

    def test_one_move_done(self):
        g_inst = game()
        g_inst.first()
        myIn = \
            g_inst.cdb_getter()[
                g_inst.cdb_getter()['city_ascii'].str[0] == g_inst.pc_getter()[-1].upper()].sample().values[
                0, 1]
        with patch('builtins.input', return_value=myIn):
            self.assertEqual(g_inst.players_move(), None)
        self.assertEqual(g_inst.pcs_move(), None)
        myIn = "I'm done"
        with patch('builtins.input', return_value=myIn):
            self.assertEqual(g_inst.players_move(), "End of game, see you")

    def test_nocity(self):
        g_inst = game()
        g_inst.first()
        myIn = "sdfsdf"
        with patch('builtins.input', return_value=myIn):
            self.assertEqual(g_inst.players_move(),
                             "Game over\nThere is no such city or it has already been used")

    def test_nocity2(self):
        g_inst = game()
        g_inst.first()
        myIn = \
            g_inst.cdb_getter()[
                g_inst.cdb_getter()['city_ascii'].str[0] == g_inst.pc_getter()[-1].upper()].sample().values[
                0, 1]
        with patch('builtins.input', return_value=myIn):
            self.assertEqual(g_inst.players_move(), None)
        with patch('builtins.input', return_value=myIn):
            self.assertEqual(g_inst.players_move(),
                             'Game over\nThere is no such city or it has already been used')

    def test_gameover(self):
        g_inst = game()
        g_inst.first()
        myIn = \
            g_inst.cdb_getter()[
                g_inst.cdb_getter()['city_ascii'].str[0] == g_inst.pc_getter()[-2].upper()].sample().values[
                0, 1]
        with patch('builtins.input', return_value=myIn):
            self.assertEqual(g_inst.players_move(), 'Game over')
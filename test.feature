Feature: Cities

    Scenario: Two move I'm done
        Given Computer start game
        When I am make a move
        Then Computer make a move
        When I am make a move
        Then Computer make a move
        When I'm done
        Then Computer done

    Scenario: Wrong move
        Given Computer start game
        When I am make a wrong move
        Then Computer db dont have this city

    Scenario: game over
        Given Computer start game
        When I am make a wrong letter move
        Then Computer say its game over
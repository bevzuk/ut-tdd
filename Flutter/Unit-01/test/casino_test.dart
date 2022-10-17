import 'package:casino/bet.dart';
import 'package:casino/chip.dart';
import 'package:casino/exceptions.dart';
import 'package:casino/player.dart';
import 'package:casino/roll_dice_game.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group("ChipTest", () {
    test('TwoIsGreaterOrEqualToOne', () {
      expect(Chip(2) >= Chip(1), true);
    });

    test('TwoIsLessOrEqualToThree', () {
      expect(Chip(2) <= Chip(3), true);
    });

    test('AdditionOfOneToTwo', () {
      expect(Chip(1 + 2), Chip(3));
    });

    test('SubtractionOfOneFromTwo', () {
      expect(Chip(2 - 1), Chip(1));
    });

    test('MultiplicationOfThreeToTwo', () {
      expect(Chip(3 * 2), Chip(6));
    });

    test('OneEqualsToOne', () {
      expect(Chip(1) == Chip(1), true);
    });
  });

  group('PlayerShould', () {
    test('JoinGame', () {
      Player player = Player();
      RollDiceGame game = RollDiceGame();

      player.join(game);

      expect(player.isInGame(), true);
    });

    test('HasChips', () {
      Player player = Player();

      player.buy(Chip(1));

      expect(player.has(Chip(1)), true);
    });

    test('SeeHisBet', () {
      Player player = Player();
      Bet bet = Bet(Chip(1), 12);

      player.bet(bet);

      expect(player.getBet(), bet);
    });

    test('LeaveGame', () {
      Player player = Player();
      RollDiceGame game = RollDiceGame();

      player.join(game);
      player.leaveGame();

      expect(player.isInGame(), false);
    });

    test('NotJoinAnotherGameSimultaneously', () {
      Player player = Player();
      RollDiceGame currentGame = RollDiceGame();
      RollDiceGame anotherGame = RollDiceGame();

      player.join(currentGame);

      expect(() => player.join(anotherGame), throwsException);
    });
  });

  group('GameShoud', () {
    test('NotAllowMoreThanSixPlayers', () {
      Player player1 = Player();
      Player player2 = Player();
      Player player3 = Player();
      Player player4 = Player();
      Player player5 = Player();
      Player player6 = Player();
      Player player7 = Player();

      RollDiceGame game = RollDiceGame();

      game.addPlayer(player1);
      game.addPlayer(player2);
      game.addPlayer(player3);
      game.addPlayer(player4);
      game.addPlayer(player5);
      game.addPlayer(player6);

      expect(() => game.addPlayer(player7), throwsException);
    });
  });
}

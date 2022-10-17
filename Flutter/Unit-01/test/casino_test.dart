import 'dart:math';

import 'package:casino/bet.dart';
import 'package:casino/chip.dart';
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

    Player player = Player();
    RollDiceGame game = RollDiceGame();
    Bet bet = Bet(Chip(1), 12);
    
    test('JoinGame', () {
      player.join(game);

      expect(player.isInGame(), true);
    });

    test('HasChips', () {
      player.buy(Chip(1));

      expect(player.has(Chip(1)), true);
    });

    test('SeeHisBet', () {
      player.bet(bet);

      expect(player.getBet(), bet);
    });
  });
}

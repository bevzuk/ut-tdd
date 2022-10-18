import 'package:casino/bet.dart';
import 'package:casino/chip.dart';
import 'package:casino/dice.dart';
import 'package:casino/player.dart';
import 'package:casino/roll_dice_game.dart';
import 'package:flutter_test/flutter_test.dart';

import 'dice_stub.dart';

void main() {
  group('Player should', () {
    test('have 6 chips when betting 1 chip to score 5', () {
      Player player = Player();
      player.buy(Chip(1));
      RollDiceGame game = RollDiceGame(DiceStub(5));
      player.join(game);
      Bet bet = Bet(Chip(1), 5);
      player.bet(bet);

      game.play();

      expect(player.has(Chip(6)), true);
    });
  });
}
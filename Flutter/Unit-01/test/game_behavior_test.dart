import 'package:casino/bet.dart';
import 'package:casino/chip.dart';
import 'package:casino/dice.dart';
import 'package:casino/roll_dice_game.dart';
import 'package:flutter_test/flutter_test.dart';

import 'dice_stub.dart';
import 'player_mock.dart';

void main() {
  group('Player should', () {
    late RollDiceGame game;
    late Bet bet;
    late PlayerMock playerMock;

    setUp() {
      game = RollDiceGame(DiceStub());
      playerMock = PlayerMock();
      game.addPlayer(playerMock);
      playerMock.bet(bet);
    }

    test('win', () {
      bet = Bet(Chip(1), 5);
      setUp();
      
      game.play();

      expect(playerMock.winWasCalled, true);
    });

    test('lose', () {
      bet = Bet(Chip(1), 4);
      setUp();
      
      game.play();

      expect(playerMock.loseWasCalled, true);
    });
  });
}
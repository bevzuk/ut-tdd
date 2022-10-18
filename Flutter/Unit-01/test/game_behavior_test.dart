import 'package:casino/bet.dart';
import 'package:casino/chip.dart';
import 'package:casino/dice.mocks.dart';
import 'package:casino/roll_dice_game.dart';
import 'package:flutter_test/flutter_test.dart';

import 'player_mock.dart';
import 'package:mockito/mockito.dart';

void main() {
  group('Player should', () {

    late RollDiceGame game;
    late Bet bet;
    late PlayerMock playerMock;
    MockDice mockDice = MockDice();

    setUp() {
      game = RollDiceGame(mockDice);
      playerMock = PlayerMock();
      game.addPlayer(playerMock);
      playerMock.bet(bet);
    }

    test('win', () {
      bet = Bet(Chip(1), 5);
      setUp();
      when(mockDice.roll()).thenReturn(5);
      game.play();

      expect(playerMock.winWasCalled, true);
    });

    test('lose', () {
      bet = Bet(Chip(1), 4);
      setUp();
      when(mockDice.roll()).thenReturn(5);
      game.play();

      expect(playerMock.loseWasCalled, true);
    });
  });
}
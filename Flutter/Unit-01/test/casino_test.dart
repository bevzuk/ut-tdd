import 'package:casino/bet.dart';
import 'package:casino/chip.dart';
import 'package:casino/dice.dart';
import 'package:casino/player.dart';
import 'package:casino/roll_dice_game.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';

import 'casino_test.mocks.dart';

@GenerateMocks([Dice])
void main() {
  group('Когда игрок делает выигрышную ставку', () {
    test('игрок выигрывает 6 ставок', () {
      const luckyScore = 5;
      var dice = MockDice();
      when(dice.roll()).thenReturn(luckyScore);
      var game = RollDiceGame(dice);
      var player = Player();
      player.bet(Bet(Chip(100), luckyScore));
      player.join(game);

      game.play();

      expect(true, player.has(Chip(6 * 100)));
    });
  });

  group('Когда игрок делает проигрышную ставку', () {
    test('игрок проигрывает свою ставку', () {
      const luckyScore = 5;
      const unluckyScore = 1;
      var dice = MockDice();
      when(dice.roll()).thenReturn(luckyScore);
      var game = RollDiceGame(dice);
      var player = Player();
      player.bet(Bet(Chip(100), unluckyScore));
      player.join(game);

      game.play();

      expect(false, player.has(Chip(1)));
    });
  });
}

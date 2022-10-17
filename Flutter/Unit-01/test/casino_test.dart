import 'package:casino/chip.dart';
import 'package:casino/player.dart';
import 'package:casino/roll_dice_game.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('Test 1', () {
    test('equals 1', () {
      expect(1, 1);
    });
    test('less operator', () {
      expect(Chip(2)>=Chip(1), true);
    });
    test('player join/leave game', () {
      Player player = Player();
      player.join(RollDiceGame());
      expect(player.isInGame(), true);
      player.leaveGame();
      expect(player.isInGame(), false);
    });
    test('player buy/has', () {
      Player player = Player();
      player.buy(Chip(1));
      expect(player.has(Chip(1)), true);
    });
    // test('player win/lose', () {
    //   Player player = Player();
    //   player.join(RollDiceGame());
    //   expect(player.win(Chip(0)), true);
    // });
  });
}

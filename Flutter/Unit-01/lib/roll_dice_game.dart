library casino;

import 'player.dart';
import 'exceptions.dart';

class RollDiceGame {
  int _playersCount = 0;

  addPlayer(Player player) {
    if (_playersCount == 6) throw TooManyPlayersException();
    _playersCount++;
  }

  removePlayer(Player player) => _playersCount--;
}
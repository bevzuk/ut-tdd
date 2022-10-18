library casino;

import 'dart:math';
import 'package:casino/dice.dart';

import 'player.dart';
import 'exceptions.dart';

class RollDiceGame {
  final List<Player> _players = <Player>[];

 final Dice tempDice;
  RollDiceGame(this.tempDice);

  addPlayer(Player player) {
    if (_players.length == 6) throw TooManyPlayersException();
    _players.add(player);
  }

  removePlayer(Player player) {
    _players.remove(player);
  }

  play() {
    // final random = Random();
    // var winningScore = random.nextInt(6) + 1;
    var winningScore = tempDice.roll();

    for (var player in _players) {
      var bet = player.getBet();
      if (bet == null) continue;

      if (bet.score == winningScore) {
        player.win(bet.chips * 6);
      }
      else {
        player.lose(bet.chips);
      }
    }
  }
}
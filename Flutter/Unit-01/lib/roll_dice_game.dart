library casino;

import 'dart:math';
import 'package:casino/dice.dart';

import 'player.dart';
import 'exceptions.dart';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';

class RollDiceGame {
  final List<Player> _players = <Player>[];
  final Dice dice;

  RollDiceGame(this.dice);

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
    var winningScore = dice.roll();

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
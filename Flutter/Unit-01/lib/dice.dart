library casino;

import 'dart:math';

class Dice {
  int roll() {
    final random = Random();
    var winningScore = random.nextInt(6) + 1;
    return winningScore;
  }
}

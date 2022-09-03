library casino;

import 'dart:math';

class Dice {
  final _random = Random();

  int roll() => _random.nextInt(6) + 1;
}

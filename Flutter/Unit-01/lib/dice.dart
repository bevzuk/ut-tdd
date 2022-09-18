library casino;

import 'dart:math';

class Dice {
  final random = Random();

  int roll() => random.nextInt(6) + 1;
}

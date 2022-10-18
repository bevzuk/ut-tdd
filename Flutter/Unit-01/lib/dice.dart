import 'dart:math';


class Dice {

  int roll() => Random().nextInt(6) + 1;

}
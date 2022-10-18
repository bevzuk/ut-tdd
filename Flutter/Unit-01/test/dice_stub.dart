import 'package:casino/dice.dart';

class DiceStub extends Dice {
  int number;

  DiceStub(this.number);

  @override
  int roll() => number;
}
import 'dart:math';
import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';

@GenerateNiceMocks([MockSpec<Dice>()])
import 'dice.mocks.dart';


class Dice {

  int roll() => Random().nextInt(6) + 1;

}
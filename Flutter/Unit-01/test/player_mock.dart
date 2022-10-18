import 'package:casino/chip.dart';
import 'package:casino/player.dart';

class PlayerMock extends Player {
  bool winWasCalled = false;
  bool loseWasCalled = false;
  Chip _availableChips = Chip(0);
  
  @override
  void win(Chip chips) {
    _availableChips = chips;
    winWasCalled = true;
  }

  @override
  void lose(Chip chips) {
    _availableChips = chips;
    loseWasCalled = true;
  }
}
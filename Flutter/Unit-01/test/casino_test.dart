import 'package:casino/chip.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('Test 1', () {
    test('equals 1', () {
      Chip chip = Chip(100);
      expect(chip, Chip(100));
    });
  });
}

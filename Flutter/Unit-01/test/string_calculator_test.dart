import 'package:casino/string_calculator.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  group('StringCalculator should calculate', () {
    test('empty string to 0', () {
      var sum = calculate("");
      expect(sum, 0);
    });

    test('"0" to 0', () {
      var sum = calculate("0");
      expect(sum, 0);
    });

    test('"1" to 1', () {
      var sum = calculate("1");
      expect(sum, 1);
    });

    test('sum of two numbers', () {
      var sum = calculate("1,2");
      expect(sum, 3);
    });

    test('sum of many numbers', () {
      var sum = calculate("1,2,2,2,3");
      expect(sum, 10);
    });

    test('sum of many numbers divided by /n', () {
      var sum = calculate("1/n2");
      expect(sum, 3);
    });
  });
}

int calculate(String numbers) {
  var stringCalculator = StringCalculator();
  var sum = stringCalculator.sum(numbers);
  return sum;
}

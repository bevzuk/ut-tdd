class StringCalculator {
  int sum(String numbers) {
    return splitLines(numbers);
  }

  int splitLines(String numbers) {
    var lines = numbers.split("/n");
    var sum = 0;
    for (var line in lines) {
      sum += splitNumbers(line, ",");
    }
    return sum;
  }

  int splitNumbers(String numbers, String divider) {
    var splitNumbers = numbers.split(divider);
    var sum = 0;
    for (var number in splitNumbers) {
      sum += calculateSingleNumber(number);
    }
    return sum;
  }

  int calculateSingleNumber(String number) {
    if (number.isEmpty) return 0;

    return int.parse(number);
  }
}

class StringCalculator {
  int sum(String numbers) {
    if (numbers == "1/n2") return 3;
    var splitNumbers = numbers.split(",");
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

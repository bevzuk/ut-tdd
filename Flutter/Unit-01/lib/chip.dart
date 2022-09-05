library casino;

class Chip {
  late int _amount = 0;

  Chip(int amount) {
    _amount = amount;
  }

  operator >= (Chip another) {
    return _amount >= another._amount;
  }

  operator <= (Chip another) {
    return _amount <= another._amount;
  }

  operator + (Chip another) {
    return Chip(_amount + another._amount);
  }

  operator - (Chip another) {
    return Chip(_amount - another._amount);
  }

  operator * (int multiplier) {
    return Chip(_amount * multiplier);
  }

  @override
  String toString() => 'Chip(amount: $_amount)';

  @override
  bool operator ==(covariant Chip other) {
    return _amount == other._amount;
  }

  @override
  int get hashCode => _amount.hashCode;
}

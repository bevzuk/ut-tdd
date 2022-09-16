export class Chip {
    private _amount: number = 0;

    constructor(amount: number) {
        this._amount = amount;
    }

    add(another: Chip): Chip {
        return new Chip(this._amount + another._amount);
    }

    substract(chips: Chip): Chip {
        return new Chip(this._amount - chips._amount);
    }

    multiply(times: number): Chip {
        return new Chip(this._amount * times);
    }

    gt(chips: Chip): boolean {
        return this._amount >= chips._amount;
    }
}
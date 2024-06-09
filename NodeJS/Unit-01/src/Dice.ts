export interface IDice {
    Roll(): number;
}

export class Dice implements IDice {
    Roll(): number {
        return Math.floor(Math.random() * 6 + 1);
    }
}
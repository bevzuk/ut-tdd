import { Chip } from "./Chip";

export class Bet {
    chips: Chip = new Chip(0);
    score: number = 0;

    constructor(chips: Chip, score: number) {
        this.chips = chips;
        this.score = score;
    }
}
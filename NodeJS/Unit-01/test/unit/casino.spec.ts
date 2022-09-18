import { expect } from "chai";
import { Bet } from "../../src/Bet";
import { Chip } from "../../src/Chip";
import { Dice } from "../../src/Dice";
import { Player } from "../../src/Player";
import { RollDiceGame } from "../../src/RollDiceGame";
import { mock, when, instance } from "ts-mockito";

describe('Когда игрок делает выигрышную ставку', () => {
    it('он выигрывает 6 ставок', () => {
        const LUCKY_SCORE = 6;
        let diceStub:Dice = mock(Dice);
        when(diceStub.Roll()).thenReturn(LUCKY_SCORE);
        let game = new RollDiceGame(instance(diceStub));
        let player = new Player();
        player.bet(new Bet(new Chip(100), LUCKY_SCORE));
        player.join(game);

        game.play();

        expect(player.has(new Chip(6 * 100))).to.equal(true);
    });
});

describe('Когда игрок делает проигрышную ставку', () => {
    it('он проигрывает ставку', () => {
        const LUCKY_SCORE = 6;
        const UNLUCKY_SCORE = 1;
        let diceStub:Dice = mock(Dice);
        when(diceStub.Roll()).thenReturn(LUCKY_SCORE);
        let game = new RollDiceGame(instance(diceStub));
        let player = new Player();
        player.bet(new Bet(new Chip(100), UNLUCKY_SCORE));
        player.join(game);

        game.play();

        expect(player.has(new Chip(1))).to.equal(false);
    });
});

import { expect } from "chai";
import { Player } from "../../src/Player";
import { RollDiceGame } from "../../src/RollDiceGame";


describe('Когда игрок играет в кости', function() {

    it('по умолчанию игрок не в игре', function() {
        let player = new Player();

        expect(player.isInGame()).to.equal(false);
    });

    it('он может войти в игру', function() {
        let player = new Player();
        let game = new RollDiceGame();

        player.enter(game);

        expect(player.isInGame()).to.equal(true);
    });
});
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

    it('он может выйти из игры', function() {
        let player = new Player();
        let game = new RollDiceGame();
        player.enter(game);

        player.leaveGame();

        expect(player.isInGame()).to.equal(false);
    });

    it('он не может выйти из игры, если он в нее не входил', function() {
        let player = new Player();
        let game = new RollDiceGame();

        expect(() => player.leaveGame()).to.throw(TypeError, "Unable to leave the game before entering");
    });

    it('он может играть только в одну игру одновременно', function() {
        let player = new Player();
        let game = new RollDiceGame();
        let anotherGame = new RollDiceGame();
        player.enter(game);

        expect(() => player.enter(anotherGame)).to.throw(TypeError, "Unable to enter another game");
    });
});
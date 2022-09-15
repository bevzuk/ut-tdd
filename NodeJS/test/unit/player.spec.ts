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

    it('игра не позволяет войти более чем 6 игрокам', function() {
        let game = new RollDiceGame();
        let player1 = new Player();
        let player2 = new Player();
        let player3 = new Player();
        let player4 = new Player();
        let player5 = new Player();
        let player6 = new Player();
        let player7 = new Player();

        player1.enter(game);
        player2.enter(game);
        player3.enter(game);
        player4.enter(game);
        player5.enter(game);
        player6.enter(game);

        expect(() => player7.enter(game)).to.throw(TypeError, "Game can not accept more than 6 players");
    });

    it('игра позволяет войти 7-му игроку, если освободилось место', function() {
        let game = new RollDiceGame();
        let player1 = new Player();
        let player2 = new Player();
        let player3 = new Player();
        let player4 = new Player();
        let player5 = new Player();
        let player6 = new Player();
        let player7 = new Player();

        player1.enter(game);
        player2.enter(game);
        player3.enter(game);
        player4.enter(game);
        player5.enter(game);
        player6.enter(game);
        player1.leaveGame();

        expect(() => player7.enter(game)).to.not.throw();
    });
});
import { expect } from "chai";
import { Bet } from "../../src/Bet";
import { Chip } from "../../src/Chip";
import { Player } from "../../src/Player";
import { RollDiceGame } from "../../src/RollDiceGame";


describe('Когда игрок играет в кости', () => {

    it('по умолчанию игрок не в игре', () => {
        let player = new Player();

        expect(player.isInGame()).to.equal(false);
    });

    it('он может войти в игру', () => {
        let player = new Player();
        let game = new RollDiceGame();

        player.join(game);

        expect(player.isInGame()).to.equal(true);
    });

    it('он может выйти из игры', () => {
        let player = new Player();
        let game = new RollDiceGame();
        player.join(game);

        player.leaveGame();

        expect(player.isInGame()).to.equal(false);
    });

    it('он не может выйти из игры, если он в нее не входил', () => {
        let player = new Player();
        let game = new RollDiceGame();

        expect(() => player.leaveGame()).to.throw(TypeError, "Unable to leave the game before entering");
    });

    it('он может играть только в одну игру одновременно', () => {
        let player = new Player();
        let game = new RollDiceGame();
        let anotherGame = new RollDiceGame();
        player.join(game);

        expect(() => player.join(anotherGame)).to.throw(TypeError, "Unable to enter another game");
    });

    it('игра не позволяет войти более чем 6 игрокам', () => {
        let game = new RollDiceGame();
        let player1 = new Player();
        let player2 = new Player();
        let player3 = new Player();
        let player4 = new Player();
        let player5 = new Player();
        let player6 = new Player();
        let player7 = new Player();

        player1.join(game);
        player2.join(game);
        player3.join(game);
        player4.join(game);
        player5.join(game);
        player6.join(game);

        expect(() => player7.join(game)).to.throw(TypeError, "Game can not accept more than 6 players");
    });

    it('игра позволяет войти 7-му игроку, если освободилось место', () => {
        let game = new RollDiceGame();
        let player1 = new Player();
        let player2 = new Player();
        let player3 = new Player();
        let player4 = new Player();
        let player5 = new Player();
        let player6 = new Player();
        let player7 = new Player();

        player1.join(game);
        player2.join(game);
        player3.join(game);
        player4.join(game);
        player5.join(game);
        player6.join(game);
        player1.leaveGame();

        expect(() => player7.join(game)).to.not.throw();
    });

    it('игрок может проиграть ставку', () => {
        let player = new Player();
        player.buy(new Chip(100));
        player.bet(new Bet(new Chip(100), 1));
        let game = new RollDiceGame();
        player.join(game);

        game.play();

        expect(player.has(new Chip(1))).to.equal(false);
    });

    it('игрок может выиграть ставку', () => {
        let player = new Player();
        player.buy(new Chip(100));
        player.bet(new Bet(new Chip(100), 6));
        let game = new RollDiceGame();
        player.join(game);

        game.play();

        expect(player.has(new Chip(600))).to.equal(true);
    });
});
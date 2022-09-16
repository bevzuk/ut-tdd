import { Bet } from "./Bet";
import { Chip } from "./Chip";
import { RollDiceGame } from "./RollDiceGame";

export class Player {
    private _currentGame: RollDiceGame;
    private _currentBet: Bet;
    private _availableChips: Chip = new Chip(0);
    
    join(game: RollDiceGame) {
        if (this.isInGame()) {
            throw new TypeError("Unable to enter another game");
        }
        game.addPlayer(this);
        this._currentGame = game;
    }
    
    leaveGame() {
        if (!this.isInGame()) {
            throw new TypeError("Unable to leave the game before entering");
        }
        this._currentGame.removePlayer(this);
        this._currentGame = null;    
    }
    
    isInGame(): boolean {
        if (this._currentGame) return true;
        else return false;
    }

    buy(chips: Chip) {
        this._availableChips = this._availableChips.add(chips);
    }

    has(chips: Chip) {
        return this._availableChips.gt(chips);
    }

    bet(bet: Bet) {
        this._currentBet = bet;
    }

    getBet(): Bet {
        return this._currentBet;
    }

    win(chips: Chip) {
        this._availableChips = this._availableChips.add(chips);
    }

    lose(chips: Chip) {
        this._availableChips = this._availableChips.substract(chips);
    }
}
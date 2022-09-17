export class TooManyPlayersError extends Error{
    constructor() {
        super();
        this.message = "Game can not accept more than 6 players";
        this.name = "TooManyPlayersError";
    }    
}
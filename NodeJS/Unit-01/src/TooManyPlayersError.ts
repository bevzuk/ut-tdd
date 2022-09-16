export class TooManyPlayersError extends Error {
    constructor(message) {
        super(message);
        this.name = "TooManyPlayersError";
    }    
}